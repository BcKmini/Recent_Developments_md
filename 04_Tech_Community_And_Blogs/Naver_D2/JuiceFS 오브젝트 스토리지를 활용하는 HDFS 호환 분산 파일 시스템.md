# JuiceFS: 오브젝트 스토리지를 활용하는 HDFS 호환 분산 파일 시스템

**출처:** [Naver_D2](https://d2.naver.com/helloworld/5215257)

## 요약
네이버에서는 다양한 서비스를 위해 공용 Hadoop 클러스터를 운영하고 있으며, Spark, Hive, MapReduce 등의 Hadoop 애플리케이션에서 처리한 데이터는 HDFS에 저장됩니다. HDFS는 Hadoop 에코시스템에서 데이터 로컬리티(data locality)를 지원해 높은 성능을 제공하며 내결함성과 확장성 측면에서도 우수하다는 장점이 있습니다.

그러나 최근 AI 서비스 확산으로 데이터 규모가 급격히 증가하고, 다양한 형태의 데이터 저장 요구가 늘어나고 있습니다. 또한 Hadoop 클러스터 외부의 AI 플랫폼(Kubernetes)과 데이터를 효율적으로 공유하는 문제도 중요한 과제가 되었습니다.

이러한 변화 속에서 오브젝트 스토리지가 HDFS의 대안이 될 수 있는지 살펴보고, 이를 보완할 수 있는 JuiceFS를 소개합니다. 이 글은 [AI 플랫폼을 위한 스토리지 JuiceFS 도입기](https://d2.naver.com/helloworld/4555524)의 후속으로, Hadoop 환경에서의 JuiceFS 활용 방법과 장점을 설명합니다.

HDFS의 한계
--------

### 1. 저장 비용 증가

AI 개발을 위해서는 지속적으로 늘어나는 데이터를 비용 효율적으로 저장해야 합니다. 모델 개선과 재학습을 위해 원본 데이터를 장기간 보존해야 하는 경우도 생깁니다.

그러나 Hadoop은 컴퓨팅과 스토리지가 강하게 결합되어 있어 스토리지만 독립적으로 확장하기 어렵습니다. 컴퓨팅 수요가 없는 상태에서 스토리지 공간을 확보하기 위해 노드를 추가하면 비용이 낭비될 수 있습니다. 또한, HDFS는 기본적으로 3중 복제(replication)를 유지해야 하므로 저장 비용 부담이 큽니다.

### 2. 파일 개수 제한

AI 개발에는 이미지, 음성, 텍스트 등 수천만 개의 작은 파일이 사용됩니다.

HDFS에는 잘 알려진 [작은 파일 문제](https://www.cloudera.com/blog/technical/the-small-files-problem.html)가 있습니다. 이는 모든 파일과 블록의 메타데이터가 네임노드 메모리에 저장되기 때문입니다. 예를 들어 1천만 개의 파일을 관리하려면 약 3GB의 메모리가 필요합니다. 결국 HDFS에서 관리할 수 있는 파일 개수는 단일 네임노드 메모리 용량에 의해 제한됩니다.

### 3. 데이터센터 재해 대응 취약

HDFS는 일반적으로 단일 데이터센터의 노드들로 구성됩니다. 데이터센터 장애나 재해에 대비하려면 타 데이터센터로 데이터를 복제하는 별도의 설루션이 필요하며 이로 인해 추가 비용이 발생합니다.

### 4. 운영 비용 증가

네이버는 전문 인력이 공용 Hadoop 클러스터를 운영하고 있어 상대적으로 부담이 적지만, 일반적으로 Hadoop 클러스터 구축과 운영은 매우 복잡하고 비용이 큽니다. 개별적으로 안정적인 Hadoop 환경을 구축,운영하려면 전문 지식과 높은 유지 비용이 필요합니다.

### 5. Kubernetes에서 낮은 사용성

네이버 AI 플랫폼은 Kubernetes 기반으로 구축되어 있으며, GPU 지원과 함께 Kubeflow, KServe 등 다양한 AI 오픈소스를 활용합니다.

하지만 HDFS는 POSIX API와 CSI 드라이버를 지원하지 않기 때문에 Kubernetes의 일반적인 스토리지 사용 방식인 PersistentVolume으로 사용할 수 없습니다. 따라서 HDFS를 Kubernetes에서 사용하려면 컨테이너에 Hadoop 패키지, 설정, 인증 정보를 준비하고 HDFS API로 코드를 작성해야 합니다. 이는 매우 번거롭고 AI 개발의 생산성을 저하시킵니다.

오브젝트 스토리지의 이점
-------------

Hadoop은 데이터 로컬리티를 통해 높은 성능을 제공하지만, 이로 인해 컴퓨팅과 스토리지 리소스를 분리하기 어렵습니다. HDFS는 컴퓨팅 노드와 결합되어 운영되므로, 단순히 저장 공간(HDFS)을 확장하려 해도 추가 Hadoop 노드를 투입해야 합니다.

반면, 클라우드 환경에서는 컴퓨팅과 스토리지를 독립적으로 확장할 수 있습니다.

![](https://d2.naver.com/content/images/2025/09/d178625e-20b5-4785-81b0-92416aab45ef.png)

클라우드 환경에서는 일반적으로 HDFS 대신 오브젝트 스토리지에 데이터를 저장합니다. 예를 들어, Hadoop 클러스터를 대체하는 관리형 컴퓨팅 서비스(AWS EMR, Google Dataproc)나 Kubernetes 기반 데이터 처리 엔진을 사용하고 오브젝트 스토리지(S3, GCS)에 데이터를 저장합니다. 이를 통해 컴퓨팅과 스토리지가 분리된 구조에서 리소스를 유연하게 확장할 수 있습니다.

또한, Hadoop 커뮤니티와 클라우드 벤더는 오브젝트 스토리지를 HDFS처럼 활용할 수 있도록 [S3A](https://hadoop.apache.org/docs/r3.4.1/hadoop-aws/tools/hadoop-aws/index.html), [Azure Blob](https://hadoop.apache.org/docs/r3.4.1/hadoop-azure/index.html), [Aliyun OSS](https://hadoop.apache.org/docs/r3.4.1/hadoop-aliyun/tools/hadoop-aliyun/index.html) 등의 HDFS 호환 파일 시스템을 제공합니다.

![](https://d2.naver.com/content/images/2025/09/f82b8549-50d6-40d2-963e-7d57533da516.png)

오브젝트 스토리지는 원격 저장소이므로 데이터 로컬리티를 취하기는 어렵지만 다음과 같은 장점이 있습니다.

* 저장 비용 절감

컴퓨팅과 스토리지를 분리해 독립적으로 확장할 수 있습니다. 일반적으로 오브젝트 스토리지는 비용이 저렴하며 필요에 따라 다양한 스토리지 클래스를 선택할 수 있습니다. 예를 들어, 자주 접근하지 않지만 장기 보관이 필요한 데이터에는 저비용 스토리지 클래스(S3 Glacier)를 사용합니다.

* 뛰어난 확장성과 탄력성

오브젝트 스토리지는 사실상 무제한 확장을 지원하도록 설계되었습니다. 오브젝트 개수나 용량에 제한이 없으며, 워크로드 변화에 따라 손쉽게 확장하거나 축소할 수 있습니다.

* 데이터센터 재해 복구 지원

S3와 같은 오브젝트 스토리지는 리전 간 복제 기능을 제공해, 데이터센터 장애나 재해 상황에서도 데이터 손실을 예방할 수 있습니다.

* 운영 비용 감소

Hadoop 클러스터의 구축과 운영 부담을 피할 수 있어 운영 비용이 절감됩니다.

오브젝트 스토리지의 한계
-------------

그런데 HDFS를 오브젝트 스토리지로 대체하는 것이 항상 좋을까요?

HDFS 호환 파일 시스템으로 지원되는 [S3A](https://hadoop.apache.org/docs/r3.4.1/hadoop-aws/tools/hadoop-aws/index.html#Introducing_the_Hadoop_S3A_client)는 S3 오브젝트 스토리지를 HDFS처럼 사용할 수 있게 합니다. 하지만 실제로는 오브젝트 스토리지에 저장된다는 것을 이해해야 합니다.

### 1. 디렉터리 미지원

파일 시스템에서는 파일 계층 정보가 디렉터리에 담깁니다. 따라서 파일 Listing은 파일 시스템에서 기본적인 오퍼레이션이며 빠릅니다.

반면, 오브젝트 스토리지는 디렉터리에 해당하는 개념이 없고 모든 오브젝트가 독립적인 flat 구조입니다. 따라서 파일 Listing은 오브젝트의 prefix 검색으로 구현되어 느립니다. 또한, 디렉터리를 지원하기 위해 임시로 생성하는 [Directory Marker](https://hadoop.apache.org/docs/r3.4.1/hadoop-aws/tools/hadoop-aws/directory_markers.html) 오브젝트가 성능 저하를 발생시키기도 합니다.

![](https://d2.naver.com/content/images/2025/09/126af790-58ec-4f52-a70a-60796f3c231a.png)

출처: [JuiceFS Blog - From Hadoop to Cloud: Why and How to Decouple Storage and Compute in Big Data Platforms](https://juicefs.com/en/blog/solutions/hadoop-cloud-decouple-storage-compute-big-data)

### 2. Rename 미지원

파일 시스템에서 Rename은 기본적인 연산으로, O(1) 수준의 원자적 트랜잭션으로 빠르게 수행됩니다. 그러나 오브젝트 스토리지는 Rename을 지원하지 않기 때문에 전체 데이터를 복사한 뒤 원본을 삭제하는 방식으로 처리됩니다. 이로 인해 속도가 매우 느리며, 중간에 실패할 가능성도 있습니다.

이 문제는 MapReduce와 Spark의 Commit 동작과도 밀접하게 관련된 널리 알려진 이슈입니다(참고: [Apache Hadoop Amazon Web Services support – Committing work to S3 with the S3A Committers](https://hadoop.apache.org/docs/r3.4.1/hadoop-aws/tools/hadoop-aws/committers.html#Introduction:_The_Commit_Problem)). OutputCommit은 태스크 재시도와 병렬 처리 시 일관성을 보장하기 위해 필요하며, 일반적으로 사용하는 FileOutputFormatCommitter는 Rename 기반으로 구현되어 있습니다. 따라서 오브젝트 스토리지에서 FileOutputFormatCommitter를 그대로 사용하면 심각한 성능 저하가 발생합니다.

이에 대응하기 위해서는 Rename을 사용하지 않고, 오브젝트 스토리지에 최적화된 방식으로 구현된 [Magic Committer](https://hadoop.apache.org/docs/r3.4.1/hadoop-aws/tools/hadoop-aws/committers.html#The_Magic_Committer)를 사용해야 합니다.

![](https://d2.naver.com/content/images/2025/09/622ee2ac-3849-4568-b369-158809471ca5.png)

출처: [Improve s3 write performance with magic committer in Spark3](https://medium.com/towards-data-engineering/improve-s3-write-performance-with-magic-committer-in-spark3-d509e49f9710)

### 3. 파일 권한 미지원

HDFS는 POSIX 권한 체계를 지원해, 파일/디렉터리의 owner, group, others 권한을 설정할 수 있습니다. 반면, 오브젝트 스토리지에서는 이를 지원하지 않으므로 파일의 소유자, 그룹은 현재 사용자로, 모든 파일, 디렉터리 권한은 각각 666, 777로 취급합니다(참고: [Object Stores vs. Filesystems](https://hadoop.apache.org/docs/r3.4.1/hadoop-project-dist/hadoop-common/filesystem/introduction.html#Object_Stores_vs._Filesystems)).

### 4. 느린 데이터 접근

오브젝트 스토리지는 원격 저장 공간입니다. 데이터 로컬리티을 보장할 수 없고 항상 네트워크 비용이 발생합니다. 따라서 HDFS 대비 성능 저하가 발생합니다.

### 5. Kubernetes에서의 낮은 사용성

POSIX API를 지원해 오브젝트 스토리지를 로컬 파일 시스템처럼 마운트할 수 있게 하는 [Mountpoint for Amazon S3](https://github.com/awslabs/mountpoint-s3), [s3fs](https://github.com/s3fs-fuse/s3fs-fuse) 등의 프로젝트가 있습니다. 또한, AWS S3는 [Mountpoint for Amazon S3 CSI Driver](https://github.com/awslabs/mountpoint-s3-csi-driver)를 지원하여 Kubernetes 볼륨으로 사용하기도 합니다.

하지만 오브젝트 스토리지와 파일 시스템에는 근본적인 차이가 있으므로 POSIX API와 완전히 호환되지 못하고 성능 저하가 큽니다. 따라서 이러한 도구는 [작동 방식과 제약 사항](https://github.com/awslabs/mountpoint-s3/blob/main/doc/SEMANTICS.md)을 충분히 이해한 뒤 사용해야 합니다. 결국 HDFS와 마찬가지로, 오브젝트 스토리지를 사용하더라도 Kubernetes 환경에서의 낮은 사용성 문제는 여전히 해소되지 않습니다.

### 6. S3 호환 오브젝트 스토리지의 S3 API 호환

S3는 사실상 오브젝트 스토리지의 표준으로 자리 잡아 다양한 애플리케이션에서 널리 지원됩니다. 이 때문에 여러 클라우드 벤더와 오픈소스 프로젝트에서 S3 호환 오브젝트 스토리지를 제공하고 있습니다.

그러나 S3 호환 오브젝트 스토리지가 곧 S3 자체를 의미하는 것은 아닙니다. 따라서 S3AFileSystem이나 애플리케이션에서 사용하는 S3 API를 문제없이 지원하는지 확인해야 합니다.

![](https://d2.naver.com/content/images/2025/09/e490cc14-c570-40dd-83a8-b9e4e2f0eacd.png)

### 정리

오브젝트 스토리지를 HDFS처럼 사용할 수는 있지만 한계를 이해해야 합니다. 기존의 HDFS 기반에서 작성된 Hadoop 애플리케이션을 [S3A](https://hadoop.apache.org/docs/r3.4.1/hadoop-aws/tools/hadoop-aws/index.html#Introducing_the_Hadoop_S3A_client)로 변경하기만 하면 오브젝트 스토리지를 문제없이 사용할 수 있을까요?

직접 HDFS API로 작성한 코드는 Rename을 회피하거나 Listing을 줄여 오브젝트 스토리지에 맞게 다시 작성해야 합니다. 기존 Spark 애플리케이션의 성능 저하를 피하려면 [Magic Committer](https://hadoop.apache.org/docs/r3.4.1/hadoop-aws/tools/hadoop-aws/committers.html#The_Magic_Committer) 사용을 검토해야 합니다. Magic Committer가 항상 유효하지도 않습니다. [Spark Dynamic Partition overwriting](https://docs.cloudera.com/runtime/7.3.1/cloud-data-access/topics/cr-cda-manifest-committer-spark-dynamic-partition.html)과 같이 지원하지 못하는 경우도 있습니다. 오브젝트 스토리지와 관련된 이슈는 Spark, Hadoop 커뮤니티에 의해 개선되고 있지만, 이슈를 파악하고 패키지 버전을 갱신하는 것도 쉽지는 않습니다. 또한, S3 호환 오브젝트 스토리지를 사용하는 경우에는 S3 API 호환성에 대한 검증도 필요합니다. 이처럼 기존의 Hadoop 애플리케이션을 그대로 사용하기는 어렵고 별도의 개발과 노력이 필요합니다.

JuiceFS란
--------

JuiceFS는 메타데이터 엔진과 데이터 스토리지로 구성된 분산 파일 시스템입니다. 오브젝트 스토리지에는 데이터 블럭만 저장되고 파일 시스템 구축을 위한 메타데이터는 데이터베이스에서 관리됩니다.

JuiceFS가 HDFS와 유사한 **분산 파일 시스템**이라는 점에 주목해야 합니다. 이 때문에 오브젝트 스토리지를 그대로 사용하는 것과 달리 HDFS API, POSIX API, Kubernetes CSI 드라이버를 완벽하게 지원할 수 있습니다.

![](https://d2.naver.com/content/images/2025/09/2fd0fa70-cbb9-4622-bfc5-bf4006070419.png)

출처: [JuiceFS Document Center - Architecture](https://juicefs.com/docs/community/architecture)

JuiceFS는 어떻게 오브젝트 스토리지와 데이터베이스로 분산 파일 시스템을 구현할까요? JuiceFS는 느리고 수정이 어려운 오브젝트 스토리지에 파일을 저장하기 위해 chunk, slice, block 개념을 도입했습니다.

* chunk(64MB): 파일을 64MB 단위로 나눠 오프셋 기반 병렬 처리 가능
* slice: chunk 내 수정 단위로, 쓰기 시 새로운 slice 생성 후 최신 버전을 우선함
* block(기본 4MB): 실제 오브젝트 스토리지에 저장되는 최소 단위로, 병렬 처리로 업로드 시간 단축

이로써 대규모 데이터 처리와 기존 파일 수정이 가능한 파일 시스템이 구현됩니다.

![](https://d2.naver.com/content/images/2025/09/55ec10af-6108-4324-9ee2-9174b9ffa14b.png)

출처: [JuiceFS Document Center - Architecture](https://juicefs.com/docs/community/architecture)

JuiceFS는 기본적으로 여러 단계의 캐싱을 지원합니다. 원격의 오브젝트 스토리지에서 데이터를 읽는 것은 느리기 때문에 캐싱으로 이를 보완합니다.

![](https://d2.naver.com/content/images/2025/09/f9a951d6-fd07-45b3-8bb6-4b2a2ae6317a.png)

출처: [JuiceFS Document Center - Cache](https://juicefs.com/docs/community/guide/cache/#data-cache)

네이버 사내 AI 플랫폼에서는 이미 JuiceFS를 활용하고 있습니다. JuiceFS에 대한 더 자세한 내용과 AI 플랫폼 도입 과정을 [AI 플랫폼을 위한 스토리지 JuiceFS 도입기](https://d2.naver.com/helloworld/4555524)에서 살펴볼 수 있습니다.

Hadoop에서 JuiceFS 사용하기
---------------------

JuiceFS는 Hadoop SDK를 지원하는 [Hadoop 호환 파일 시스템](https://hadoop.apache.org/docs/r3.4.1/hadoop-project-dist/hadoop-common/filesystem/introduction.html)입니다. JuiceFS를 설정하고 Hadoop SDK를 배포해 JuiceFS 파일 시스템을 사용할 수 있습니다.

### JuiceFS 설정하기

Hadoop에서 JuiceFS 파일 시스템을 인식하게 하려면 core-site.xml 파일에 다음 내용을 추가해야 합니다. [`fs.jfs.impl`, `fs.AbstractFileSystem.jfs.impl`, `juicefs.meta`는 필수](https://juicefs.com/docs/community/hadoop_java_sdk/#core-configurations)입니다.

```
<!-- jfs://로 JuiceFS를 사용할 수 있도록 설정 -->  
  <property>
    <name>fs.jfs.impl</name>
    <value>io.juicefs.JuiceFileSystem</value>
  </property>
  <property>
    <name>fs.AbstractFileSystem.jfs.impl</name>
    <value>io.juicefs.JuiceFS</value>
  </property>
<!-- juicefs meta url -->  
  <property>
    <name>juicefs.meta</name>
    <value>redis://:password@addr</value>
  </property>
<!-- 본 예시에서는 모든 사용자에게 접근 권한을 부여해, 권한 문제가 없도록 한다. -->  
  <property>
    <name>juicefs.umask</name>
    <value>000</value>
  </property>
<!-- 최대 100GiB까지 캐싱한다. -->  
  <property>
    <name>juicefs.cache-size</name>
    <value>102400</value>
  </property>
<!-- YARN 컨테이너의 임시 경로 하위에 캐싱하여, 컨테이너가 종료되면 캐싱도 제거된다.  
공용 Hadoop이므로 작업 수행 동안에만 임시로 캐싱한다. -->
  <property>
    <name>juicefs.cache-dir</name>
    <value>${env.PWD}/tmp</value>
  </property>
<!-- 지표 수집을 위한 Prometheus remote write 설정 -->  
  <property>
    <name>juicefs.push-remote-write</name>
    <value>http://host:port</value>
  </property>
  <property>
    <name>juicefs.push-remote-write-auth</name>
    <value>username:password</value>
  </property>
<!-- Hadoop 사용자, YARN 컨테이너 ID를 추가로 수집한다.  
공용 Hadoop이므로 사용자, 앱을 구분하기 위한 것이다 -->
  <property>
    <name>juicefs.push-labels</name>
    <value>user:${env.USER};container_id:${env.CONTAINER_ID}</value>
  </property>
```

위에서는 하나의 `default` 파일 시스템만 설정했으나, 필요하다면 [여러 파일 시스템을 설정](https://juicefs.com/docs/community/hadoop_java_sdk/#multiple-file-systems-configuration)해 동시에 사용하는 것도 가능합니다.

더 다양한 설정 옵션은 [Client Configurations](https://juicefs.com/docs/community/hadoop_java_sdk/#client-configurations)에서 살펴볼 수 있습니다.

### Hadoop SDK

Hadoop SDK가 포함된 JAR 파일은 [미리 컴파일된 클라이언트를 다운로드](https://juicefs.com/docs/community/getting-started/installation/#install-the-pre-compiled-client)하거나 [직접 소스 코드를 컴파일](https://juicefs.com/docs/community/getting-started/installation#manually-compiling)할 수 있습니다.

쉬운 배포 방법은 모든 Hadoop 노드의 [Hadoop 배포판별 설치 경로](https://juicefs.com/docs/community/hadoop_java_sdk/#big-data-platforms)에 미리 설치해 두는 것입니다. 하지만 이 방법은 대규모 Hadoop 클러스터에서는 번거로운 작업이며, 특히 공용 Hadoop에서는 모든 사용자가 특정 버전만 사용해야 한다는 제한이 생깁니다.

대부분의 Hadoop 애플리케이션은 원하는 JAR 파일을 배포하고 classpath에 추가하는 방법을 제공하므로 사용자가 필요에 따라 직접 배포하고 사용할 수 있습니다. 아래에서 HDFS CLI, MapReduce, Spark에서의 방법을 설명합니다.

#### HDFS CLI

앞에서 설명한 core-site.xml 파일을 설정한 후 `HADOOP_CLASSPATH` 환경 변수에 Hadoop SDK 파일 경로를 설정합니다. 다음과 같이 [hdfs](https://hadoop.apache.org/docs/r3.4.1/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html) 명령으로 `hdfs://`, `jfs://`를 사용할 수 있습니다.

```
$ export HADOOP_CLASSPATH=/home/juicefs/juicefs-hadoop-1.2.3.jar
$ hdfs dfs -ls hdfs://home/foo
Found 6 items  
...
drwx------   - foo users          0 2022-10-14 20:55 hdfs://home/foo/.Trash  
drwx------   - foo users          0 2022-01-06 10:18 hdfs://home/foo/dfsio  
drwx------   - foo users          0 2025-01-22 17:54 hdfs://home/foo/tpcds

$ hdfs dfs -ls jfs://default/
2025-08-25 19:15:43,964 INFO fs.TrashPolicyDefault: Namenode trash configuration: Deletion interval = 60 minutes, Emptier interval = 60 minutes.  
Found 8 items  
...
drwxrwxrwx   - 10000 hadoop-admins       4096 2025-06-10 18:06 jfs://default/nyc  
drwxrwxrwx   - 10000 hadoop-admins       4096 2025-05-15 19:42 jfs://default/subdir
```

#### MapReduce

MapReduce는 Hadoop의 여러 노드에서 동시에 실행되므로 작업이 할당된 모든 노드에 JAR 파일이 배포되어야 합니다. 권장하는 방법은 [분산 캐시](https://hadoop.apache.org/docs/r3.4.1/hadoop-mapreduce-client/hadoop-mapreduce-client-core/DistributedCacheDeploy.html)에 따라 배포하는 것입니다. 이 방식을 사용하면 작업 수행 시 `mapreduce.application.framework.path`에 설정한 MapReduce 프레임워크를 작업 노드에 자동으로 배포합니다.

mapred-site.xml 파일의 예시입니다.

* `mapreduce.application.framework.path`: Hadoop SDK가 포함된 MapReduce 프레임워크의 HDFS 경로
* `mapreduce.application.classpath`: Hadoop SDK가 포함되도록 설정

```
 <property>
   <name>mapreduce.application.classpath</name>
   <value>$PWD/mr-framework/hadoop/share/hadoop/mapreduce/*:$PWD/mr-framework/hadoop/share/hadoop/mapreduce/lib/*:$PWD/mr-framework/hadoop/share/hadoop/common/*:$PWD/mr-framework/hadoop/share/hadoop/common/lib/*:$PWD/mr-framework/hadoop/share/hadoop/yarn/*:$PWD/mr-framework/hadoop/share/hadoop/yarn/lib/*:$PWD/mr-framework/hadoop/share/hadoop/hdfs/*:$PWD/mr-framework/hadoop/share/hadoop/hdfs/lib/*:$PWD/mr-framework/hadoop/share/hadoop/tools/lib/*</value>
 </property>
 <property>
   <name>mapreduce.application.framework.path</name>
   <value>hdfs://mapred/framework/hadoop-mapreduce-3.1.2-juicefs-1.2.3.tar.gz#mrframework</value>
 </property>
```

#### Spark

Spark의 기본 설정은 spark-defaults.conf 파일입니다. core-site.xml 파일 대신 spark-defaults.conf 파일에 다음과 같이 설정합니다.

* 임의의 Hadoop 설정은 `spark.hadoop.key=value`와 같이 추가([참고](https://spark.apache.org/docs/3.5.1/configuration.html#custom-hadoophive-configuration))
* `spark.jars`: Spark driver, executor에 배포하고 classpath로 포함시킬 JAR 파일 명시

```
spark.hadoop.fs.jfs.impl io.juicefs.JuiceFileSystem  
spark.hadoop.fs.AbstractFileSystem.jfs.impl io.juicefs.JuiceFS  
spark.hadoop.juicefs.meta redis://:password@addr  
spark.hadoop.juicefs.umask 000  
spark.hadoop.juicefs.push-remote-write http://host:port  
spark.hadoop.juicefs.push-remote-write-auth username:password  
spark.hadoop.juicefs.push-labels user:${env.USER};container_id:${env.CONTAINER_ID}  
spark.hadoop.juicefs.cache-size 102400  
spark.hadoop.juicefs.cache-dir ${env.PWD}/tmp  
spark.jars hdfs://juicefs/juicefs-hadoop/juicefs-hadoop-1.2.3.jar
```

JuiceFS 개선 이슈
-------------

JuiceFS는 다양한 인터페이스를 제공해 여러 플랫폼 간 데이터 공유가 가능합니다. 예를 들어, Hadoop에서 MapReduce나 Spark로 처리한 데이터를 JuiceFS에 저장하면 이후 Kubernetes 환경에서도 쉽게 활용할 수 있습니다.

네이버 공용 Hadoop과 Kubernetes 기반 플랫폼들이 원활하게 데이터를 공유하기 위해 몇 가지 개선이 필요했습니다.

### [all-squash 마운트 지원](https://github.com/juicedata/juicefs/issues/5394)

네이버 공용 Hadoop은 LDAP과 연동해 사용자 계정을 관리합니다. 따라서 Hadoop에서 생성한 데이터는 해당 사용자의 LDAP UID와 GID로 소유합니다. 반면 Kubernetes에서는 컨테이너를 임의의 UID, GID로 실행할 수 있어, Hadoop에서 생성한 데이터에 접근할 때 권한 문제가 발생할 수 있습니다.

이를 해결하기 위해 마운트 옵션 [--all-squash](https://juicefs.com/docs/community/command_reference/#mount-fuse-options)를 추가했습니다. 이 옵션은 마운트 경로 접근 시 현재 계정이 아니라 지정한 UID:GID로 접근하게 합니다. 따라서 Hadoop 사용자의 LDAP UID, GID를 설정하면 Kubernetes에서도 권한 문제 없이 데이터를 사용할 수 있습니다.

### [juicefs.users, juicefs.group 설정 방식 개선](https://github.com/juicedata/juicefs/issues/4723)

앞서 설명한 대로, Hadoop 클러스터에서 작업을 실행하면 데이터는 Hadoop 사용자의 LDAP UID, GID 소유가 됩니다. 하지만 Hadoop 클러스터 외부에서 Hadoop SDK를 사용하는 경우에는 임의의 UID, GID가 됩니다. 예를 들어 Docker 컨테이너에서 [HDFS 명령어](https://hadoop.apache.org/docs/r3.4.1/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html)로 데이터를 저장하면, 컨테이너 내부 계정의 UID, GID가 소유자가 됩니다.

이 문제를 해결하기 위해서는 `juicefs.users`와 `juicefs.groups` 설정으로 원하는 UID와 GID를 지정해야 하는데, 기존에는 `<사용자명>:<UID>`, `<그룹명>:<GID>` 형식의 파일을 작성하고 해당 파일 경로를 설정해야 해서 매우 번거로웠습니다. 이를 설정 값으로 직접 지정할 수 있도록 기능을 추가했습니다.

### [subdir 지원](https://github.com/juicedata/juicefs/issues/6096)

Kubernetes 기반 AI 플랫폼에서는 JuiceFS를 [Dynamic Provisioning](https://juicefs.com/docs/csi/guide/pv/#dynamic-provisioning) 방식으로 사용합니다. PersistentVolumeClaim(PVC)을 생성하면 JuiceFS 파일 시스템 내에 해당 볼륨을 위한 하위 디렉터리가 생성됩니다. 이때 Hadoop에서 해당 PVC를 공유하려면, 볼륨에 해당하는 디렉터리만 안전하게 공유해야 합니다.

그러나 Hadoop SDK에는 마운트 옵션 [--subdir](https://juicefs.com/docs/community/command_reference#mount-metadata-options)처럼 하위 경로에만 접근할 수 있게 하는 기능이 없습니다. 이를 해결하기 위해 Hadoop SDK에 [juicefs.subdir](https://juicefs.com/docs/community/hadoop_java_sdk#other-configurations) 설정을 추가했습니다. 이 설정을 사용하면 지정된 경로에만 접근 가능하게 설정할 수 있습니다.

### [hdfs 명령으로 쿼터 확인](https://github.com/juicedata/juicefs/issues/5937)

JuiceFS는 파일 시스템 전체 또는 특정 디렉터리 단위로 쿼터를 설정할 수 있습니다. Kubernetes에서 PVC의 spec.resources.requests.storage 값은 해당 디렉터리의 쿼터로 설정됩니다.

Hadoop과 PVC를 공유하는 경우에도 쿼터 확인이 필요합니다. 하지만 기존 HDFS 명령어 `hdfs dfs -count -q`로는 JuiceFS의 쿼터 정보를 확인할 수 없었습니다. 이를 개선해, 동일한 명령어로 JuiceFS에서도 쿼터를 확인할 수 있는 기능을 추가했습니다.

### [Prometheus remote\_write 프로토콜 지원](https://github.com/juicedata/juicefs/issues/6295)

JuiceFS Hadoop SDK를 사용하면서 지표를 Pushgateway와 Graphite로 전송할 수 있습니다. 하지만 Pushgateway는 주기적으로 지표를 정리해야 하는 문제가 있고, Graphite는 고유한 형태가 있어 활용하기 어려웠습니다.

다양한 시스템이 [Prometheus remote\_write 프로토콜](https://prometheus.io/docs/specs/prw/remote_write_spec)을 지원합니다. JuiceFS에도 이 프로토콜을 통해 지표를 전송하는 기능을 추가했습니다. [juicefs.push-remote-write, juicefs.push-remote-write-auth](https://juicefs.com/docs/community/hadoop_java_sdk#other-configurations) 설정으로 [VictoriaMetrics' vmagent](https://docs.victoriametrics.com/victoriametrics/vmagent/#victoriametrics-remote-write-protocol)나 [Prometheus](https://prometheus.io/docs/specs/prw/remote_write_spec/)를 지정할 수 있습니다. 이 기능으로 플랫폼 간 데이터뿐만 아니라 모니터링 시스템도 통합할 수 있게 되었습니다.

JuiceFS의 이점
-----------

### 병렬 처리, 캐싱으로 오브젝트 스토리지의 성능 극복

JuiceFS는 네트워크를 통해 원격 오브젝트 스토리지와 데이터 블럭을 주고받아야 하므로, 데이터 로컬리티의 이점이 있는 HDFS보다 좋은 성능을 보이긴 어렵습니다. 하지만 데이터를 블럭으로 나누어 병렬로 처리하고 한 번 읽은 데이터는 캐싱하는 방식으로 이를 극복합니다.

이를 확인하기 위해 HDFS, JuiceFS 각각에 대한 성능 테스트를 진행했습니다.

#### DFSIO

10개의 map task를 사용해 100GB 파일을 대상으로 HDFS와 JuiceFS에서 순차 데이터 쓰기(Write), 읽기(Read)의 초당 처리량을 측정했습니다. 값이 높을수록 성능이 좋습니다. 순차 Write/Read에 적합하도록 JuiceFS의 [block size](https://juicefs.com/docs/community/command_reference/#format-data-format-options)는 16MB로 설정했습니다.

![](https://d2.naver.com/content/images/2025/09/02bed8e4-96f7-4c4f-b799-e30b7325a5ba.png)

* 쓰기(Write): JuiceFS의 처리량이 HDFS의 1.7배입니다. 이는 데이터를 작은 블록으로 분할하여 병렬 업로드하기 때문입니다.
* 읽기(Read): JuiceFS의 처리량이 HDFS의 0.75배입니다. 그러나 데이터가 캐싱된 경우에는 HDFS과 유사한 성능이 예상됩니다.

#### TPC-DS

Spark SQL을 사용해 HDFS와 JuiceFS에 저장된 100GB 규모의 테이블을 대상으로 쿼리 응답 시간을 측정했습니다. 값이 낮을수록 성능이 좋습니다.

![](https://d2.naver.com/content/images/2025/09/f2c0a5a4-4013-4c2a-a200-7ec1317d22ee.png)

* JuiceFS의 응답 시간이 HDFS의 1.8배입니다. 이는 데이터 로컬리티의 차이로 인한 것입니다.
* 캐싱된 JuiceFS는 HDFS와 유사한 성능을 보입니다.

### HDFS와 완벽히 호환되어 기존 Hadoop 애플리케이션을 변경 없이 사용 가능

네이버에는 안정적으로 운영되는 공용 Hadoop 클러스터가 있으며, 다양한 서비스의 Hadoop 애플리케이션이 실행되고 있습니다.

만약 저장 비용을 절감하기 위해 자주 사용하지 않는 데이터만 오브젝트 스토리지에 보관하려 한다면 문제가 발생합니다. 앞에서 살펴본 것처럼, 오브젝트 스토리지는 파일 시스템이 아니므로 기존 Hadoop 애플리케이션의 성능과 동작을 보장하지 않습니다. 따라서 오브젝트 스토리지에 맞게 코드를 재작성하거나 데이터 처리 엔진에서 이를 지원하는지 검토해야 합니다. 또한 저장소 유형에 따라 Hadoop 애플리케이션을 별도로 실행·관리해야 하는 부담도 생깁니다.

반면 JuiceFS를 사용하면 기존 Hadoop 애플리케이션을 그대로 유지할 수 있습니다. 사용자는 단순히 입출력 경로를 `hdfs://` 또는 `jfs://`로 지정하는 것만으로 동일한 방식으로 애플리케이션을 실행할 수 있습니다.

![](https://d2.naver.com/content/images/2025/09/bfa13a7a-ecc5-426d-8f6d-b4957bc13fa1.png)

HDFS는 데이터 로컬리티를 기반으로 높은 성능을 보장하고, 오브젝트 스토리지는 저비용과 확장성이 장점입니다. 어느 한쪽을 완전히 대체하기는 어려우며 요구 사항에 따라 선택이 필요합니다. JuiceFS를 활용하면 기존 Hadoop 애플리케이션을 수정하지 않고도 HDFS와 오브젝트 스토리지를 함께 사용할 수 있습니다.

### 다양한 인터페이스 지원으로 플랫폼 간 통합 스토리지 역할 가능

네이버에는 서비스 개발/운영을 위한 다양한 플랫폼이 활용됩니다. 예를 들어 AI 서비스를 개발/운영해야 한다면, 데이터 처리 플랫폼에서 정제한 데이터를 사용해 AI 플랫폼에서 모델을 학습하고 컨테이너 플랫폼을 통해 서비스가 제공됩니다.

네이버에서 각 플랫폼은 독자적인 저장소를 제공하는데, 플랫폼 내부에서는 쉽게 사용할 수 있지만 다른 플랫폼의 저장소로 접근하기는 어렵습니다. 각 플랫폼에 고립되어 운영되는 저장소는 데이터 사일로 현상을 유발하고 중복 데이터로 비용 낭비가 발생하기 쉽습니다.

![](https://d2.naver.com/content/images/2025/09/6dfc993e-360a-4c2f-9660-668a78ae5793.png)

JuiceFS는 HDFS뿐만 아니라 POSIX, Kubernetes CSI 드라이버를 완벽하게 지원해 플랫폼 간 통합 스토리지로 적합합니다. JuiceFS를 활용해 다양한 플랫폼에서 원활하게 데이터를 사용함으로써 더욱 효율적으로 AI 서비스를 개발하고 데이터를 관리할 수 있습니다.

![](https://d2.naver.com/content/images/2025/09/c6131496-c395-4d52-8f72-cbccfb276e24.png)

마치며
---

지금까지 JuiceFS를 Hadoop 환경에서 활용하는 방법과 그 이점을 살펴보았습니다.

상황에 따라 HDFS나 오브젝트 스토리지를 직접 사용하는 편이 더 적합할 때도 있습니다. 예를 들어, 데이터 로컬리티를 확보해 빠른 처리가 필요한 경우에는 HDFS에 저장해야 합니다. 또한 데이터 접근 빈도가 낮거나 [Iceberg](https://iceberg.apache.org/)처럼 오브젝트 스토리지에 최적화된 포맷을 사용하는 경우에는 오브젝트 스토리지를 직접 사용하는 것이 간단합니다.

다만, 아래와 같은 상황에서는 JuiceFS가 더 나은 선택이 될 수 있습니다

* Kubernetes, Hadoop 간의 데이터를 공유해야 하는 경우
* 기존 Hadoop 애플리케이션을 변경하지 않고 HDFS와 병행해 사용하고자 하는 경우
* 동일한 데이터를 반복해 읽는 작업으로 캐싱 효과를 기대할 수 있는 경우
* S3 호환 스토리지가 애플리케이션이 사용하는 S3 API를 잘 지원하지 못하는 경우

JuiceFS는 [다양한 오브젝트 스토리지](https://juicefs.com/docs/community/reference/how_to_set_up_object_storage#supported-object-storage)와 [다양한 데이터베이스](https://juicefs.com/docs/community/databases_for_metadata)를 조합해 구성할 수 있습니다. 이 글에서는 네이버 사내 온프레미스 환경에서의 적용 사례를 다루었지만, AWS, Google Cloud 등 퍼블릭 클라우드 환경에서도 동일하게 활용할 수 있습니다. 비슷한 고민을 하고 있는 분들께 도움이 되었으면 합니다.

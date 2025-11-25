# DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기

**출처:** [Naver_D2](https://d2.naver.com/helloworld/8992409)

## 요약
네이버 사내 기술 교류 행사인 NAVER ENGINEERING DAY 2025(10월)에서 발표되었던 세션을 공개합니다.

#### 발표 내용

* 과거 데이터 파이프라인의 문제를 해결하고 사용자 중심의 on-demand data lineage pipeline 서비스인 Flow.er를 개발하고 발전시킨 내용에 대해 소개합니다
* DBT, Airflow를 활용하여 어떻게 데이터 계보 중심 파이프라인을 구축했는지 공유 합니다
* 데이터 파이프라인 플랫폼으로써 여러 데이터 조직으로 확장하기 위한 개발 컴포넌트들을 소개합니다

#### 발표 대상

* DBT, Airflow를 활용하여 품질 높은 Data Product 운영이 필요한 분들
* DBT 운영 도입을 고려중인 Data Engineer
* Airflow를 활용하고 있으나 과거 데이터 적재(Backfill) 및 파이프라인 복구 작업으로 인해 운영 비용이 높은 분들

#### 목차

* Episode 1: Introduction
  + 1-1: Data FLOW
  + 1-2: 과거 파이프라인의 문제
* Episode 2: Flow.er. On-demand data lineage pipeline
  + 2-1: Proof of Concept
  + 2-2: Flow.er
  + 2-3: Flow-er 구성 요소
  + 2-4: DBT의 역할
  + 2-5: Airflow의 역할
  + 2-6: 개인 인스턴스
  + 2-7: 모델 관리 페이지
  + 2-8: CI/CD 파이프라인
* Episode 3: Flow.er의 확장 – 추가 프로덕트 개발과 개선
  + 3-1: Playground
  + 3-2: Tower
  + 3-3: Manager DAG System 개선
  + 3-4: 정합성 향상을 위한 Partition Checker
* Episode 4: Flow.er의 미래 - 하고 싶은 것들
  + 4-1: MCP 서버 운영하기
  + 4-2: 또 다른 미래
* Episode 5: Conclusion
  + 5-1: 무엇이 바뀌었는가
  + 5-2: Conclusion

> ##### **◎ NAVER ENGINEERING DAY란?**
>
> NAVER에서는 사내 개발 경험과 기술 트렌드를 교류를 할 수 있는 프로그램이 많이 있습니다. 그중 매회 평균 70개 이상의 발표가 이루어지는 NAVER ENGINEERING DAY를 빼놓을 수 없는데요.   
> 2016년부터 시작된 ENGINEERING DAY는 실무에서의 기술 개발 경험과 새로운 기술과 플랫폼 도입 시 유용하게 활용될 수 있는 팁 등을 공유하며 서로 배우고 성장하는 네이버의 대표적인 사내 개발자 행사입니다.   
> 올해 진행된 NAVER ENGINEERING DAY의 일부 세션을 공개합니다.

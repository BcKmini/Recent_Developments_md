# VLOps:Event-driven MLOps & Omni-Evaluator

**출처:** [Naver_D2](https://d2.naver.com/helloworld/0931890)

## 요약
네이버 사내 기술 교류 행사인 NAVER ENGINEERING DAY 2025(10월)에서 발표되었던 세션을 공개합니다.

#### 발표 내용

* Event-driven MLOps는 학습·평가·배포를 Typed Message 단위로 정의하고, Event Sensor가 이를 감지해 자율적으로 실행하는 구조입니다.
* Kubeflow 같은 파이프라인처럼 전체 버전 관리가 필요하지 않으며, 메시지를 추가하는 것만으로 기능 확장이 가능합니다.
* 사용자는 내부 오케스트레이션을 몰라도 메시지 발행만으로 동일한 파이프라인을 구동할 수 있습니다.
* 이를 통해 평가·배포 시스템 간 느슨한 결합(Loose Coupling)과 클라우드 간 호환성을 확보했습니다.
* Omni-Evaluator와 Dashboard는 다양한 엔진·벤치마크를 통합하고, 실시간 모니터링과 사용자 주도 트리거 기능을 제공합니다.

#### 발표 대상

* MLOps 엔지니어, ML 리서처, 데이터 사이언티스트
* 클라우드 인프라/DevOps 개발자, 모델 배포 및 평가 담당자

#### 목차

1. MLOps가 필요한 이유
2. Event-driven MLOps의 등장
3. Event Sensor: 핵심 로직
4. EvalOps에서 Omni-Evaluator로
5. VLOps Dashboard: 사용자 경험의 허브
6. 결론 및 비전

> ##### **◎ NAVER ENGINEERING DAY란?**
>
> NAVER에서는 사내 개발 경험과 기술 트렌드를 교류를 할 수 있는 프로그램이 많이 있습니다. 그중 매회 평균 70개 이상의 발표가 이루어지는 NAVER ENGINEERING DAY를 빼놓을 수 없는데요.   
> 2016년부터 시작된 ENGINEERING DAY는 실무에서의 기술 개발 경험과 새로운 기술과 플랫폼 도입 시 유용하게 활용될 수 있는 팁 등을 공유하며 서로 배우고 성장하는 네이버의 대표적인 사내 개발자 행사입니다.   
> 올해 진행된 NAVER ENGINEERING DAY의 일부 세션을 공개합니다.

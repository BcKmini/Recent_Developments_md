# Iceberg Low-Latency Queries with Materialized Views  (feat. 실시간 거래 리포트)

**출처:** [Naver_D2](https://d2.naver.com/helloworld/9290684)

## 요약
네이버 사내 기술 교류 행사인 NAVER ENGINEERING DAY 2025(10월)에서 발표되었던 세션을 공개합니다.

#### 발표 내용

* 본 영상에서는 “실시간 거래 리포트를 어떻게 하면 사용자가 원하는 다양한 조건으로 빠르게 조회할 수 있을까?” 라는 질문에서 출발한 기술적 여정을 다룹니다.
* 단순히 데이터를 쌓고 조회하는 단계를 넘어, 거래 데이터의 최신성과 응답 속도, 그리고 확장성을 동시에 확보하기 위한 여러 시도를 공유합니다.

#### 발표 대상

* 데이터 플랫폼 엔지니어 / 데이터 아키텍트 – 대용량 실시간 데이터 처리 및 저지연 설계에 관심 있는 분
* 분석 플랫폼 운영자 / BI 개발자 – 다차원 필터 조회 속도 및 Freshness 향상 전략을 찾고 있는 분
* Spark, Iceberg, StarRocks 활용자 – 실제 조합 운영 사례를 통해 운영 팁을 얻고자 하는 분

#### 목차

1. 소개 (Introduction)
2. 문제 정의 (Problem Definition)
3. 도전 과제 (Challenges)
4. 리서치 여정 (Research Journey)
5. 아키텍처 개요 (Architecture Overview)
6. 구성 요소 (Components)
7. 결과 및 성능 (Results & Performance)

> ##### **◎ NAVER ENGINEERING DAY란?**
>
> NAVER에서는 사내 개발 경험과 기술 트렌드를 교류를 할 수 있는 프로그램이 많이 있습니다. 그중 매회 평균 70개 이상의 발표가 이루어지는 NAVER ENGINEERING DAY를 빼놓을 수 없는데요.   
> 2016년부터 시작된 ENGINEERING DAY는 실무에서의 기술 개발 경험과 새로운 기술과 플랫폼 도입 시 유용하게 활용될 수 있는 팁 등을 공유하며 서로 배우고 성장하는 네이버의 대표적인 사내 개발자 행사입니다.   
> 올해 진행된 NAVER ENGINEERING DAY의 일부 세션을 공개합니다.

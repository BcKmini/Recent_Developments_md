# Telegraf로 커스텀 지표 수집하기: Exporter 개발 경험 공유

**출처:** [Naver_D2](https://d2.naver.com/helloworld/8677833)

## 요약
네이버 사내 기술 교류 행사인 NAVER ENGINEERING DAY 2025(10월)에서 발표되었던 세션을 공개합니다.

#### 발표 내용

Telegraf를 활용한 Exporter 개발 경험 공유 및 가이드를 소개합니다.

#### 발표 대상

오픈소스 기반 Exporter와 Telegraf 적용을 고려중인 엔지니어

#### 목차

1. 오픈소스 기반 Exporter 도입 배경
2. 오픈소스 Benchmark Test
3. Telegraf 란?
4. Telegraf 적용 후 개선점
5. Telegraf 옵션

> ##### **◎ NAVER ENGINEERING DAY란?**
>
> NAVER에서는 사내 개발 경험과 기술 트렌드를 교류를 할 수 있는 프로그램이 많이 있습니다. 그중 매회 평균 70개 이상의 발표가 이루어지는 NAVER ENGINEERING DAY를 빼놓을 수 없는데요.   
> 2016년부터 시작된 ENGINEERING DAY는 실무에서의 기술 개발 경험과 새로운 기술과 플랫폼 도입 시 유용하게 활용될 수 있는 팁 등을 공유하며 서로 배우고 성장하는 네이버의 대표적인 사내 개발자 행사입니다.   
> 올해 진행된 NAVER ENGINEERING DAY의 일부 세션을 공개합니다.

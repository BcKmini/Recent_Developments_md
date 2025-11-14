# ARC로 확장가능한 GPU 서비스 개발 인프라 구축하기

**출처:** [Naver_D2](https://d2.naver.com/helloworld/0548704)

## 요약
네이버 사내 기술 교류 행사인 NAVER ENGINEERING DAY 2025(10월)에서 발표되었던 세션을 공개합니다.

#### 발표 내용

Actions Runner Controller 를 사용하여 Kubernetes 클러스터 위에서 GPU 서비스 개발을 위한 CICD 인프라를 확장 가능한 형태로 구축하는 방법을 소개합니다.

#### 발표 대상

* Github Actions 등 CICD 인프라를 구축하려는 엔지니어
* 자동화된 GPU Testing 파이프라인을 구축하려는 엔지니어
* Scalable CICD 를 구현하고자 하는 엔지니어

#### 목차

1. CICD, Scalability, 그리고 GPU
2. Actions Runner Controller (ARC)
3. CICD for GPU Service on ARC
4. SNOW의 Scalable CICD Infrastructure

> ##### **◎ NAVER ENGINEERING DAY란?**
>
> NAVER에서는 사내 개발 경험과 기술 트렌드를 교류를 할 수 있는 프로그램이 많이 있습니다. 그중 매회 평균 70개 이상의 발표가 이루어지는 NAVER ENGINEERING DAY를 빼놓을 수 없는데요.   
> 2016년부터 시작된 ENGINEERING DAY는 실무에서의 기술 개발 경험과 새로운 기술과 플랫폼 도입 시 유용하게 활용될 수 있는 팁 등을 공유하며 서로 배우고 성장하는 네이버의 대표적인 사내 개발자 행사입니다.   
> 올해 진행된 NAVER ENGINEERING DAY의 일부 세션을 공개합니다.

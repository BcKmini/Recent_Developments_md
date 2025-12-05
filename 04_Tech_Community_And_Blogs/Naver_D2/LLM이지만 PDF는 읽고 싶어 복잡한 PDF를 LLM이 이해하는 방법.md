# LLM이지만 PDF는 읽고 싶어: 복잡한 PDF를 LLM이 이해하는 방법

**출처:** [Naver_D2](https://d2.naver.com/helloworld/9036125)

## 요약
네이버 사내 기술 교류 행사인 NAVER ENGINEERING DAY 2025(10월)에서 발표되었던 세션을 공개합니다.

#### 발표 내용

LLM-friendly PDF parser PaLADIN을 소개합니다.

#### 발표 대상

* AI/LLM을 적극적으로 활용하고 싶으신 분
* 문서 처리에 관심이 있으신 분
* 웹검색에 관심이 있으신 분

#### 목차

1. PDF가 왜 중요한가요?   
   * LLM-friendly PDF Parser
2. 기술 탐색 및 PoC (with NVIDIA)   
   * 관련 기술 탐색
   * PoC with NVIDIA
3. PaLADIN: 표와 차트, 숫자를 정확히 이해하고 표현하는 LLM-friendly PDF Parser   
   * 아키텍쳐 설계 - nv-ingest
   * 아키텍쳐 설계 - PaLADIN
   * Model 소개 - Element-Detector: Doclayout-Yolo
   * Model 소개 - Table-Extractor: nemoretriever-table-structure-v1
   * Model 소개 - Chart-Extractor: google/gemma3-27b-it
   * Model 소개 - Papago OCR
   * PDF parsing 예제
   * 속도 개선 및 최적화
4. 성능 평가   
   * Parsing 평가셋 구축
   * Parsing 능력 평가
   * 속도 측정
   * 성능 비교
5. 서비스 적용 사례: AIB 증권사 리포트   
   * 서비스 적용 예시
   * Summary 모델 선정: LLM as a judge
   * Summary 예시
6. Future Works   
   * Table Cell 좌표 오류 개선
   * 차트 정확도 개선

> ##### **◎ NAVER ENGINEERING DAY란?**
>
> NAVER에서는 사내 개발 경험과 기술 트렌드를 교류를 할 수 있는 프로그램이 많이 있습니다. 그중 매회 평균 70개 이상의 발표가 이루어지는 NAVER ENGINEERING DAY를 빼놓을 수 없는데요.   
> 2016년부터 시작된 ENGINEERING DAY는 실무에서의 기술 개발 경험과 새로운 기술과 플랫폼 도입 시 유용하게 활용될 수 있는 팁 등을 공유하며 서로 배우고 성장하는 네이버의 대표적인 사내 개발자 행사입니다.   
> 올해 진행된 NAVER ENGINEERING DAY의 일부 세션을 공개합니다.

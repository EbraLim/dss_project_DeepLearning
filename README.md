[Deep Learning Project]\
Real-time Object Detection in bird's eye view  
==
## 0. 요약
```
1) 프로젝트 시행 목적
    - 지상 높이에서는 수행하기 어려운 광범위한 영역의 object detection을 항공뷰 데이터를 통해 수행하고자 함
2) 결과
    - xx, xx, xx 구현 성공
```

## 1. 소개
### 1) 주제
* 항공뷰에서의 multi-object detection and tracking
### 2) 기획의도
* 항공뷰에서는 지상 높이에서 파악하기 힘든 object features를 파악할 수 있을 것이라고 예상
* 성능이 뒷받침된다면, 다른 각도의 시선과 넓은 영역에 걸친 detection을 통해 지상에서와는 또다른 부가가치 창출이 가능할 것이라고 생각하였음
### 3) 기대효과 및 예상 적용 분야 예시
* 특정 구역의 특징 파악  
  (ex. 시간대별 유동인구 수, 특정 object의 분포 현황)
* 주요 대상 감시  
  (ex. 군사적 목적)
* 기타 광범위한 영역에 걸친 특징을 파악해야 하는 분야  
  (ex. 건설업)
### 4) 사용한 라이브러리, 알고리즘 및 Tool
* 라이브러리: tensorflow-gpu 2.3.0
* 알고리즘: Yolo v3, v4, SORT
* Tool: Google Colaboratory, LabelImg, Iriun
----

## 2. 진행 Step
- step 설정 이유: computing power 및 시간 등의 한계 존재 → 목표를 세분화하여 incremental improvement 추구
### 1) Step 1
* 보행자 탐지
### 2) Step 2
* 실시간으로 특정 영역 내에 있는 보행자 수 파악
* 특정 시간 동안 특정 영역을 통과했던 보행자 수 파악
### 3) Step 3
* 촬영지점으로부터 object 사이의 거리 추정
### 4) Step 4
* object class를 점차 확대하며 Step 1~3 반복
### 5) Step 5
* 탐지한 object를 추적하며 이동 경로 생성
----

## 3. 진행 프로세스
* '데이터 수집' → '데이터 라벨링' → 'train' → 'test'
* 위 과정 성공 시 다음 step에 대해 동일 과정 수행  
  (추후 도식으로 표현 예정)
----

## 4. 프로세스별 상세설명
### 1) 데이터 수집
* 약 3시간 동안 2천 장의 이미지 수집
* 휴대폰 카메라를 웹캠으로 활용했으며, 카메라 위치 고정 후 정해진 주기마다 자동으로 사진 촬영 후 저장하도록 설정
* [Iriun](https://iriun.com/)을 사용하여 휴대폰 카메라를 웹캠으로 설정

### 2) 데이터 라벨링
* Google Colaboratory의 제한 사용시간 내에 train을 수행하기 위해 데이터셋 크기를 제한
* 랜덤하게 500장의 이미지를 선택하여 라벨링 수행하였으며, 도구는 LabelImg 사용

### 3) train
* Google Colaboratory에서 yolo v3를 사용하여 weight 파일 도출

### 4) test
* 테스트 비디오에 모델 적용, 문제 없이 구현되는지 확인

### 5) 다음 Step에 대해 2~4번 반복 수행
----
## 5. 결과
* Step 별로 결과물 이미지 or 움짤 or 유튜브링크 첨부 예정
----

## 6. 추후 보완점
* 작성예정
----

## 7. 멤버 & 수행업무
#### 1) [임현수](https://github.com/EbraLim/)
* 작성예정
#### 2) [정민주](https://github.com/meiren13/)
* 작성예정  
----  
참고: (유튜버 깃헙 주소들 남기기)
본 프로젝트는 패스트캠퍼스 데이터사이언스 취업스쿨 16th 딥러닝 프로젝트로 진행되었습니다.

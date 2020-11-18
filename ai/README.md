#### 파일 및 디렉토리 구성도

```ANSI
└─ai
  │  README.md
  │  anonymize_face_pixelate.py
  │  anonymize_face_simple.py
  │  blur.py
  │  detect.py
  │
  ├─cascade
  │  haarcascade_eye.xml
  │  haarcascade_eye_tree_eyeglasses.xml
  │  ....
  ├─result
  │  tongchun-facedetect.png
  ├─imgs
  │  00001.png
  │  00011.png
  │   ....
  ├─3DDFA
  │ └─ .....
  ├─face_generator
  │ └─ .....
  ├─face_landmark
  │ └─ .....
  └─face-swap_81
    └─ .....
```



#### 폴더별 설명

- 3DDFA
  - 얼굴 인식 및 Landmark 도출
- face_generator
  - 가상 얼굴 학습 및 생성
- face_landmark
  - dlib 이용한 face landmark_68
- face-swap_81
  - dlib 이용한 얼굴 교환
    - landmark_81 사용




#### AI 진행중 이슈
##### Face Recognition & Face Classification(얼굴 인식 및 분류)

1. **vgg_face**와 **Keras** 이용한 pre_trained 된 모델을 이용하여 closed set classification로 구성
- 학습된 데이터에 대해서만 분류가 되어 학습시키지 않은 얼굴 모델의 경우 unknown으로 분류가 되지 않음
   - closed set이 아닌 open set classification 방식으로 학습 시키지 않는 모델 식별 필요하여 **파기**
2. **ArcFace**를 이용한 모델 학습으로 학습 되지 않은 부분까지 인지할 수 있음
   - 학습 시켜야 할 모델의 크기가 너무 크고(100GB) 중요도 측면에서 고성능의 인식 및 분류를 원치 않아 **파기**
3. **OpenCV Face Recognition**에 있는 얼굴 유사도 측정
   - 이미 잘 알려져있는 방법으로 신뢰도는 낮지만 빨리 구현할 수 있다고 판단하여 **선택**



##### Face Landmark (얼굴 특성 좌표점)

1. **OpenCV**를 이용하여 사용할 수 있는 모델인 mmod_human_face_detector.dat와 shape_predictor_68_face_landmarks.dat 를 이용하여 얼굴 인식 및 Landmark생성
   - 옆모습 및 각도에 따라 인식률이 현저하게 낮음
   - 다양한 각도에 대해서도 인식을 하고 Landmark를 만들어 줄 수 있는 모델의 필요성이 있어 **파기**
2. **3DDFA**라는 Open Source로 기존 학습된 모델을 이용하여 얼굴 인식 및 얼굴 윤곽선의 예측 좌표를 표시
   - Face Swap을 하는데에 있어 보이지 않는 부분의 윤곽선도 나타내어 추가적인 알고리즘을 대입하여 윤곽선을 거르는 작업이 필요하여 **파기**
3. **MTCNN**및 **PFLD**를 이용한 얼굴 인식 및 얼굴 Landmark 검출
   - 2번의 3DDFA와 달리 예측 좌표가 아닌 보이는 Landmark만 표시하여 경계를 구분할 수 있음
   - 인식이 되지 않는 부분이 있지만 편의상 **선택**



##### Face Detection (얼굴 감지)

1. **Wider_Face**를 이용하여 얼굴을 감지
   - Pre_Trained된 모델을 이용하여 많거나 작은 얼굴까지 모두 사각형 형태로 감지할 수 있음
   - Face Landmark의 **3DDFA**와 합쳐서 사용할 수 있었지만 빨리 구현이 가능한  **MTCNN**과 **PFLD**를 이용하기로 하여 **파기**
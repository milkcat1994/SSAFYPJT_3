### 출처

https://github.com/gsurma/face_generator



#### Google Cloud Platform 작업시 의존성

- ubuntu 18.04
- python3
- pip3
- nvidia-455 driver (Tesla V100 이용)
- grpcio
- matplotlib
- tensorflow 2.3.1
- CUDA (10.1)
- CUDA (10.2)
- CUDA (11.1)



#### 사전 작업

- 100k 자료 다운로드
  - https://www.kaggle.com/greg115/celebrities-100k
- face_generator 내의 100k 폴더에 파일 배치
- .bashrc에 아래 내용 추가
  - export PATH=/usr/local/cuda-10.1/bin:$PATH
  - export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64:$LD_LIBRARY_PATH



#### 파일 및 디렉토리 구성도

```ANSI
└─face_generator
  │  face_generator.py
  │  face_generator_train.py
  │  tfTest.py
  ├─input
  |  100k.txt
  ├─100k
  |  0000001.jpg
  |  0000002.jpg
  |  0000003.jpg
  |  ....
  ├─final_models
  | |  model_99.ckpt.data-00000-of-00001
  | |  model_99.ckpt.index
  | |  model_99.ckpt.meta
  | |  ....
  | └─images
  |   |  samples_99_0.png
  |   |  samples_99_1.png
  |   |  samples_99_2.png
  |   └  ....
  └─models
    |  checkpoint
    |  model_24.ckpt.data-00000-of-00001
    |  model_24.ckpt.index
    |  model_24.ckpt.meta
    └  ....
```



#### 학습 실행

- nohup python3 -u face_generator_train.py &
  - ./models 에 model.ckpt 파일 저장

#### 학습 모니터링

- tail -f nohup.out

#### 학습 모델로 이미지 생성
- python3 face_generator.py
  - ./final_models/images 에 결과물 저장




#### 학습 관련 수정 사항 있을 시

- 생성 checkout 변경 요망시 face_generator_train.py 내의 EPOCH 및 EPOCHS 변경
- 기존 참고 Model 없을 경우 train()내의 checkpoint_path=None 으로 변경



#### 모델 예제 생성 관련 수정 사항 있을 시

- 참고 checkout 변경 요망시 face_generator.py 내의 EPOCH 변경
- 샘플 갯수 변경 요망시 face_generator.py 내의 SAMPLES_TO_SHOW 변경



#### 참고 자료

GAN : https://honeycomb-makers.tistory.com/18

DCGAN : https://research.sualab.com/introduction/practice/2019/05/08/generative-adversarial-network.html
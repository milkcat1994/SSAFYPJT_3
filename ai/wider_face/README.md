### 출처

https://www.kaggle.com/mksaad/wider-face-a-face-detection-benchmark



#### 의존성

- windows10
- python3
- matplotlib
- chainer
- chainercv
- dlib



#### 사전 작업

- dlib 설치
  - https://sulastri.tistory.com/3
- chainer, chainercv 설치
  - pip install chainer chainercv matplotlib



#### 파일 및 디렉토리 구성도

```ANSI
└─wider_face
  │  README.md
  │  demo.py
  │  download_model.py
  │  test_detection.py
  │  ....
  │
  ├─trained_model
  │ │ snapshot_model.npz
  │ └─snapshot_model_20180404.npz
  ├─wider_face_split
  │ └─wider_face_split
  │   │ ....
  │   └─readme.txt
  └─images
     0_Parade_marchingband_1_20.jpg
     8.jpg
```



#### 실행

- python demo.py images/8.jpg



#### 참고 자료


<img src="https://user-images.githubusercontent.com/18321002/99801227-05023500-2b79-11eb-93c6-7af736e1ff11.png" width="200" height="200">

## FACE OFF
![Generic badge](https://img.shields.io/badge/version-1.0.0-blue.svg) ![Generic badge](https://img.shields.io/badge/React-17.0.1-brightgreen.svg) ![Generic badge](https://img.shields.io/badge/TypeScript-4.0.3-brightgreen.svg) ![Generic badge](https://img.shields.io/badge/Sass-4.11.1-brightgreen.svg) ![Generic badge](https://img.shields.io/badge/Django-3.1.2-green.svg) ![Generic badge](https://img.shields.io/badge/TensorFlow-1.14.0-brightgreen.svg) ![Generic badge](https://img.shields.io/badge/Opencv_Python-4.4.0.46-brightgreen.svg) ![Generic badge](https://img.shields.io/badge/MariaDB-10.5.6-blue.svg) ![Generic badge](https://img.shields.io/badge/server-AWS_EC2-9cf.svg) ![Generic badge](https://img.shields.io/badge/License-MIT-yellow.svg)



## 📖 프로젝트 소개

`FACE OFF`는 손쉬운 사진 모자이크 웹 어플리케이션입니다.

### 📷 [프로젝트 영상](https://www.youtube.com/watch?v=97YLNTS6HaQ&feature=youtu.be)



## :fire: Gantt 
![mermaid-diagram-20201120215237](https://user-images.githubusercontent.com/18321002/99802267-c0779900-2b7a-11eb-97df-8fd53db21c6a.png)


### :grey_question: 기획 배경 및 의도

- 블로그, 인스타그램 등 이미지 중심 SNS는 일상의 일부로 자리잡았고, 때와 장소를 가리지 않은 사진들이 SNS에 공유되고 있습니다. 이런 사회적 변화와 함께 초상권 침해 피해도 증가하고 있습니다. 방송통신심의위원회의 발표에 따르면 초상권 침해 피해 신고사례는
  2014년 5,017건에서 2018년 1만 건 이상으로 크게 증가하였습니다. 

- 사진 수정 어플리케이션 등을 통해 모자이크 처리를 할 수 있지만, 직접 영역을 선택해야하고 모자이크를 하면 사진이 부자연스러워지는 문제가 있었습니다. 또한 앱스토어에서 어플리케이션을 다운로드 받아야하는 불편이 존재했습니다.

- 이에 우리 팀은 보다 손쉽게 사진에 모자이크를 적용할 수 있는 웹 어플리케이션을 개발하여 이러한 불편을 해소하고자 하였습니다.



### :mag: 핵심 기능

- **자동 얼굴인식**

  - AI 기반 자동 얼굴인식 기술을 이용하여 빠르게 수정하지 않을 인물을 선택할 수 있습니다.

  

- **다양한 모자이크 옵션**

  - 픽셀, 흐리게, 가상얼굴, 스티커 등 다양한 모자이크 옵션을 제공합니다.

  - 가상얼굴 옵션은 대상의 얼굴을 가리는 대신, AI가 생성한 가상얼굴로 대체함으로써 보다 자연스러운 결과물을 얻을 수 있습니다.

    

- **소셜 로그인 및 친구 얼굴 등록**

  - 카카오, 구글 아이디 등을 통해 손쉽게 회원가입하고 로그인할 수 있습니다.
  - 자동 얼굴인식 단계에서 등록된 친구 얼굴을 찾아 이름을 표시해주고, 모자이크 대상에서 자동으로 제외합니다.



- **다운로드 및 공유**
  - 손쉽게 사진을 다운로드하고, 친구들에게 공유할 수 있습니다.




## :family: 드래곤볼 팀 소개

- `드래곤볼` 이란 7개의 구슬을 모아 소원을 이루어주는 아이템입니다.

   `드래곤볼`이라는 팀 이름은, 드래곤볼처럼 모여서 사람들의 불편을 해결해 줄 수 있는 서비스를 개발하겠다는 의지를 담고 있습니다.



### 팀원 구성

	👦 문명기 : 팀장 / Backend 
	
	🧑 정세린 : Backend Tech Leader
	
	🧔 이원준 : Frontend Tech Leader
	
	🧑 박태웅 : Frontend
	
	🧒 오정엽 : AI Tech Leader
	
	🧒 양지용 : AI



## 💻 기술 스택

### Frontend

- React.js  17.0.1
  - 네이티브 앱과 같이 뛰어난 사용성을 제공하는 SPA를 구현하고자 React.js를 채택하였습니다.
- TypeScript 4.0.3
  - 개발의 생산성과 유지보수의 용이성을 위해 타입스크립트를 도입하고자 하였습니다.
- Sass (Scss) 4.11.1
  - 스타일링 측면에서의 개발 생산성을 높이기 위해 Sass를 채택하였습니다.


### Backend

- Django 3.1.2
  - TensorFlow와의 결합을 용이하게 하기 위하여 프레임워크로 Django를 채택하였습니다.
- TensorFlow 1.14.0
- MariaDB 10.5.6



### AI

##### Face Recognition & Face Classification(얼굴 인식 및 분류)

1. **vgg_face**와 **Keras** 이용한 pre_trained 된 모델을 이용하여 closed set classification로 구성 되어있음
   - 학습된 데이터에 대해서만 분류가 되어 학습시키지 않은 얼굴 모델의 경우 unknown으로 분류가 되지 않음
     - closed set이 아닌 open set classification 방식으로 학습 시키지 않는 모델 식별 필요하여 `파기`
2. **ArcFace**를 이용한 모델 학습으로 학습 되지 않은 부분까지 인지할 수 있음
   - 학습 시켜야 할 모델의 크기가 너무 크고(100GB) 새로운 얼굴이 등록될 때마다 학습이 이루어 져야 하며, 이용자 별로 모델을 따로 가지고 있어야 하여 `파기`
3. **OpenCV Face Recognition**에 있는 얼굴 유사도 측정
   - 이미 잘 알려져있는 방법으로 가볍고 빠르다고 판단하여 `선택`



##### Face Landmark (얼굴 특성 좌표점)

1. **OpenCV**를 이용하여 사용할 수 있는 모델인 mmod_human_face_detector.dat와 shape_predictor_68_face_landmarks.dat 를 이용하여 얼굴 인식 및 Landmark생성
   - 옆모습 및 각도에 따라 인식률이 현저하게 낮음
   - 다양한 각도에 대해서도 인식을 하고 Landmark를 만들어 줄 수 있는 모델의 필요성이 있어 `파기`
2. **3DDFA**라는 Open Source로 기존 학습된 모델을 이용하여 얼굴 인식 및 얼굴 윤곽선의 예측 좌표를 표시
   - Face Swap을 하는데에 있어 보이지 않는 부분의 윤곽선도 나타내어 추가적인 알고리즘을 대입하여 윤곽선을 거르는 작업이 필요하여 `파기`
3. **MTCNN**및 **PFLD**를 이용한 얼굴 인식 및 얼굴 Landmark 검출
   - 2번의 3DDFA와 달리 예측 좌표가 아닌 보이는 Landmark만 표시하여 경계를 구분할 수 있어 `선택`



##### Face Detection (얼굴 감지)

1. **Wider_Face**를 이용하여 얼굴을 감지
   - Pre_Trained된 모델을 이용하여 많거나 작은 얼굴까지 모두 사각형 형태로 감지할 수 있음
   - Face Landmark의 **3DDFA**와 합쳐서 사용할 수 있었지만  **MTCNN**과 **PFLD**를 이용하기로 하여 `파기`



### Dev-Ops

- AWS EC2 (Ubuntu 18.0.4)
- Jenkins 2.249.2
  - CI/CD 자동화를 통해 개발 생산성을 높이기 위하여 Jenkins를 도입하였습니다.
- Docker 19.03.13
  - 배포에서의 용이성을 위하여 Docker를 도입하였습니다.


## :hammer: git branch 정책 
 master -> develop -> feat/기능이름

- master : 제품으로 출시하는 branch
- develop : 다음 출시버전을 개발하는 branch
- feat/ : 기능을 개발하는 branch 


## :page_facing_up: Coding Convention

### Back-end 

#### Base

- 4 space(1 tab) 들여쓰기를 사용한다.
- 함수명 위에 한줄 주석으로 기능을 정의한다.
- swagger 를 이용해 parameter 및 return 값을 명시한다. 

#### Naming Conventions

- 클래스 명은 카멜케이스(CamelCase)로 작성한다.
- 함수명은 소문자로 구성하되 필요하면 밑줄(find_user)로 나눈다.
- DB의 테이블, 컬럼명은 대문자로 정의한다. 

### Front-end 

#### Base

- 세미콜론을 사용한다.
- 2 space 들여쓰기를 사용한다.

#### React

- 기본적으로 Airbnb React Style Guide를 준수한다.

- 컴포넌트 이름은 PascalCase로 작성한다.

- 컴포넌트 이름은 큰 범주로부터 세부 기능의 순서로 한다.

  - HomeButtonLogin.tsx
  - page / type / function

#### TypeScript

- class는 PascalCase로 작성한다.

- interface 이름은 PascalCase로 작성한다. interface임을 나타내기 위해 I를 이지 않는다.

  - TypeScript 소스코드에서 중요 interface를 네이밍할 때 I 를 붙이지 않음

  ``` typescript
  // bad
  interface IFoo {
      name: string
  };
  
  // good
  interface Foo {
      name: String
  };

  ```

import React from 'react';

function WelcomeItem2() {
  const srcList = [
    "http://k3a207.p.ssafy.io/capture/00시작하기.jpg",
    "http://k3a207.p.ssafy.io/capture/01옵션선택.jpg",
    "http://k3a207.p.ssafy.io/capture/02대상선택.jpg",
    "http://k3a207.p.ssafy.io/capture/03결과이미지.jpg",
    "http://k3a207.p.ssafy.io/capture/04로그인시얼굴등록.jpg",
    "http://k3a207.p.ssafy.io/capture/06모자이크대상제외.jpg",
    "http://k3a207.p.ssafy.io/capture/07아는얼굴수정.jpg",
    "http://k3a207.p.ssafy.io/capture/08커스텀스티커.jpg",
  ]
  
  const textList = [
    "① 시작하기 또는 사진 추가 버튼을 눌러 사진을 업로드합니다.",      
    "② 적용할 옵션(픽셀, 흐리게, 가상얼굴, 스티커)을 선택합니다.",
    "③ 모자이크 대상을 선택합니다.",
    "④ 결과 사진은 기기에 저장이 가능하며, 소셜 로그인을 통해 더 다양한 기능을 만나보실수 있습니다.",
    "⑤ 로그인을 하면 사진의 등장인물을 아는 얼굴로 등록할 수 있습니다.",
    "⑤ 다음에 사진을 업로드하면 아는얼굴을 인식하여 모자이크 대상에서 자동으로 제외시킵니다.",
    "⑥ 아는얼굴은 설정에서 친구관리 기능을 통해 얼굴을 추가하거나 이름을 수정할 수 있습니다.",
    "⑦ 로그인을 하면 내 스티커 기능을 통해 사용할 스티커를 업로드 할 수 있습니다.",
  ]

  const ExampleImg = ({ idx }) => (
    <div className="example-img-wrap1">
      <img className="example-img1" src={srcList[idx]} alt=""/>
    </div>
  );

  const Items = textList.map((text, idx) => (
    <div key={idx} ><p className="welcome-text">{ text }</p><ExampleImg idx={idx} /></div>
  ));

  const Source = () => (
    <div className="source">
      <a href="http://www.topstarnews.net/news/articleView.html?idxno=231190 ">
        이미지 출처 : <br/>
        에이프릴(April) '앳스타일(@star1)' 화보 / '앳스타일(@star1)
      </a>
    </div>
  );

  return (
    <div className="welcome-item">
      { Items }
      <Source />
    </div>
  );
}

export default WelcomeItem2;
import React from 'react';

function WelcomeItem1() {
  const featureNames = [
    '1. 얼굴 자동 인식',
    '2. 다양한 모자이크 옵션',
    '3. 다운로드 및 친구등록',
    '4. 친구 얼굴 자동인식',
  ];

  const FeatureTitle = ({ idx }) => (
    <h3 className="feature-title">{ featureNames[idx] }</h3>
  );

  return (
    <>
      <div className="welcome-item">
        <ul>
          <li>FACE/OFF는 인공지능 기술을 이용해 사진에 쉽게 모자이크를 입힐 수 있는 웹 어플리케이션입니다.</li>
          <li>FACE/OFF를 이용해 사진에 원하는 얼굴만 남기세요.</li>
        </ul>

        <h2 className="mt-50">주요 기능</h2>
        <div className="divider"></div>


        {/* 얼굴 자동 인식 */}

        <FeatureTitle idx={0} />
        <ul>
          <li>사진상의 얼굴을 인공지능이 인식하여 자동으로 영역을 선택해줍니다. </li>
        </ul>
        <div className="feature">
          <div className="example-img-wrap1">
            <div>
              <img className="example-img1" 
                src="http://k3a207.p.ssafy.io/welcome/f1-1.jpg" alt="" />
              <div>원본 화면</div>
            </div>

            <div>
              <img className="example-img1"
                src="http://k3a207.p.ssafy.io/welcome/f1-2.jpg" alt="" />
              <div>자동 인식 화면</div>
            </div>
          </div>
        </div>

        <FeatureTitle idx={1} />
        <ul>
          <li>기본적인 픽셀, 블러 효과 및 스티커와 가상얼굴 옵션을 제공합니다.</li>
          <li>가상얼굴은 인공지능에 의해 생성된 얼굴로 기존의 얼굴을 대체합니다.</li>
        </ul>

        <div className="feature">
          <div className="example-face-grid">
            {/* 픽셀 */}
            <div>
              <img className="example-face" 
                src="http://k3a207.p.ssafy.io/welcome/f2-1.jpg" alt="" />
              <div>원본</div>
            </div>

            {/* 블러 */}
            <div>
              <img  className="example-face" 
              src="http://k3a207.p.ssafy.io/welcome/f2-2.jpg" alt="" />
              <div>블러</div>
            </div>
            {/* 픽셀 */}
            <div>
              <img className="example-face" 
              src="http://k3a207.p.ssafy.io/welcome/f2-3.jpg" alt="" />
              <div>픽셀</div>
            </div>
            {/* 스티커 */}
            <div>
              <img className="example-face" 
              src="http://k3a207.p.ssafy.io/welcome/f2-4.jpg" alt="" />
              <div>스티커</div>
            </div>
            {/* 가상얼굴 */}
            <div>
              <img className="example-face" 
              src="http://k3a207.p.ssafy.io/welcome/f2-5.jpg" alt="" />
              <div>가상얼굴</div>
            </div>
          </div>
        </div>

        {/* 원본 */}
        <FeatureTitle idx={2} />
        <ul>
          <li>결과사진을 쉽게 기기에 저장할 수 있습니다.</li>
          <li>로그인을 하면, 인식된 얼굴을 아는 얼굴에 등록할 수 있습니다.</li>
        </ul>

          <div className="feature">
            <div className="example-img-wrap1">
              <div>
                  <img className="example-img1"
                  src="http://k3a207.p.ssafy.io/welcome/f3-1.jpg" alt="" />
                  <div>다운로드 화면</div>
              </div>
              <div>
                  <img className="example-img1"
                  src="http://k3a207.p.ssafy.io/welcome/f3-2.jpg" alt="" />
                  <div>얼굴 등록 화면</div>
              </div>
            </div>
          </div>

        <FeatureTitle idx={3} />
        <ul>
          <li>아는 얼굴에 등록되면, 인공지능이 이를 인식하여 자동으로 모자이크 대상에서 제외시킵니다.</li>
        </ul>

        <div className="feature">
          <div>
            <img className="example-img1"
            src="http://k3a207.p.ssafy.io/welcome/f4.jpg" alt="" />
            <div>등록된 친구 얼굴 자동 인식</div>
          </div>
        </div>

        <div className="source">
          <a href="http://www.topstarnews.net/news/articleView.html?idxno=231190 ">
          이미지 출처 : <br/>
          에이프릴(April) '앳스타일(@star1)' 화보 / '앳스타일(@star1)
          </a>
        </div>
        {/* 이미지 출처 : http://www.topstarnews.net/news/articleView.html?idxno=231190 
        에이프릴(April) '앳스타일(@star1)' 화보 / '앳스타일(@star1)'
        */}
      </div>
    </>
  );
}

export default WelcomeItem1;
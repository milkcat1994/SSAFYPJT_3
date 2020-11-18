import React, { useEffect } from 'react';

const KakaoShareButton = () => {

  useEffect(() => {
    createKakaoButton()
  }, [])
  
  const createKakaoButton = () => {
    // kakao sdk script이 정상적으로 불러와졌으면 window.Kakao로 접근이 가능합니다
    if (window['Kakao']) {
      const Kakao = window['Kakao']
      // 중복 initialization 방지
      if (!Kakao.isInitialized()) {
        // 두번째 step 에서 가져온 javascript key 를 이용하여 initialize
        Kakao.init(process.env.REACT_APP_KAKAO_KEY)
      }
      Kakao.Link.createDefaultButton({
        // Render 부분 id=kakao-link-btn 을 찾아 그부분에 렌더링을 합니다
        container: '#kakao-link-btn',
        objectType: 'feed',
        content: {
          title: '타이틀',
          description: '#리액트 #카카오',
          imageUrl: 'https://i.pinimg.com/originals/39/ea/2f/39ea2ff7f4fdfc6f19f31dca0076ea70.png', // i.e. process.env.FETCH_URL + '/logo.png'
          link: {
            mobileWebUrl: 'http://localhost:3000/logo512.png',
            webUrl: 'http://localhost:3000/logo512.png',
          },
        },
        buttons: [
          {
            title: '수정하러 가기',
            link: {
              mobileWebUrl: 'http://localhost:3000',
              webUrl: 'http://localhost:3000',
            },
          },
        ],
      })
    }
  }
  return (
    <div className="kakao-share-button">
      {/* Kakao share button */}
      <div id="kakao-link-btn">
        공유 하기
      </div>
    </div>
  )
}
export default KakaoShareButton
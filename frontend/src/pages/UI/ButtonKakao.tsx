import React from "react";

const Kakao = window['Kakao'];

try {
  Kakao.init('416a3da039b588e8fcd7e5de4a07e25f');
} catch (error) {}

export function ButtonLoginKakao({ onSocialLoginSuccess }) {
  const src = 'http://k3a207.p.ssafy.io/icon/kakao.png';

  const kakaoLoginClickHandler = () => {
    Kakao.Auth.login({
      scope: 'account_email',
      success() {
        Kakao.API.request({
          url: "/v2/user/me",
          success(response) {
            localStorage.clear();
            onSocialLoginSuccess(response.kakao_account.email,'kakao');
          },
          fail(error) {
          },
        });
      },
    });
  };
  return (
    <div className="base-btn-icon" onClick={kakaoLoginClickHandler}>
      <img src={src} alt=""/>
    </div>
  );
}

export function ButtonLogoutKakao({ onLogout }) {
  const src = 'http://k3a207.p.ssafy.io/icon/logout3.png';

  const logoutHandler = () => {
    Kakao.Auth.logout(() => {});
    onLogout();
  }

  return (
    <div
      className="base-btn-icon"
      onClick={logoutHandler}>
      <img className="menu-logo-img" src={src} alt=""/>
    </div>
  );
}
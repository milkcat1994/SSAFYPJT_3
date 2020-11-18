import React from 'react';
import { GoogleLogin, GoogleLogout } from 'react-google-login';

const clientId = '237475771915-u5sqqo0e7lhvtf296fckun9g2cdrpia7.apps.googleusercontent.com'

export function ButtonLoginGoogle({ onSocialLoginSuccess }) {
  const src = 'http://k3a207.p.ssafy.io/icon/google.png';
  const onSuccess = (res) => {
    onSocialLoginSuccess(res.profileObj.email, 'google')
  };
  const onFailure = (res) => {};

  return (
    <GoogleLogin
      clientId={clientId}
      render={renderProps => (
        <div title="구글 로그인" className="base-btn-icon" onClick={renderProps.onClick}>
          <img className="menu-logo-img" src={src} alt=""/>
        </div>
      )}
      onSuccess={onSuccess}
      onFailure={onFailure}
      cookiePolicy={'single_host_origin'}
      // isSignedIn={true}
    />
  )
}

export function ButtonLogoutGoogle({ onLogout }) {
  const src = 'http://k3a207.p.ssafy.io/icon/logout3.png';

  return (
      <GoogleLogout
        clientId={clientId}
        render={renderProps => (
          <div
            onClick={renderProps.onClick} 
            className="base-btn-icon">
            <img className="menu-logo-img" src={src} alt=""/>
          </div>
        )}
        buttonText="Logout"
        onLogoutSuccess={() => onLogout()} />
  )
}

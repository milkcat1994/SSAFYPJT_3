import React, { useEffect, useState } from 'react';
import { useHistory, useLocation } from 'react-router-dom';
import './Header.scss';

function Header() {
  const history = useHistory();
  const location = useLocation();
  const src = 'http://k3a207.p.ssafy.io/icon/favicon.png';
  const [path, setPath] = useState('');

  useEffect(() => {
    switch (location.pathname) {
      case '/edit':
        setPath('사진 수정하기');
        break;
      case '/result':
        setPath('수정 완료');
        break;
      default:
        setPath('');
    }
  }, [location.pathname])

  return (
    <div className="header">
      <div onClick={() => history.push('/')} className="logo">
        <img src={src} alt="logo"/>
        <span className="service-name">FACE/OFF</span>
      </div>
      <div>{ path }</div>
      <div style={{ width: '105px'}}></div>
    </div>
  );
};

export default Header;
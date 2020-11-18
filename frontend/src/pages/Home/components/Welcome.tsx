import React, { useState } from 'react';

// components
import WelcomeItem1 from './WelcomeItem1';
import WelcomeItem2 from './WelcomeItem2';
// import WelcomeItem3 from './WelcomeItem3';
import './Home.scss';

function Welcome({ showCredit }) {
  const [item, setItem] = useState(0);

  if (item === 3) {showCredit()};

  // vars
  const itemNames = [ 'FACE/OFF란?', '사용하는 법', '만든 이들', ];
  const titles = [ 'Welcome!', 'About', 'How To Use', 'Created by'];

  // components
  const Title = () => ( <h1>{ titles[item] }</h1> );  
  const Item = ({ name, idx }) => {
    const onClick = () => {
      if (idx === 2) {showCredit()} 
      else {setItem(idx+1)}
    }
    return <li onClick={onClick} className="list-item"><p>{name}</p></li>
  };
  const ItemList = () => {
    const items = itemNames.map((name, idx) => <Item name={name} idx={idx} key={idx} />);
    return (<ul>{ items }</ul>);
  };
  const WelcomeItem0 = () => (
    <><p>
      FACE/OFF에 오신 것을 환영합니다.. <br/>
      아래 메뉴를 눌러 FACE/OFF에 대해 알아보십시오.
    </p><ItemList /></>
  );
  const ButtonGoBack = () => (
    <>{ item !== 0 && <div className="back-btn" onClick={() => setItem(0)}>메인 화면으로...</div>}</>
  );
  const Copyright = () => (
    <p className="copyright">
      © copyright 2020-2049. Not all right reserved.<br/>Powered by SSAFY.</p>
    );

  const Contents = () => (
    <>
      { item === 0 && <WelcomeItem0 /> }
      { item !== 0 &&
        <div className="content-area">
          { item === 1 && <WelcomeItem1 /> }
          { item === 2 && <WelcomeItem2 /> }
        </div>
      }
    </>
  )

  return (
    <>
      <div className="welcome">
        <div className="welcome-wrap">
          <Title />
          <div className="divider"></div>
          <ButtonGoBack />
          <Contents />
          <Copyright />
        </div>
      </div>
    </>
  );
}

export default Welcome;

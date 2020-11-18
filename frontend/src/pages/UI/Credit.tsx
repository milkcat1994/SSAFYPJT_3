import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../..';
import { hideCredit } from '../../redux/modules/modal';
import './Credit.scss';

function Credit() {
  const { creditShow } = useSelector((state: RootState) => state.modal);
  const dispatch = useDispatch();

  const srcBase = 'http://k3a207.p.ssafy.io/team/team';

  const people = [
    { role: '백엔드', name: '문명기 (팀장)' },
    { role: '백엔드', name: '정세린'},
    { role: 'AI', name: '양지용'},
    { role: 'AI', name: '오정엽'},
    { role: '프론트엔드', name: '이원준'},
    { role: '프론트엔드', name: '박태웅'},
    { role: '특별출연', name: 'Nick (가상인간)'},
  ]

  const names = people.map((person, idx) => {
    const style = {
      animationDelay: (500 * (idx + 2)) + 'ms',
    }
    return (
    <div style={style} key={idx} className="p-box">
      <div className="p-img">
        <img src={srcBase + (idx+1) + '.png'} alt=""/>
      </div>
      <div className="p-name">{person.name}</div>
      <div className="p-role">{person.role}</div>
    </div>
    );
  })

  const ButtonClose = () => (
    <div 
      onClick={() => dispatch(hideCredit())} 
      className="credit-close-btn">메인 화면으로..
    </div>
  )

  return (
    <>
      { creditShow &&
        <div className="credit-wrap">
          <ButtonClose />
          <h1>Created by</h1>
          <h1 className="team-name">SSAFY A207</h1>
          <div className="team-grid">
            { names }
          </div>
          <div className="thx">감사합니다.</div>
        </div>
      }
    </>
  )
}

export default Credit;

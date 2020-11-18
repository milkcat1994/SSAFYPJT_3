import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router';
import Message2 from '../../UI/Message2';
import './AddFriends.scss';

function AddFriends({ state, methods }) {
  const location = useLocation();
  useEffect(() => {
    if (location.pathname !== '/result') {hideModal();}
  });

  // props
  const { 
    faceDetected, friendsArray,
    show, visibleInput, 
    img, temp, idx, addFriendSelected
   } = state;

  const { 
    updateFriends, 
    hideModal, setVisibleInput, showMsg,
    setImg, setTemp, setIdx, setAddFriendSelected
  } = methods;


  // local vars
  const closeSrc = 'http://k3a207.p.ssafy.io/icon/close.png';
  let selected = [...addFriendSelected];
  
  // local state
  const [showMsg2, setShowMsg2] = useState(false);

  // components
  function Faces() {
    
    const faces = faceDetected.map((face,index) => {
      const style = {
        display: `${
          (addFriendSelected[index] === 'complete'
          || addFriendSelected[index] === 'temp')
          ? 'none' : 'flex'}`,
        opacity:
        `${(addFriendSelected[index] === 'no') ? '20%': '100%'}`
      }

      return (
        <div className="face-wrap" key={index} style={{ display: `${
          (addFriendSelected[index] === 'complete'
          || addFriendSelected[index] === 'temp')
          ? 'none' : 'block'}`,}}>
          <img
          onClick={() => {
            setImg(face[0]); setIdx(index);
            selected = selected.map((x) => (x === 'yet' || x === 'yes') ? 'no' : x);
            selected[index] = 'yes';
            setAddFriendSelected(selected);
          }}
          className={`base-face`} style={style}
          src={`data:image/png;base64,${face[0]}`} alt=""/>
          <div className="face-name" >{face[1]}</div>
        </div>
      )
    })
    return <div className="friend-face-grid">{ faces }</div>;
  }

  function Friends() {
    const Friends = friendsArray.map((friend,index) =>
      <div className='face-wrap' key={index}>
        <img
          className="base-face"
          src={`http://k3a207.p.ssafy.io/${friend.img}`}
          onClick={() => {
            if (!!img) {
              setTemp([...temp,[friend.kid,`data:image/png;base64,${img}`]]);
              setImg('')
              selected[idx] = 'temp';
              selected = selected.map((x) => {
                if (x === 'complete' || x === 'temp') {
                  return (x)
                } else {
                  return x = 'yet'
                }
              })
              setAddFriendSelected(selected)
            } else {
              showMsg('Warning', '등록하고 싶은 얼굴을 먼저 선택해주세요.');
            }
          }}
          alt=""
        />
        <div className="face-name">{friend.fname}</div>
      </div>
      )
    return(
      <>{ !visibleInput && Friends }</>
    )}

  function AddFriend() {
    const [fname, setFname] = useState('');
    const handleChange = e => setFname(e.target.value);
    
    const onClick = () => {
      !!img ? setVisibleInput(true) : showMsg('Warning', '등록하고 싶은 얼굴을 먼저 선택해 주세요.');
    };
    // sub-components 
    const ButtonInputConfirm = () => {
      const onClick = () => {
        const uid = sessionStorage.userId;
        if (fname && img) {
          setTemp([...temp,[uid,fname,`data:image/png;base64, ${img}`]]);
          setImg('')
          selected[idx] = 'temp';
          selected = selected.map(v => (v === 'complete' || v === 'temp') ? v : 'yet');
          setAddFriendSelected(selected);
          setVisibleInput(!visibleInput);
        } else if (!img) {
          showMsg('Warning', '친구를 선택해 주세요.');
        } else if (!fname) {
          showMsg('Warning', '이름을 입력해주세요.');
        }
      }
      return (
        <div onClick={onClick} 
        className={`base-btn ${fname ? 'font-blue' : ''}`}>확인</div>);
    }
    const ButtonInputCancel = () => (
      <div 
      onClick={() => {setVisibleInput(false); setFname('')}} 
      className="base-btn font-red">취소</div>);

    return(
      <>
        { !visibleInput &&
          <div onClick={onClick} className="add-friend-btn" >신규 <br/> 등록</div>
        }
        { visibleInput &&
          <div className="fname-input-wrap">
            <input 
              onChange={handleChange} 
              value={fname}
              type="text" className="fname-input" placeholder="unknown"
            />
            <ButtonInputCancel />
            <ButtonInputConfirm />
          </div>
        }
      </>
    )}

  function TempFriends() {
    const TempFriends = temp.filter((l) => (l.length > 2)).map((tempfriend,index) => {
      return (
        <div className='face-wrap' key={index}>
          <img className="base-face" src={tempfriend[2]} alt=""/>
          <div className="face-name">{tempfriend[1]}</div>
        </div>
        )
    })
    return <> { !visibleInput && TempFriends} </>;
  }

  
  // Component : Button
  const onClickClose = () => { temp.length ? setShowMsg2(true) : hideModal(); };
  const ButtonHeaderClose = () => (
  <div className="header-btn" onClick={onClickClose}><img src={closeSrc} alt=""/></div>
  );
  const ButtonComplete = () => {
    const onClick = () => {
      setAddFriendSelected(
        selected.map((x) => (x === 'complete' || x === 'temp') ? 'complete' : 'yet')
      ); 
      updateFriends();
      hideModal();
      showMsg('Success', '수정이 완료되었습니다.');
    }
    return (
      <div className="btn-wrap">
        <div onClick={onClick} className="base-btn">완료</div>
      </div>
    );
  };

  // Props for Component: Message
  const msg = {
    confirm() {
      setTemp([]);
      selected = selected.map((x) => (x === 'complete') ? x : 'yet');
      setAddFriendSelected(selected);
      setShowMsg2(false);
      hideModal();
    },
    cancel() {
      setShowMsg2(false)
    },
    text: <>
    완료버튼을 눌러야 변경사항이 저장됩니다. <br/> 
    저장하지 않고 종료하시겠습니까? 

    </>
  }

  return (
    <>
      { showMsg2 && <Message2 confirm={msg.confirm} cancel={msg.cancel} text={msg.text} />}
      { show &&
        <div className="add-friends">
          <div className="base-header">
            <div>아는 얼굴 등록하기</div>
            <ButtonHeaderClose />
          </div>

          <div className="divider"></div>
          <div className="section-title">탐지된 얼굴들</div>
          <Faces />

          <div className="divider"></div>
          <div className="section-title">등록된 얼굴들</div>
          <div className="friend-face-grid">
            <AddFriend />
            <Friends />
            <TempFriends />
          </div>
          
          <div className="divider"></div>
          <ButtonComplete />
        </div>
      }
    </>
  );
}

export default AddFriends;
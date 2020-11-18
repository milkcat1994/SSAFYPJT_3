import React, { useState } from 'react';

import Message from './Message2';
import { selectPicture } from '../../redux/modules/pic';

import { useHistory, useLocation } from 'react-router-dom';
import { useDispatch } from 'react-redux';

// components
function ButtonUpload({ content, className }) {
  const dispatch = useDispatch();
  const location = useLocation();
  const history = useHistory();

  // local state
  const [showMsg, setShowMsg] = useState(false);
  
  // vars
  const input = document.querySelector('.input-file') as HTMLElement;

  // methods
  const handleImageUpload = (e) => { 
    const picURL = URL.createObjectURL(e.target.files[0]);
    dispatch(selectPicture(''));
    dispatch(selectPicture(picURL));
    history.push('/');
  };

  const onClickButton = () => {
    if (location.pathname === '/edit') {
      setShowMsg(true);
    } else {
      const input = document.querySelector('.input-file') as HTMLElement;
      input.click();
    }
  }
  
  // message
  const text = <>진행사항은 저장되지 않습니다. <br/> 새 사진을 수정하시겠습니까?</>
  const cancel = () => setShowMsg(false);
  const confirm = () => {input.click(); setShowMsg(false);};
  
  return (
    <>
        <div onClick={onClickButton} className={className}>
          { content }
          <input 
            className="input-file"
            onChange={handleImageUpload} style={{display:"none"}}
            type="file" accept="image/*" />
        </div>
        { showMsg && <Message confirm={confirm} cancel={cancel} text={text} /> }
    </>
  )
}

export default ButtonUpload;
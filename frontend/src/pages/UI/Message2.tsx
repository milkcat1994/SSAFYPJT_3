import React from 'react';

function Message({ confirm, cancel, text }) {

  return (
    <div className="overlay">
      <div className="msg-card">
        <div className="msg-card-header">Warning</div>
        <div className="msg-card-text">{ text }</div>
        <div className="msg-card-footer">
          <div onClick={cancel} className="base-btn">취소</div>
          <div onClick={confirm} className="base-btn">확인</div>
        </div>
      </div>
    </div>
  );
}

export default Message;
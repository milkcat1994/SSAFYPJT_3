import React from 'react';

function Message({ state, methods }) {
  const { msgShow, msgTitle, msgText } = state;
  const { close } = methods;

  return (
    <>
      { msgShow &&
      <div className="overlay">
        <div className="msg-card">
          <div className="msg-card-header">{ msgTitle }</div>
          <div className="msg-card-text">{ msgText }</div>
          <div className="msg-card-footer">
            <div onClick={close} className="base-btn">확인</div>
          </div>
        </div>
      </div>
      }
    </>
  );
}

export default Message;
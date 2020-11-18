import React, { useEffect } from 'react';
import './Loading.scss';

function Loading({ show }) {

  useEffect(() => {
    window.scrollTo(0, 0);
    if (show) {
      document.body.classList.add('no-scroll');
    } else {
      document.body.classList.remove('no-scroll');
    }
  });

  const LoadingBlock = () => {
    return <div className="loading-block"></div>
  }

  const LoadingBlocks = () => {
    const blocks = Array(20).fill('').map((v, index) => <LoadingBlock key={index} />)
    return <>{blocks}</>
  }


  return (
    <>
      { show && 
        <div className="overlay">
          <div className="msg-card">
            <div className="msg-card-header">LOADING...</div>  
            <div className="loading-block-wrap">
              <LoadingBlocks />
            </div>
          </div>
        </div>
      }
    </>
  )
}

export default Loading;

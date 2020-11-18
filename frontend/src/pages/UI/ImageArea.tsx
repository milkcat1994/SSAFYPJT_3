import React from 'react';
import '../../base.scss';


function ImageArea({ picURL }) {
  return (
    <div className="pic-area">
      <div className="img-wrap">
        <img src={picURL} alt="" />
      </div>
    </div>
  );
}

export default ImageArea;

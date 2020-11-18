import React from 'react';

function PicEditImageArea({ picURL, FaceArea }) {
  return (
    <div className="pic-area">
      <div className="img-wrap">
        <img src={picURL} alt="" />
        { FaceArea }
      </div>
    </div>
  );
}

export default PicEditImageArea;

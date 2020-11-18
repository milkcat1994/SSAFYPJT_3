import React from 'react';
import '../../base.scss';
import FaceArea from '../PidEdit/components/FaceArea'


function EditImageArea({ state, methods }) {
  const { picURL, faceArea, selectedFaceIdx } = state
  const { setSelectedFaceIdx } = methods
  return (
    <div className="pic-area">
      <div className="img-wrap" style={{position:'relative'}}>
        <img src={picURL} alt="" />
        <FaceArea faceArea={faceArea} selectedFaceIdx={selectedFaceIdx} setSelectedFaceIdx={setSelectedFaceIdx} />
      </div>
    </div>
  );
}

export default EditImageArea;

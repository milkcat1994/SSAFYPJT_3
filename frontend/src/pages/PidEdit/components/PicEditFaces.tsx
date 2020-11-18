import React from 'react';

function PicEditFaces({ state, methods }) {
  // props
  const { faceDetected, selectedFaceIdx } = state;
  const { setSelectedFaceIdx } = methods;

  // methods
  const selectAll = () => setSelectedFaceIdx(selectedFaceIdx.map(v => true));
  const unSelectAll = () => setSelectedFaceIdx(selectedFaceIdx.map(v => false));


  // components
  const Face = ({face, index}) => {
    const src = `data:image/png;base64, ${face[0]}`;
    const onClickFace = () => {
      setSelectedFaceIdx(selectedFaceIdx.map((v, i) => i === index ? !v : v));
    };

    return (
      <div 
      onClick={onClickFace}
        className={`face-wrap ${selectedFaceIdx[index] ? 'face-selected' : ''}`}>
        <img src={src} alt="" className="face-img-wrap"/>
        <div className="face-name">{face[1]}</div>
      </div>
    );
  }

  const Faces = faceDetected.map((face, index) => (
    <Face face={face} key={index} index={index} />
  ));

  return (
    <>
      <div className="pic-edit-faces-legend">가리고 싶은 얼굴을 선택하십시오.</div>
      <div className="flex">
        <div onClick={selectAll} className="sticker-type-btn">전체선택</div>
        <div onClick={unSelectAll} className="sticker-type-btn">전체취소</div>
      </div>
      <div className="pic-edit-faces"> { Faces } </div>
    </>
  ) 
}

export default PicEditFaces;
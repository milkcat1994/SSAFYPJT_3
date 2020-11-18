import React, { useEffect, useState } from 'react';

function FaceArea( { faceArea, selectedFaceIdx, setSelectedFaceIdx } ) {
  const getRatio = (el) => (el.width / el.naturalWidth);
  const image = document.querySelector('div.img-wrap img') as HTMLImageElement;

  const [ratio, setRatio] = useState(getRatio(image));
  let tempSelected = selectedFaceIdx.slice();

  const handleResize = () => {setRatio(getRatio(image));};

  useEffect(() => {
    handleResize();
    window.addEventListener('resize', handleResize);
    return () => {
      window.removeEventListener('resize', handleResize);
    }
  })

  // components
  const FaceBox = ({ pos, index }) => {
    const [x1, y1, x2, y2] = pos;
    const top = (y1 * ratio) + 'px';
    const left = (x1 * ratio) + 'px';
    const width = ((x2 - x1) * ratio) + 'px';
    const height = ((y2 - y1) * ratio) + 'px';
    const isSelected = tempSelected[index];

    const style = {
      borderColor: isSelected ? 'red' : 'lawngreen',
      borderWidth: isSelected ? '2px' : '1px',
      borderStyle: isSelected ? 'dashed' : 'solid',
      backgroundColor: isSelected ? 'rgba(0, 0, 0, 0.5)' : 'none',
      top, left, width, height
    };

    const onClick = () => {
      tempSelected[index] = !tempSelected[index];
      setSelectedFaceIdx(tempSelected);
    };

    return <div onClick={onClick} className="face-box" style={style}></div>;
  };

  const Boxes = faceArea.map((pos, index) => (
    <FaceBox pos={pos} index={index} key={index} />
  ));
  
  return <>{image && Boxes}</>;
}

export default FaceArea;
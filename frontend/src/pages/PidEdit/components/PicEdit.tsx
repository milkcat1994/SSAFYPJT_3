import React, { useEffect, useState } from 'react';
import './PicEdit.scss';
import { useHistory } from 'react-router-dom';

// components
import EditImageArea from '../../UI/EditImageArea';
import PicEditOptions from './PicEditOptions';
import PicEditFaces from './PicEditFaces';

function PicEdit({ state, methods }) {
  const history = useHistory();
  useEffect(() => {
    if (!picURL) { history.push('/');}
  })

  // props
  const { picURL, faceDetected, optionTypeNamesKr, optionTypeIdx, optionLevel, selectedFaceIdx } = state;
  const { setSelectedFaceIdx, onUploadOptions } = methods;

  // local state
  const [ menu , setMenu ] = useState(0);
  
  // vars
  const optionSelected = 
  `: ${optionTypeNamesKr[optionTypeIdx]} ${optionTypeIdx < 2 ? optionLevel : ''}`;

  // components
  const MenuItem = ({index, name}) => {
    const className = `menu-item ${menu === index ? 'menu-item-active' : ''}`;
    return (
      <div onClick={() => setMenu(index)} className={className}>
        { name }
        <span className="font-blue">{index === 0 && optionSelected }</span>
      </div>
    );
  }
  return (
    <>
      { picURL && 
        <>
        <div className="pic-edit">
          <div className="image-area-wrap" >
            <EditImageArea state={state} methods={methods} />
          </div>
          <div className="menu-wrap">

            <div className="menu-item-wrap">
              <MenuItem index={0} name={'옵션'} />
              <MenuItem index={1} name={'얼굴 선택'} />
            </div>
            
            <div className="menu-detail-wrap">
              { menu === 0 && 
                <PicEditOptions state={state} methods={methods} /> 
              }
              { menu === 1 && 
                <PicEditFaces 
                state={{ faceDetected, selectedFaceIdx}}
                methods={{setSelectedFaceIdx}} /> 
              }
            </div>
          </div>
        </div>
        
        <div className="divider"></div>
        <div className="btn-wrap">
          <div className={`base-btn ${ selectedFaceIdx.filter(v => v).length ? 'font-blue' : ''}`} 
            onClick={onUploadOptions}>실행하기</div>
        </div>
      </>
      }
    </>
  );
}

export default PicEdit;

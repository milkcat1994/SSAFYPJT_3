import React from 'react';
import PicEditStickerContainer from './PicEditStickerContainer';

function PicEditOptionsDetail({ state, methods }) {
  const { optionTypeIdx, optionLevel } = state;
  const { handleOptionLevel } = methods;
  const sampleSrc = 'http://k3a207.p.ssafy.io/icon/';



  return (
    <>
        { optionTypeIdx < 2 &&
        <div className="option-detail-wrap">
          <div className="option-level">
            <div className="base-face"><img src={sampleSrc+`${optionTypeIdx}${optionLevel}.png`} alt=""/></div>
            <div className="option-level-input-wrap">
              <input 
                onChange={handleOptionLevel}
                type="range" min="1" max="5" value={optionLevel} step="1" />
            </div>
          </div>
        </div>
        }
        { optionTypeIdx === 2 && 
          <div className="option-level">인공지능이 생성한 가상 얼굴로 대체합니다.</div>
        }
        {
          optionTypeIdx === 3 &&
          <PicEditStickerContainer />
        }
    </>
  );
}

export default PicEditOptionsDetail;

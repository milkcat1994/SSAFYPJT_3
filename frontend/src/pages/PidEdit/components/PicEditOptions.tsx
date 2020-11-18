import React from 'react';
import './PicEditOptions.scss';
import PicEditOptionsDetail from './PicEditOptionsDetail';

function PicEditOptions({ state, methods }) {
  // props
  const { optionTypeIdx, optionTypeNamesKr } = state;
  const { setOptionType } = methods;

  // vars
  const baseSrc = 'http://k3a207.p.ssafy.io/icon/';
  const imgSrc = [ 'pixel.png', 'blur3.png', 'swap.png','sticker2.png']

  // components
  const ButtonOptionTypes = optionTypeNamesKr.map((name, index) => {
    const buttonClassName = `option-item-btn ${ optionTypeIdx === index ? 'option-item-btn-active' : ''}`;

    return (
      <div onClick={() => setOptionType(index)} className='option-item'  key={ index }>
        <div className={buttonClassName}>
          <img src={baseSrc + imgSrc[index]} alt=""/>
        </div>
        <div className={`${optionTypeIdx === index ? 'font-blue' : ''}`}>{ name }</div>
      </div>
    )
  });
  
  return (
    <div className="pic-edit-options">
      <div className="option-item-wrap">{ ButtonOptionTypes }</div>
      <PicEditOptionsDetail state={state} methods={methods} />
    </div>
  );
}

export default PicEditOptions;
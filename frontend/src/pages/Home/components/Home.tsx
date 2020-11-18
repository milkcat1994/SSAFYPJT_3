import React  from 'react';

// components
import ImageArea from '../../UI/ImageArea';
import Welcome from './Welcome';
import './Home.scss';

function Home({ state, methods }) {
  const { picURL } = state;
  const { showCredit, onSelectPicture, onStart } = methods;
  
  // methods
  const handleImageUpload = (e) => { 
    onSelectPicture(URL.createObjectURL(e.target.files[0]))
  };

  // components
  const ButtonUpload = ({ text }) => (
      <label>
        <input 
          onChange={handleImageUpload} style={{display:"none"}}
          type="file" accept="image/*" />
        <div className="base-btn">{text}</div>
      </label>
  );
  const ButtonStart = () => (
    <>{ picURL && <div onClick={onStart} className="base-btn font-blue">시작하기!</div>}</>
  );

  return (
    <>
      { !picURL && <Welcome showCredit={showCredit} /> }

      { picURL &&
        <div className="home-image-wrap">
          <ImageArea picURL={picURL} />
        </div>
      }
      <div className="divider"></div>

      <div className="btn-wrap">
        <ButtonStart />
        <ButtonUpload text={picURL ? '다른 사진' : '시작하기!'} />
      </div>
    </>
  );
}

export default Home;
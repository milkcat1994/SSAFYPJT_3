import React from 'react';
import './PicResult.scss';

// components
import ImageArea from '../../UI/ImageArea';
import ButtonUpload from '../../UI/ButtonUploadBase';
import { useHistory } from 'react-router-dom';

function PicResult({ state, methods }) {
  const history = useHistory();

  // props
  const { isAuthed, resultPicURL } = state;
  const { showModal } = methods;

  const download = () => {
    const element = document.createElement("a");
    element.href = resultPicURL;
    element.download = "after_FACEOFF.jpg";
    element.click();
  };

  // components
  const ButtonDownload = () => (
    <div onClick={download} className="base-btn">저장하기</div>
  );

  const ButtonReEdit = () => (
    <div onClick={() => history.goBack()} className="base-btn">다시 수정하기</div>
  );

  const ButtonFriendRegister = () => (
    <div onClick={showModal} className="base-btn">아는 얼굴 등록하기</div>
  );

  return (
    <>
    <div className="pic-result">
      <ImageArea picURL={resultPicURL} />
      <div className="divider hide-on-PC"></div>
      
      <div className="btn-wrap2">
        <ButtonDownload />
        <div className="divider show-on-PC"></div>
        <ButtonReEdit />
        <ButtonUpload content={<>다른 사진 수정하기</>} className="base-btn" />
        <div className="divider show-on-PC"></div>
        {isAuthed && <ButtonFriendRegister />}
      </div>
    </div>
    <div className="show-on-PC">
      <div className="divider"></div>
      <div className="btn-wrap"></div>
    </div>
    </>
  );
}

export default PicResult;
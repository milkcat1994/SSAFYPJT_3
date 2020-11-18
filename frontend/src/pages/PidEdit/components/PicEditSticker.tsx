import React, {useState} from 'react';

function PicEditSticker({ state, methods }) {
  const { isAuthed, stickerBase, stickerUser, selectedStickerIdxBase, selectedStickerIdxUser } = state;
  const { fetchStickerBase, fetchStickerUser, selectSticker, addSticker, deleteSticker, showMessage, } = methods;
  
  if (!stickerBase.length) { fetchStickerBase(); };

  // vars
  const typeNames = ['기본 스티커', '내 스티커'];
  const srcBase = 'http://k3a207.p.ssafy.io/';

  // local state
  const [ stickerType, setStickerType ] = useState(typeNames[0]);

  // components
  const ButtonAddSticker = () => {
    const handleImageUpload = async (e) => { 
      addSticker({
        uid: sessionStorage.userId,
        img: URL.createObjectURL(e.target.files[0])
      })
    };

    return (
      <label>
        <input 
          onChange={handleImageUpload} style={{display:"none"}}
          type="file" accept="image/*" />
        <div className="base-face chewy">+</div>
      </label>
    )
  };

  const Sticker = ({ item, idx }) => {
    const imgSrc = srcBase + item.img;
    const isUser = stickerType === '내 스티커';
    const selectedIdx = isUser ? selectedStickerIdxUser : selectedStickerIdxBase ;

    return (
      <div 
        onClick={() => {selectSticker(imgSrc, idx, stickerType)}}
        className={`sticker ${selectedIdx === idx ? 'sticker-selected' : ''}`}>
        <img src={imgSrc} alt=""/>
        { isUser &&
          <div onClick={() => deleteSticker(item.sid)} className="sticker-delete-btn">
          <div></div>
        </div>
        }
      </div>
  )};

  const StickerBase = () => {
    const list = stickerBase.map((item, index) => (
      <Sticker key={index} item={item} idx={index} />
    ));
    return <div className="sticker-grid">{ list }</div>;
  }

  const StickerUser = () => {
    const list = stickerUser.map((item, index) => (
      <Sticker key={index} item={item} idx={index} />
    ));
    return <div className="sticker-grid"><ButtonAddSticker />{ list }</div>;
  }

  return (
    <>
      <div className="flex">
        <div 
          onClick={() => setStickerType(typeNames[0])}
          className='sticker-type-btn' >{ typeNames[0] }
        </div>
        <div 
          onClick={() => {
            if (isAuthed) {
              setStickerType(typeNames[1]);
              fetchStickerUser();
            } else {
              showMessage();
            }
          }}
          className='sticker-type-btn' >{ typeNames[1] }
        </div>
      </div>

      { stickerType === typeNames[0] && <StickerBase /> }
      { stickerType === typeNames[1] && <StickerUser /> }

    </>
  )
}

export default PicEditSticker;
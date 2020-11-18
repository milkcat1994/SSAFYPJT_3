import React,{ useState} from 'react';

function DetailFriend( {state, methods }) {
  // props
  const { mainFace, otherFaces, friendName } = state;
  const { 
    deleteFriend, deleteFriendFace,viewAllFriends,updateFriendName, updateFriendImg 
  } = methods;

  // local state
  const [action, setAction] = useState('none');
  
  // local vars
  const messages = {
    'none': `${otherFaces.length + 1}개의 얼굴이 등록되어 있습니다.`,
    'update': '메인사진으로 사용할 얼굴을 선택해주세요.',
    'delete': '삭제할 얼굴을 선택해주세요.'
  }

  function MainFace () {
    const initName = !!mainFace.fname ? mainFace.fname : friendName;
    
    const [fname,setFname] = useState(initName);
    const [viewNameChangeInput, setViewNameChangeInput] = useState(false);
    return (
      <div
        style={{width: `100%`,
          maxWidth: `500px`,
          margin: `auto`,
        display:'flex'}}
      > 
        {mainFace.img && 
        <img className="base-face" src={`http://k3a207.p.ssafy.io/${mainFace.img}`} alt="" 
          style={{
            width: `30%`,
            height: `30%`,
            margin: `3%`,
            display:'inline-block',
            minHeight:`80px`,
            minWidth:`80px`,
          }}/>
        }
        <div style= {{width:`57%`, margin:`3%`}}>
          <h2 style= {{textAlign:`center`,margin:'20px 0'}}>{fname}</h2>
          { !viewNameChangeInput && 
            <div className="base-btn" onClick={() => setViewNameChangeInput(!viewNameChangeInput)}>이름수정</div>
          }
          { viewNameChangeInput && 
          <>
            <input type="text" className="fname-input" style={{width:`100%`}} defaultValue={fname} onChange={(e) => setFname(e.target.value)} />
            <div className="base-btn" onClick={() => {
              setViewNameChangeInput(!viewNameChangeInput);
              updateFriendName(mainFace.kid,fname)
            }}>
              완료
            </div>
          </>
          }
          
          <div className="base-btn font-red" onClick={deleteFriend}>친구삭제</div>

        </div>
      </div>
    )
  } 

  const Others = otherFaces.map((otherFace) => {
    const onClickFace = () => {
      if (action === 'delete') { 
        deleteFriendFace(otherFace.fid); 
      }
      else if (action === 'update') {
        updateFriendImg(otherFace.kid, otherFace.fid);
      }
    };

    return ( 
    <div className="face-wrap" key={otherFace.fid} style={{paddingTop:'25px', paddingBottom:`25px`}}>  
      <img 
      onClick={onClickFace}
      className="base-face" style={{margin:`auto`}} src={`http://k3a207.p.ssafy.io/${otherFace.img}`} alt="" />
    </div>
    );
  });

  const ButtonOptionSelect = ({ type, name }) => {
    const style = { flexGrow: 2}
    return (
    <div onClick={() => setAction(type)} className="base-btn" style={style}>
      { name }
    </div>);
  }

  const ButtonComplete = () => (
    <div onClick={() => setAction('none')} 
      className="base-btn" style={{flexGrow: 2}}>완료</div>   
  );

  return (
    <>
      <div className="base-btn" onClick={viewAllFriends}>전체보기</div>
      <div className="legend">{messages[action]}</div>
      <MainFace />
      <div className="divider"></div>
      <div className="flex">

        {action === 'none' &&        
          <>
          <ButtonOptionSelect type="update" name="메인사진 바꾸기" />
          <ButtonOptionSelect type="delete" name="사진 삭제하기" />
          </>
        }
        {action !== 'none' && <ButtonComplete />}
      </div>

      <div className="face-grid base-face-grid" 
      style={{
          margin: `auto`,
          gridTemplateColumns: `repeat(auto-fill, 85px)`,
        }}
      >
        {Others}
      </div>
    </>)
}

export default DetailFriend;
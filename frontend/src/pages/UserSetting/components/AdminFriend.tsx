import React, { useEffect } from 'react';
import DetailFriend from './DetailFriend';

function AdminFriend({ state, methods } ) {

  useEffect(() => {
    const self = document.querySelector('.admin-friend');
    window.scrollTo(0, self?.scrollTop || window.innerHeight);
  })

  //state
  const { adminFriendsModalShow, friendsArray, viewDetail} = state;
  //methods
  const { setViewDetail, getFriendDetail, setFriendName, hideAdminFriend } = methods;

  //component
  function Friends() {
    if (friendsArray.length) {

      const Friend = friendsArray.map((friend) => {
        return (
          <div className="face-wrap" key={friend.kid}>
            <img
              src={`http://k3a207.p.ssafy.io/${friend.img}`}
              onClick={() => {
                setViewDetail(friend.kid); 
                getFriendDetail(friend.kid); 
                setFriendName(friend.fname);}}
              className="base-face"
              alt=''
            />
            <div className="face-name">{friend.fname}</div>
          </div>
        )})
      return (<div className="face-grid base-face-grid">{Friend}</div>);
    } else {
      return <div></div>
    }
  }

  return(
    <div className="admin-friend">
      { adminFriendsModalShow && 
        <div className="window">
          <div className="base-header">
            <div>아는 얼굴 관리</div>
            <div onClick={hideAdminFriend} className="header-btn">
            <img src="http://k3a207.p.ssafy.io/icon/close.png" alt=""/>
            </div>
          </div>
          { (friendsArray.length !==0 && !viewDetail) && 
            <div className="legend"> 총 {friendsArray.length}명의 얼굴이 등록되어 있습니다.</div>
          }

          {(viewDetail === 0) && 
            <Friends />
          }
          {(viewDetail !== 0) && 
            <DetailFriend state={state} methods={methods} />
          }

          { !friendsArray.length &&
            <div>
              <h3>아직 등록된 얼굴이 없습니다.</h3>
            </div>
          }

        </div>  
      }
    </div>
  );  
};

export default AdminFriend;
import React,{ useState} from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../../../index';
import { hideAddFriendsModal } from '../../../redux/modules/modal'
import { setAddFriendSelected } from '../../../redux/modules/friend'
import AddFriends from './AddFriends';
import API from '../../../api';
import { showMessage } from '../../../redux/modules/message';

function AddFriendsContainer() {
  const [visibleInput,setVisibleInput] = useState(false);
  const [img,setImg] = useState(''); // 클릭하는 이미지 잠시 저장하기 위함
  const [temp,setTemp] = useState([] as any) // 친구등록 요청 보내기 전 임시 저장
  const [idx,setIdx] = useState(0)
  const dispatch = useDispatch();


  // state
  const state = {
    faceDetected :useSelector((state: RootState) => state.pic.faceDetected),
    show: useSelector((state: RootState) => state.modal.addFriendsModalShow),
    friendsArray: useSelector((state:RootState) => state.friend.friendsArray),
    addFriendSelected: useSelector((state:RootState) => state.friend.addFriendSelected),
    visibleInput,
    img,
    temp,
    idx,
  };

  // methods
  const methods = {
    setVisibleInput,
    setImg,
    setTemp,
    setIdx,
    hideModal() {
      dispatch(hideAddFriendsModal());
    },
    setAddFriendSelected(addFriendSelected) {
      dispatch(setAddFriendSelected(addFriendSelected));
    },
    updateFriends() {
      temp.forEach(e => {
        if (e.length === 3) {
          API.addFriends(e[0], e[1], e[2])
            .then(res => {
            })
            .catch(err => console.error(err))
        } else {
          API.addFriendsFace(e[0],e[1])
            .then(res => {
            })
            .catch(err => {
              console.error(err)
            })
        }     
      });
      setTemp([])
    },
    showMsg(title, text) {
      dispatch(showMessage(title, text));
    },
  };

  return <AddFriends state={state} methods={methods} />;
}

export default AddFriendsContainer
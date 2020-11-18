import React,{ useState } from 'react';

// components
import AdminFriend from './components/AdminFriend';

// modules
import API from '../../api';
import { useHistory } from 'react-router-dom';

// redux
import { RootState } from '../../index';
import { logout } from '../../redux/modules/auth';
import { useDispatch, useSelector } from 'react-redux';
import { setFriendsArray,setFriendMainFace, setFriendOtherFaces } 
from '../../redux/modules/friend';
import { hideAdminFriendsModal } from '../../redux/modules/modal';

function AdminFriendContainer() {
  const dispatch = useDispatch();
  const history = useHistory()
  
  const [viewDetail, setViewDetail] = useState(0);
  const [friendName, setFriendName] = useState('');
  const [viewFriends, setViewFriends] = useState(false);

  const state = {
    friendsArray: useSelector((state:RootState) => state.friend.friendsArray),
    mainFace: useSelector((state:RootState) => state.friend.mainFace),
    otherFaces: useSelector((state:RootState) => state.friend.otherFaces),
    adminFriendsModalShow: useSelector(
      (state:RootState) => state.modal.adminFriendsModalShow),
    viewDetail,
    viewFriends,
    friendName,
  };

  const methods = {
    setViewDetail,
    setViewFriends,
    setFriendName,
    deleteUser() {
      API.deleteUser()
        .then((res) => {
          sessionStorage.clear();
          dispatch(logout());
          history.push('/');
        })
    },
    viewAllFriends() {
      setViewDetail(0);
      dispatch(setFriendMainFace({}));
      dispatch(setFriendOtherFaces([]));
      API.getFriendsList(sessionStorage.userId)
      .then((res) => {
        dispatch(setFriendsArray(res.data));
      })
      .catch((err) => console.error(err));
    },
    getFriendsList() {
      API.getFriendsList(sessionStorage.userId)
      .then((res) => {
        dispatch(setFriendsArray(res.data));
      })
      .catch((err) => console.error(err));
    },
    getFriendDetail(viewDetail) {
      API.detailFriends(viewDetail)
        .then((res) => {
          dispatch(setFriendMainFace(res.data.main_face));
          dispatch(setFriendOtherFaces(res.data.others));
        })
        .catch((err) => console.error(err))
    },
    deleteFriend() {
      API.deleteFriends(viewDetail)
        .then((res) => {
          setViewDetail(0);
          dispatch(setFriendMainFace({}));
          dispatch(setFriendOtherFaces([]));
          API.getFriendsList(sessionStorage.userId)
          .then((res) => {
            dispatch(setFriendsArray(res.data));
          })
          .catch((err) => console.error(err));
        })
        .catch((err) => console.error(err))
    },
    deleteFriendFace(fid) {
      API.deleteFriendsFace(fid)
        .then((res) => {
          API.detailFriends(viewDetail)
          .then((res) => {
            dispatch(setFriendOtherFaces(res.data.others));
          })
          .catch((err) => console.error(err))
        })
        .catch((err) => console.error(err))
    },
    updateFriendName(kid,fname) {
      API.updateFriendName(kid,fname)
        .then((res) => {
          dispatch(setFriendMainFace(res.data))
        })
        .catch((err) => {});
    },
    updateFriendImg(kid, fid) {
      API.updateFriendImg(kid,fid)
        .then((res) => {
          API.detailFriends(viewDetail)
          .then((res) => {
            dispatch(setFriendMainFace(res.data.main_face));
            dispatch(setFriendOtherFaces(res.data.others));
          })
          .catch((err) => console.error(err));
        })
        .catch((err) => console.error(err));
    },
    hideAdminFriend() {
      dispatch(hideAdminFriendsModal());
    }
  }

  return <AdminFriend state={state} methods={methods} />;
}

export default AdminFriendContainer;
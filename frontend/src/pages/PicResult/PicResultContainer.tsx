import React from 'react';

// components
import PicResult from './component/PicResult';

// redux
import { useDispatch, useSelector } from 'react-redux';
import { showAddFriendsModal, hideAddFriendsModal } from '../../redux/modules/modal';
import { setFriendsArray } from '../../redux/modules/friend';
import { RootState } from '../../index';
import API from '../../api';

function PicResultContainer() {
    const dispatch = useDispatch();

    // state
    const state = {
      isAuthed : useSelector((state: RootState) => state.auth.isAuthed),
      resultPicURL :useSelector((state: RootState) => state.pic.resultPicURL),
      friendsArray: useSelector((state: RootState) => state.friend.friendsArray),
      addFriendSelected: useSelector((state: RootState) => state.friend.addFriendSelected),
    };

    // methods
    const methods = {
      showModal() {
        API.getFriendsList(sessionStorage.userId)
        .then((res) => {
          dispatch(setFriendsArray(res.data));
        })
        .catch((err) => console.error(err));
        dispatch(showAddFriendsModal());
        setTimeout(() => {
          window.scrollBy(0, window.innerHeight);
        }, 300);
      },
      hideModal() {
        dispatch(hideAddFriendsModal());
      },
    };

  return <PicResult state={state} methods={methods} />;
} 

export default PicResultContainer;
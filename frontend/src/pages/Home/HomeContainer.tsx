import React from 'react';

// components
import Home from './components/Home';

// modules
import API from '../../api';
import { useHistory } from 'react-router-dom';

// redux
import { useSelector, useDispatch } from 'react-redux';
import { selectPicture, setFaceDetected, setFaceArea, setSelectedFaceIdx } from '../../redux/modules/pic';
import { hideLoading, showLoading } from '../../redux/modules/message';
import { setAddFriendSelected } from '../../redux/modules/friend';
import { RootState } from '../../index';
import { showCredit } from '../../redux/modules/modal';

function HomeContainer() {
  const dispatch = useDispatch();
  const history = useHistory();

  // state
  const state = {
    picURL: useSelector((state:RootState) => state.pic.picURL),
  };

  // methods
  const methods = {
    showCredit() {
      dispatch(showCredit());
    },
    onSelectPicture(picURL: string){
      dispatch(selectPicture(picURL));
    },
    onStart() {
      dispatch(showLoading());
      API.uploadPic(state.picURL)
        .then(res => {
          const addFriendSelected = new Array(res.data.faces_area.length).fill('yet');
          let selectedFaceIdx = new Array(res.data.faces_area.length).fill(true);
          let faceDetected = res.data.faces_crop.map((x) => [x,'unknown']);
          res.data.friend_list.map((x) => {
            selectedFaceIdx[x['idx']] = false;
            faceDetected[x['idx']] = [faceDetected[x['idx']][0],x['fname']]
            return (x)
          })
          dispatch(setFaceArea(res.data.faces_area));
          dispatch(setFaceDetected(faceDetected));
          dispatch(setSelectedFaceIdx(selectedFaceIdx));
          dispatch(setAddFriendSelected(addFriendSelected));
          setTimeout(() => {dispatch(hideLoading()); history.push('/edit');}, 1000);
        })
        .catch(() => dispatch(hideLoading()))
    },
  };

  return <Home state={state} methods={methods} />
}

export default HomeContainer
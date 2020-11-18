import { createAction, createReducer } from '@reduxjs/toolkit';

// actionTypes
const SHOW_MESSAGE: string = 'message/SHOW_MESSAGE';
const HIDE_MESSAGE: string = 'message/HIDE_MESSAGE';
const SHOW_LOADING: string = 'message/SHOW_LOADING';
const HIDE_LOADING: string = 'message/HIDE_LOADING';


// actions
export const showMessage = createAction(
  SHOW_MESSAGE,
  function prepare(msgTitle = '', msgText = '') {
    return { payload: { msgTitle, msgText} };
  }
)
export const hideMessage = createAction(HIDE_MESSAGE);
export const showLoading = createAction(SHOW_LOADING);
export const hideLoading = createAction(HIDE_LOADING);

const initState = {
  msgShow: false,
  msgTitle: '',
  msgText: '',
  loadingShow: false
}

const message = createReducer(initState, (builder) => {
  builder
  .addCase(showMessage, (state, action) => {
    state.msgShow = true;
    state.msgTitle = action.payload.msgTitle;
    state.msgText = action.payload.msgText;
  })
  .addCase(hideMessage, (state) => {
    state.msgShow = false;
    state.msgTitle = '';
    state.msgText = '';
  })
  .addCase(showLoading, (state) => {
    state.loadingShow = true;
  })
  .addCase(hideLoading, (state) => {
    state.loadingShow = false;
  })

});

export default message;

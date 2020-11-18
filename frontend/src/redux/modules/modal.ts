import { createAction, createReducer } from '@reduxjs/toolkit';

// actionTypes
const SHOW_ADD_FRIENDS: string = 'modal/SHOW_ADD_FRIENDS';
const HIDE_ADD_FRIENDS: string = 'modal/HIDE_ADD_FRIENDS';
const SHOW_ADMIN_FRIENDS: string = 'modal/SHOW_ADMIN_FRIENDS';
const HIDE_ADMIN_FRIENDS: string = 'modal/HIDE_ADMIN_FRIENDS';
const SHOW_CREDIT = 'modal/SHOW_CREDIT';
const HIDE_CREDIT = 'modal/HIDE_CREDIT';


// actions
export const showAddFriendsModal = createAction(SHOW_ADD_FRIENDS);
export const hideAddFriendsModal = createAction(HIDE_ADD_FRIENDS);
export const showAdminFriendsModal = createAction(SHOW_ADMIN_FRIENDS);
export const hideAdminFriendsModal = createAction(HIDE_ADMIN_FRIENDS);
export const showCredit = createAction(SHOW_CREDIT);
export const hideCredit = createAction(HIDE_CREDIT);

const initState = {
  addFriendsModalShow: false,
  adminFriendsModalShow: false,
  creditShow: false,
};

const modal = createReducer(initState, (builder) => {
  builder
  .addCase(showAddFriendsModal, (state) => {
    state.addFriendsModalShow = true;
  })
  .addCase(hideAddFriendsModal, (state) => {
    state.addFriendsModalShow = false;
  })
  .addCase(showAdminFriendsModal, (state) => {
    state.adminFriendsModalShow = true;
  })
  .addCase(hideAdminFriendsModal, (state) => {
    state.adminFriendsModalShow = false;
  })
  .addCase(showCredit, (state) => {
    state.creditShow = true;
  })
  .addCase(hideCredit, (state) => {
    state.creditShow = false;
  })

});

export default modal;

import { createAction,createReducer } from '@reduxjs/toolkit';

/* Action Types */
const LOG_IN: string = "auth/LOG_IN";
const LOG_OUT: string = "auth/LOG_OUT";

/* Action Functions */
export const login = createAction(LOG_IN);
export const logout = createAction(LOG_OUT);

/* Initial State */
const initState = {
  isAuthed: !!sessionStorage.getItem('userId'),
}

const auth = createReducer(initState, (builder) => {
  builder
  .addCase(login, (state) => {
    state.isAuthed = true;
  })
  .addCase(logout, (state) => {
    state.isAuthed = false;
  })
})

export default auth
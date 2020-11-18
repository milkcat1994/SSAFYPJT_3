import { createAction, createReducer } from '@reduxjs/toolkit';

// stickers
const SET_STICKER_BASE: string = 'pic/SET_STICKER_BASE';
const SET_STICKER_USER: string = 'pic/SET_STICKER_USER';
const ADD_STICKER_USER: string = 'pic/ADD_STICKER_USER';
const DEL_STICKER_USER: string = 'pic/DEL_STICKER_USER';
const SET_SELECTED_STICKER: string = 'pic/SET_SELECTED_STICKER';
const SET_SELECTED_STICKER_IDX: string = 'pic/SET_SELECTED_STICKER_IDX';


/* Action Functions */
export const setStickerBase = createAction(
  SET_STICKER_BASE,
  function prepare(stickers) {
    return { payload: { stickers }}
  }
);
export const setStickerUser = createAction(
  SET_STICKER_USER,
  function prepare(stickers) {
    return { payload: { stickers }}
  }
);
export const addStickerUser = createAction(
  ADD_STICKER_USER,
  function prepare(sticker) {
    return { payload: { sticker }}
  }
);
export const deleteStickerUser = createAction(
  DEL_STICKER_USER,
  function prepare(sid) {
    return { payload: { sid }}
  }
);
export const setSelectedSticker = createAction(
  SET_SELECTED_STICKER,
  function prepare(img: string) {
    return { payload: { img }}
  }
);
export const setSelectedStickerIdx = createAction(
  SET_SELECTED_STICKER_IDX,
  function prepare(idx: number, type: string) {
    return { payload: { idx, type }}
  }
);

/* Initial State */
interface state {
  stickerBase: any[],
  stickerUser: any[],
  selectedSticker: string,
  selectedStickerIdxBase: number,
  selectedStickerIdxUser: number
}
const initState: state = {
  // sticker
  stickerBase: [],
  stickerUser: [],
  selectedSticker: '',
  selectedStickerIdxBase: 0,
  selectedStickerIdxUser: 0,
}

/* Reducer */
const pic = createReducer(initState, (builder) => {
  builder
  .addCase(setStickerBase, (state, action) => {
    state.stickerBase = action.payload.stickers;
  })
  .addCase(setStickerUser, (state, action) => {
    state.stickerUser = action.payload.stickers;
  })
  .addCase(addStickerUser, (state, action) => {
    state.stickerUser = [ ...state.stickerUser, action.payload.sticker ];
  })
  .addCase(deleteStickerUser, (state, action) => {
    state.stickerUser = state.stickerUser.filter(item => item.sid !== action.payload.sid)
  })
  .addCase(setSelectedSticker, (state, action) => {
    state.selectedSticker = action.payload.img;
  })
  .addCase(setSelectedStickerIdx, (state, action) => {
    const { idx, type } = action.payload;
    type === '기본 스티커'
    ? state.selectedStickerIdxBase = idx
    : state.selectedStickerIdxUser = idx;
  })
});

export default pic;

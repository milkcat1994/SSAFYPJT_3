import { createAction, createReducer } from '@reduxjs/toolkit';

/* Action Types */
const SELECT_PICTURE: string = 'pic/SELECT_PICTURE';
const SET_RESULT_PUCTURE: string = 'pic/SET_RESULT_PICTURE';

// options
const SET_OPTION_TYPE: string = 'pic/SET_OPTION_TYPE';
const SET_OPTION_LEVEL: string = 'pic/SET_OPTION_LEVEL';

// face detection
const SET_FACE_AREA: string = 'pic/SET_FACE_AREA';
const SET_FACE_DETECTED: string = 'pic/SET_FACE_DETECTED';
const SET_SELECTED_FACE_IDX: string = 'pic/SET_SELECTED_FACE_IDX';


/* Action Functions */
export const selectPicture = createAction(
  SELECT_PICTURE,
  function prepare(picURL: string) {
    return { payload: { picURL } };
  }
);
export const setResultPicture = createAction(
  SET_RESULT_PUCTURE,
  function prepare(resultPicURL) {
    return { payload: { resultPicURL }}
  }
);
export const setOptionType = createAction(
  SET_OPTION_TYPE,
  function prepare(optionTypeIdx: number) {
    return { payload: { optionTypeIdx } };
  }
);
export const setOptionLevel = createAction(
  SET_OPTION_LEVEL,
  function prepare(optionLevel: number) {
    return { payload: { optionLevel } };
  }
);
export const setFaceDetected = createAction(
  SET_FACE_DETECTED,
  function prepare(faceDetected) {
    return { payload: { faceDetected } };
  }
);
export const setFaceArea = createAction(
  SET_FACE_AREA,
  function prepare(faceArea) {
    return { payload: { faceArea } };
  }
);
export const setSelectedFaceIdx = createAction(
  SET_SELECTED_FACE_IDX,
  function prepare(selectedFaceIdx) {
    return { payload: { selectedFaceIdx } };
  }
);

/* Initial State */
const optionTypeNames = ['pixel', 'blur', 'swap', 'sticker']

interface state {
  // img
  picURL: string,
  resultPicURL: string,

  // options
  optionType: string,
  optionTypeIdx: number,
  optionLevel: number,

  // face detection
  faceDetected: any[],
  faceArea: any[],
  selectedFaceIdx: any[],
}

const initState: state = {
  // img
  picURL: '',
  resultPicURL: '',

  // options
  optionType: 'pixel',
  optionTypeIdx: 0,
  optionLevel: 3,

  // face detection
  faceDetected: [],
  faceArea: [],
  selectedFaceIdx: [],
}

/* Reducer */
const pic = createReducer(initState, (builder) => {
  builder
  .addCase(selectPicture, (state, action) => {
    state.picURL = action.payload.picURL;
  })
  .addCase(setResultPicture, (state, action) => {
    state.resultPicURL = action.payload.resultPicURL
  })
  .addCase(setOptionType, (state, action) => {
    const idx = action.payload.optionTypeIdx;
    state.optionTypeIdx = idx;
    state.optionType = optionTypeNames[idx];
  })
  .addCase(setOptionLevel, (state, action) => {
    state.optionLevel = action.payload.optionLevel;
  })
  .addCase(setFaceDetected ,(state, action) => {
    state.faceDetected = action.payload.faceDetected;
  })
  .addCase(setFaceArea ,(state, action) => {
    state.faceArea = action.payload.faceArea;
  })
  .addCase(setSelectedFaceIdx ,(state, action) => {
    state.selectedFaceIdx = action.payload.selectedFaceIdx;
  })
});

export default pic;

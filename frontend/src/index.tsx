import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { Provider } from 'react-redux';
import {configureStore} from '@reduxjs/toolkit';
import rootReducer from './redux';

export const store = configureStore({reducer:rootReducer});
export type RootState = ReturnType<typeof rootReducer>;

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}><App /></Provider>
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
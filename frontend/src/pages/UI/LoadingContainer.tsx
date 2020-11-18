import React from 'react';

// components
import Loading from './Loading';

// redux
import { RootState } from '../../index';
import { useSelector } from 'react-redux';

function LoadingContainer() {
  // state
  const show = useSelector((state: RootState) => state.message.loadingShow);

  return  <Loading show={show} /> 
}

export default LoadingContainer;
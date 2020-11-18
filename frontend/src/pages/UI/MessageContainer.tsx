import React from 'react';

// components
import Message from './Message';

// redux
import { useDispatch, useSelector } from 'react-redux';
import { hideMessage } from '../../redux/modules/message';
import { RootState } from '../../index';


function MessageContainer() {
  const dispatch = useDispatch();

  // state
  const state = useSelector((state: RootState) => state.message);

  // methods
  const methods = {
    close() {
      dispatch(hideMessage());
    }
  }

  return <Message state={state} methods={methods} />;
}

export default MessageContainer;
import { combineReducers } from 'redux';
import auth from './modules/auth';
import pic from './modules/pic';
import message from './modules/message';
import modal from './modules/modal';
import sticker from './modules/sticker';
import friend from './modules/friend';

const reducers = combineReducers({
    auth,
    pic,
    sticker,
    message,
    modal,
    friend
});

export default reducers;

import axios from 'axios';
import { URLToBase64 } from '../util';

const AXIOS = axios.create({
  // baseURL: "http://127.0.0.1:8000/"
  baseURL: "http://k3a207.p.ssafy.io:8000/"
});

// 로드하는 데 시간이 걸리기 때문에 비동기 처리에 신경써야 함


const API = {

  // picture
  async uploadPic(picURL: string) {
    const img = await URLToBase64(picURL);
    const uid = sessionStorage.userId || '';
    return AXIOS({
      url: 'swap/upload/',
      method: 'POST',
      data: { 
        uid, img 
      }
    });
  },

  async fetchResult(picURL, optionType, optionlevel, stickerURL, targetFace) {
    const img = await URLToBase64(picURL);
    const sticker = await URLToBase64(stickerURL);

    return AXIOS({
      url: 'swap/result/',
      method: 'post',
      data: { 
        img, optionType, optionlevel, sticker, targetFace,
      }
    });
  },
  
  // stickers
  fetchStickerBase() {
    return AXIOS({
      url: 'sticker/all',
      method: 'get'
    })
  },
  fetchStickerUser() {
    const uid = sessionStorage.userId || '';
    return AXIOS({
      url: 'sticker/' + uid,
      method: 'get'
    })
  },
  async addSticker(item) {
    const { uid } = item;
    const img = await URLToBase64(item.img);

    return AXIOS({
      url: 'sticker/add/',
      method: 'post',
      data: { 
        uid, img
      }
    })
  },
  deleteSticker(sid) {
    return AXIOS({
      url: 'sticker/delete/' + sid,
      method: 'delete',
    })
  },

  // auth
  login(email, provider) {
    return AXIOS({
      url: 'user/login/',
      method: 'POST',
      data: {
          email: email,
          domain: provider,
      }
    })
  },
  deleteUser() {
    return AXIOS({
      url:`user/delete/${sessionStorage.userId}`,
      method: 'DELETE',
      data : {
        uid:`${sessionStorage.userId}`,
      }
    })
  },

  // friends
  addFriends(uid, fname, img) {
    return AXIOS({
      url: 'friends/add/',
      method: 'POST',
      data: {
          uid: uid,
          fname: fname,
          img: img,
      }
    })
  },
  addFriendsFace(kid, img) {
    return AXIOS({
      url: 'friends/add/face/',
      method: 'POST',
      data: {
          kid: kid,
          img: img,
      }
    })
  },
  deleteFriendsFace(fid) {
    return AXIOS({
      url: `friends/delete/face/${fid}/`,
      method: 'DELETE',
      data: {
          fid: fid,
      }
    })
  },
  deleteFriends(kid) {
    return AXIOS({
      url: `friends/delete/${kid}/`,
      method: 'DELETE',
      data: {
          kid: kid,
      }
    })
  },
  detailFriends(kid) {
    return AXIOS({
      url: `friends/detail/faces/${kid}/`,
      method: 'GET',
      data: {
          kid: kid,
      }
    })
  },
  updateFriendName(kid,fname) {
    return AXIOS({
      url: `friends/update/`,
      method: 'PUT',
      data: {
          kid: kid,
          fname:fname
      }
    })
  },
  updateFriendImg(kid,fid) {
    return AXIOS({
      url: `friends/update/img/`,
      method: 'PUT',
      data: {
          kid: kid,
          fid:fid
      }
    })
  },
  getFriendsList(uid) {
    return AXIOS({
      url: `friends/${uid}/`,
      method: 'GET',
      data: {
          uid: uid,
      }
    })
  },
  // 아래 signup, getUser는 샘플코드입니다.
  signup(data) {
    return AXIOS({
        url: 'rest-auth/registration/',
        method: 'post',
        data
    })
  },
  getUser() {
    return AXIOS({
      url: 'rest-auth/user/',
      method: 'get'
    })
  },
};

export default API;
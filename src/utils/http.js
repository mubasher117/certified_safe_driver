import axios from "axios";
import { appConfig } from "../config/app";
import { errorMessage, forceSignOut } from '../actions';
import Toast from 'react-native-toast-message';
import store from "../store";

const APP_PLATFORM = "Mobile";

export const request = axios.create({
  headers: {
    app_platform: APP_PLATFORM,
    app_version: 1,
  }
});

export function setupHttpConfig() {
  console.log('store.getState().userReducer.token', store.getState().userReducer.token);
  request.defaults.baseURL = appConfig.emailAuthAPIEndPoint;
  request.defaults.timeout = appConfig.defaultTimeout;
  axios.defaults.headers["Content-Type"] = "application/json";
  if (store.getState().userReducer.token) {
    request.defaults.headers['Authorization'] = `Bearer ${store.getState().userReducer.token}`
  }
  // you can add more default values for http requests here
}

export async function apiPost(endpoint, data) {
  try {
    console.log('apiPost :: calling ::', `${appConfig.emailAuthAPIEndPoint}${endpoint}`, 'with data', data)
    let res = await request.post(`${endpoint}`, data)
    if (res) {
      console.log(endpoint, '---res---:', res);
      return res
    }
  } catch (error) {
    console.log('API POST ERROR endpoint:', endpoint, ' || error:', error);
    return APIErrorHandler(error, endpoint);
  }
}

export async function apiGet(endpoint) {
  try {
    console.log('apiGet :: calling ::', `${appConfig.emailAuthAPIEndPoint}${endpoint}`)
    let res = await request.get(`${endpoint}`)
    if (res) {
      console.log(endpoint, '---res---:', res);
      return res
    }
  } catch (error) {
    console.log('API GET ERROR endpoint:', endpoint, ' || error:', error)
    return APIErrorHandler(error, endpoint)
  }
}

export async function apiPut(endpoint, data, stringify) {
  try {
    console.log('apiPut :: calling ::', `${appConfig.emailAuthAPIEndPoint}${endpoint}`, 'with data', data)
    let res = await request.put(`${endpoint}`, stringify ? data : JSON.stringify(data))
    if (res) {
      console.log(endpoint, '---res---:', res);
      return res
    }
  } catch (error) {
    console.log('API PUT ERROR endpoint:', endpoint, ' || error:', error);
    return APIErrorHandler(error, endpoint);
  }
}

export async function apiPatch(endpoint, data, stringify) {
  try {
    console.log('apiPatch :: calling ::', `${appConfig.emailAuthAPIEndPoint}${endpoint}`, 'with data', data)
    let res = await request.patch(`${endpoint}`, stringify ? data : JSON.stringify(data))
    if (res) {
      console.log(endpoint, '---res---:', res);
      return res
    }
  } catch (error) {
    console.log('API PATCH ERROR endpoint:', endpoint, ' || error:', error);
    return APIErrorHandler(error, endpoint);
  }
}


export async function apiDelete(endpoint) {
  try {
    console.log('apiDelete :: calling ::', `${appConfig.emailAuthAPIEndPoint}${endpoint}`)
    let res = await request.delete(`${endpoint}`)
    if (res) {
      console.log(endpoint, '---res---:', res);
      return res
    }
  } catch (error) {
    console.log('API DELETE ERROR endpoint:', endpoint, ' || error:', error)
    return APIErrorHandler(error, endpoint)
  }
}

function APIErrorHandler(error, endpoint) {
  // console.log('apiPost err', error.response)
  // console.log('error', error);
  // console.log('errorType', typeof error);
  console.log('error', Object.assign({}, error));
  // console.log('getOwnPropertyNames', Object.getOwnPropertyNames(error));
  // console.log('stackProperty', Object.getOwnPropertyDescriptor(error, 'stack'));
  // console.log('messageProperty', Object.getOwnPropertyDescriptor(error, 'message'));
  // console.log('stackEnumerable', error.propertyIsEnumerable('stack'));
  // console.log('messageEnumerable', error.propertyIsEnumerable('message'));
  // Object.getOwnPropertyNames(error).forEach(err => {
  //   console.log('err', err, ':', error[err])
  // });
  if (error.message == "Network Error") {
    errorMessage('No Internet');
    return false;
  } else if (error.code && error.code == 'ECONNABORTED') {
    errorMessage('Poor Internet Connection');
    return false;
  } else if (error.response && error.response.status && error.response.status == 403) {
    errorMessage(`${endpoint}\n${error}`);
    return { error: { ...error.response } };
  } else if (error.response && error.response.status && error.response.status == 401 && endpoint != '/api/v1/admin/login/token/') {
    console.log('session expired 401')
    errorMessage('Session Expired');
    forceSignOut();
    return false;
  } else if (error.response && error.response.status && error.response.status == 504) {
    errorMessage('504');
    return false;
  }
  // else if (error.response && error.response.status && error.response.status == 400 && endpoint == '/users') {
  //   return { data: error.response.data };
  // }
  else if (error.response) {
    return { error: { ...error.response } }
  } else {
    return { error }
  }
}

export function showToast(message, type = 'error', position = 'bottom') {
  Toast.show({
    type: type,
    position: position,
    text1: '',
    text2: message,
    visibilityTime: 4000,
    autoHide: true,
    topOffset: 30,
    bottomOffset: 40,
    onShow: () => { },
    onHide: () => { },
    onPress: () => { }
  });
}
import {
  SIGNIN_SUCCESS,
  SIGNOUT_SUCCESS,
  FETCH_USER_PROFILE,
} from './types';
import _ from 'lodash';
import store from '../store';
import NavigationService from '../navigation/NavigationService';
import { apiPost, apiGet, request, setupHttpConfig } from '../utils/http';
import { errorMessage } from './parent_actions';
import axios from 'axios';

export const signInWithEmailAndPasswordAction = ({ email, password }) => async (dispatch, getState) => {
  const data = {
    username: email,
    password,
  }
  let res = await apiPost('/api/v1/admin/login/token/', data);
  if (res && res.data) {
    dispatch({ type: SIGNIN_SUCCESS, payload: res.data });
    setupHttpConfig();
    // request.defaults.headers["Authorization"] = `Bearer ${res.data.access}`;
    // axios.defaults.headers["Authorization"] = `Bearer ${res.data.access}`;
    return true;
  } else if (res && res.error) {
    //handle error
    console.log('login error', res.error)
    if (res.error.status == 401 && res.error.data) {
      errorMessage('Invalid Credentials')
    } else {
      errorMessage('Something went wrong')
      // return false;
    }
    return false;
  }
};


export const fetchUserProfileAction = () => async (dispatch, getState) => {
  // return true; 
  let res = await apiGet('/api/v1/account/profile/');
  if (res && res.data) {
    dispatch({ type: FETCH_USER_PROFILE, payload: res.data });
    return res.data;
  } else if (res && res.error) {
    //handle error
    return false;
  } else {
    return false;
  }
};

export const forceSignOut = () => store.dispatch(signOutAction())
export const signOutAction = () => async (dispatch, getState) => {
  //TODO: google and facebook signout
  NavigationService.navigate('SigninScreen')
  setTimeout(() => {
    dispatch({ type: SIGNOUT_SUCCESS });
  }, 200);
};

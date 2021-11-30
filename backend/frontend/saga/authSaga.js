import { call, put, takeEvery } from 'redux-saga/effects';

import { AUTH, setAuthenticatedUser, setAuthError, getCurrentUser } from '../actions/authActions';
import { doLoginAPI, doGetUser } from '../services/authServices';

export function* handleLogin({ payload }) {
  const { response, error } = yield call(doLoginAPI, payload);
  console.log('response', response);
  if (response) {
    const { data } = response;
    yield put(getCurrentUser());
    yield put(setAuthenticatedUser(data));
  } else if (error) {
    const { status, data } = error.response;
    let msg = '';
    if (status >= 500) {
      msg = 'Internal server error';
    }
    if (status === 403) {
      msg = data;
    } else {
      msg = data.detail;
    }
    yield put(setAuthError(msg));
  } else if (response === undefined && error === undefined) {
    yield put(setAuthError('Server is down'));
  }
}

export function* handleGetUser() {
  const { response, error } = yield call(doGetUser);
  if (response) {
    const { data } = response;
    yield put({ type: AUTH.GET_USER_DETAILS_SUCCESS, response: data });
  } else if (error) {
    const { status, data } = error.response;
    let msg = '';
    if (status >= 500) {
      msg = 'Internal server error';
    } else {
      msg = data.non_field_errors[0];
    }
    yield put({ type: AUTH.GET_USER_DETAILS_ERROR, error: msg });
  } else if (response === undefined && error === undefined) {
    yield put({ type: AUTH.GET_USER_DETAILS_ERROR, error: 'server is down' });
  }
}

export function* watchHandleLogin() {
  yield takeEvery(AUTH.LOGIN, handleLogin);
  yield takeEvery(AUTH.GET_USER_DETAILS, handleGetUser);
}

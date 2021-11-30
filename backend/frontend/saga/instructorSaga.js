import { call, put, takeEvery } from 'redux-saga/effects';

import { INSTRUCTOR } from '../actions/instructorActions';
import { doGetInstructor, doPatchInstructor, doAddInstructor } from '../services/instructorServices';

export function* handleGetInstructors({ payload }) {
  const { response, error } = yield call(doGetInstructor, payload);
  if (response) {
    const { data } = response;
    yield put({ type: INSTRUCTOR.GET_INSTRUCTOR_SUCCESS, response: data });
  } else if (error) {
    const { status, data } = error.response;
    let msg = '';
    if (status >= 500) {
      msg = 'Internal server error';
    } else {
      msg = data.detail;
    }
    yield put({ type: INSTRUCTOR.GET_INSTRUCTOR_ERROR, error: msg });
  } else if (response === undefined && error === undefined) {
    yield put({ type: INSTRUCTOR.GET_INSTRUCTOR_ERROR, error: 'server is down' });
  }
}

export function* handlePatchInstructor({ payload }) {
  const { response, error } = yield call(doPatchInstructor, payload);
  if (response) {
    const { data } = response;
    yield put({ type: INSTRUCTOR.UPDATE_INSTRUCTOR_SUCCESS, response: data });
    yield put({ type: INSTRUCTOR.GET_INSTRUCTOR });
  } else if (error) {
    const { status, data } = error.response;
    let msg = '';
    if (status >= 500) {
      msg = 'Internal server error';
    } else {
      msg = data.detail;
    }
    yield put({ type: INSTRUCTOR.GET_INSTRUCTOR_ERROR, error: msg });
  } else if (response === undefined && error === undefined) {
    yield put({ type: INSTRUCTOR.GET_INSTRUCTOR_ERROR, error: 'server is down' });
  }
}

export function* handleAddInstructor({ payload }) {
  const { response, error } = yield call(doAddInstructor, payload);
  if (response) {
    const { data } = response;
    yield put({ type: INSTRUCTOR.ADD_INSTRUCTOR_SUCCESS, response: data });
    yield put({ type: INSTRUCTOR.GET_INSTRUCTOR });
  } else if (error) {
    const { status, data } = error.response;
    let msg = '';
    if (status >= 500) {
      msg = 'Internal server error';
    } else {
      msg = data.detail;
    }
    yield put({ type: INSTRUCTOR.ADD_INSTRUCTOR_ERROR, error: msg });
  } else if (response === undefined && error === undefined) {
    yield put({ type: INSTRUCTOR.ADD_INSTRUCTOR_ERROR, error: 'server is down' });
  }
}

export function* watchHandleGetInstructor() {
  yield takeEvery(INSTRUCTOR.GET_INSTRUCTOR, handleGetInstructors);
  yield takeEvery(INSTRUCTOR.UPDATE_INSTRUCTOR, handlePatchInstructor);
  yield takeEvery(INSTRUCTOR.ADD_INSTRUCTOR, handleAddInstructor);
}

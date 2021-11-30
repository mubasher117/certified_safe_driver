import { call, put, takeEvery } from 'redux-saga/effects';
import { toast } from 'react-toastify';

import { STUDENTS } from '../actions/studentsActions';
import { doGetStudents, doPatchStudent, doGetStudentReport, doPostStudent } from '../services/studentsService';

export function* handleGetStudents({ payload }) {
  const { response, error } = yield call(doGetStudents, payload);
  if (response) {
    const { data } = response;
    yield put({ type: STUDENTS.GET_STUDENTS_SUCCESS, response: data });
  } else if (error) {
    const { status, data } = error.response;
    let msg = '';
    if (status >= 500) {
      msg = 'Internal server error';
    } else {
      msg = data.detail;
    }
    yield put({ type: STUDENTS.GET_STUDENTS_ERROR, error: msg });
    toast(msg, { type: toast.TYPE.ERROR });
  } else if (response === undefined && error === undefined) {
    toast('Server is not responding');
    yield put({ type: STUDENTS.GET_STUDENTS_ERROR, error: 'server is down' });
  }
}
export function* handleGetStudentReport({ payload }) {
  const { response, error } = yield call(doGetStudentReport, payload);
  if (response) {
    const { data } = response;
    yield put({ type: STUDENTS.GET_STUDENT_REPORT_SUCCESS, response: data });
  } else if (error) {
    const { status, data } = error.response;
    let msg = '';
    if (status >= 500) {
      msg = 'Internal server error';
    } else {
      msg = data.detail;
    }
    yield put({ type: STUDENTS.GET_STUDENT_REPORT_ERROR, error: msg });
  } else if (response === undefined && error === undefined) {
    yield put({ type: STUDENTS.GET_STUDENT_REPORT_ERROR, error: 'server is down' });
  }
}

export function* handlePatchStudent({ payload }) {
  const { response, error } = yield call(doPatchStudent, payload);
  if (response) {
    const { data } = response;
    yield put({ type: STUDENTS.UPDATE_STUDENT_SUCCESS, response: data });
    yield put({ type: STUDENTS.GET_STUDENTS });
  } else if (error) {
    const { status, data } = error.response;
    let msg = '';
    if (status >= 500) {
      msg = 'Internal server error';
    } else {
      msg = data.detail;
    }
    yield put({ type: STUDENTS.UPDATE_STUDENT_ERROR, error: msg });
  } else if (response === undefined && error === undefined) {
    yield put({ type: STUDENTS.UPDATE_STUDENT_ERROR, error: 'server is down' });
  }
}

export function* handlePostStudent({ payload }) {
  const { response, error } = yield call(doPostStudent, payload);
  if (response) {
    const { data } = response;
    yield put({ type: STUDENTS.ADD_STUDENT_SUCCESS, response: data });
    yield put({ type: STUDENTS.GET_STUDENTS });
    toast('Student added successfully', { type: toast.TYPE.SUCCESS });
  } else if (error) {
    const { status, data } = error.response;
    let msg = '';
    if (status >= 500) {
      msg = 'Internal server error';
    } else {
      msg = data.detail;
    }
    yield put({ type: STUDENTS.ADD_STUDENT_ERROR, error: msg });
    toast(msg, { type: toast.TYPE.ERROR });
  } else if (response === undefined && error === undefined) {
    yield put({ type: STUDENTS.ADD_STUDENT_ERROR, error: 'server is down' });
  }
}

export function* watchHandleGetStudents() {
  yield takeEvery(STUDENTS.GET_STUDENTS, handleGetStudents);
  yield takeEvery(STUDENTS.UPDATE_STUDENT, handlePatchStudent);
  yield takeEvery(STUDENTS.GET_STUDENT_REPORT, handleGetStudentReport);
  yield takeEvery(STUDENTS.ADD_STUDENT, handlePostStudent);
}

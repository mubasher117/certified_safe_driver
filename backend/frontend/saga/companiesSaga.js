import { call, put, takeEvery } from 'redux-saga/effects';

import { COMPANIES } from '../actions/companiesActions';
import { doGetCompanies, doPatchCompany, doPostCompany } from '../services/companiesService';

export function* handleGetCompanies({ payload }) {
  const { response, error } = yield call(doGetCompanies, payload);
  if (response) {
    const { data } = response;
    yield put({ type: COMPANIES.GET_COMPANIES_SUCCESS, response: data });
  } else if (error) {
    const { status, data } = error.response;
    let msg = '';
    if (status >= 500) {
      msg = 'Internal server error';
    } else {
      msg = data.detail;
    }
    yield put({ type: COMPANIES.GET_COMPANIES_ERROR, error: msg });
  } else if (response === undefined && error === undefined) {
    yield put({ type: COMPANIES.GET_COMPANIES_ERROR, error: 'server is down' });
  }
}

export function* handlePatchCompany({ payload }) {
  const { response, error } = yield call(doPatchCompany, payload);
  if (response) {
    const { data } = response;
    yield put({ type: COMPANIES.UPDATE_COMPANY_SUCCESS, response: data });
    yield put({ type: COMPANIES.GET_COMPANIES });
  } else if (error) {
    const { status, data } = error.response;
    let msg = '';
    if (status >= 500) {
      msg = 'Internal server error';
    } else {
      msg = data.detail;
    }
    yield put({ type: COMPANIES.UPDATE_COMPANY_ERROR, error: msg });
  } else if (response === undefined && error === undefined) {
    yield put({ type: COMPANIES.UPDATE_COMPANY_ERROR, error: 'server is down' });
  }
}

export function* handlePostCompany({ payload }) {
  console.log('payload', payload);
  const { response, error } = yield call(doPostCompany, payload);
  if (response) {
    const { data } = response;
    yield put({ type: COMPANIES.ADD_COMPANY_SUCCESS, response: data });
    yield put({ type: COMPANIES.GET_COMPANIES });
  } else if (error) {
    const { status, data } = error.response;
    let msg = '';
    if (status >= 500) {
      msg = 'Internal server error';
    } else {
      msg = data.detail;
    }
    yield put({ type: COMPANIES.ADD_COMPANY_ERROR, error: msg });
  } else if (response === undefined && error === undefined) {
    yield put({ type: COMPANIES.ADD_COMPANY_ERROR, error: 'server is down' });
  }
}

export function* watchHandleGetCompanies() {
  yield takeEvery(COMPANIES.GET_COMPANIES, handleGetCompanies);
  yield takeEvery(COMPANIES.UPDATE_COMPANY, handlePatchCompany);
  yield takeEvery(COMPANIES.ADD_COMPANY, handlePostCompany);
}

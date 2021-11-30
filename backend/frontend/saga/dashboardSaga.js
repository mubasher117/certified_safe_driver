import { call, put, takeEvery } from 'redux-saga/effects';

import {
  setOnGoingTripsDetail,
  TRIP,
  setOnGoingError,
  REVIEWS,
  setReviewsStats,
  setReviewsErrors
} from '../actions/dashboardActions';
import { getOnGoingTrips, overAllReviews } from '../services/dashboardServices';

export function * handleGetOnGoingTrips () {
  const { response, error } = yield call(getOnGoingTrips);
  if (response) {
    const { data } = response;
    yield put(setOnGoingTripsDetail(data));
  } else if (error) {
    const { status, data } = error.response;
    let msg = '';
    if (status >= 500) {
      msg = 'Internal server error';
    } else {
      msg = data;
    }
    yield put(setOnGoingError(msg));
  } else if (response === undefined && error === undefined) {
    yield put(setOnGoingError('server is down'));
  }
}

export function * handleGetOverAllReviews () {
  const { response, error } = yield call(overAllReviews);
  if (response) {
    const { data } = response;
    yield put(setReviewsStats(data));
  } else if (error) {
    const { status, data } = error.response;
    let msg = '';
    if (status >= 500) {
      msg = 'Internal server error';
    } else {
      msg = data;
    }
    yield put(setReviewsErrors(msg));
  } else if (response === undefined && error === undefined) {
    yield put(setReviewsErrors('server is down'));
  }
}

export function * watchHandleGetOnGoingTrip () {
  yield takeEvery(TRIP.GET_ON_GOING, handleGetOnGoingTrips);
}

export function * watchHandleGetReviewStat () {
  yield takeEvery(REVIEWS.GET_REVIEWS_STATS, handleGetOverAllReviews);
}

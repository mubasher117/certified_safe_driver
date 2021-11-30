import { all } from 'redux-saga/effects';

import { watchHandleLogin } from './authSaga';
import { watchHandleGetCompanies } from './companiesSaga';
import { watchHandleGetOnGoingTrip, watchHandleGetReviewStat } from './dashboardSaga';
import { watchHandleGetStudents } from './studentSaga';
import { watchHandleGetInstructor } from './instructorSaga';

export default function* rootSaga() {
  yield all([
    // Auth
    watchHandleLogin(),

    // Dashboard
    watchHandleGetOnGoingTrip(),
    watchHandleGetReviewStat(),

    // Companies
    watchHandleGetCompanies(),

    // students
    watchHandleGetStudents(),

    // Instructor
    watchHandleGetInstructor(),
  ]);
}

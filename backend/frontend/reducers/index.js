import { combineReducers } from 'redux';

import authReducer from './authReducer';
import companiesReducer from './companiesReducer';
import dashboardReducer from './dashboardReducer';
import studentReducer from './studentsReducer';
import instructorReducer from './InstructorReducer';

const rootReducer = combineReducers({
  auth: authReducer,
  dashboard: dashboardReducer,
  companies: companiesReducer,
  students: studentReducer,
  instructor: instructorReducer,
});
export default rootReducer;

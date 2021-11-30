// import {
//   FETCH_USER_PROFILE,
// } from './types';
// import { apiPost, apiGet } from '../utils/http';

// export const fetchUserProfileAction = () => async (dispatch, getState) => {
//   let res = await apiGet('/users/profile');
//   if (res && res.data) {
//     dispatch({ type: FETCH_USER_PROFILE, payload: res.data });
//     return res.data;
//   } else if (res && res.error) {
//     //handle error
//     return false;
//   } else {
//     return false;
//   }
// };

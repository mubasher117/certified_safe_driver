export const AUTH = {
  LOGIN: 'LOGIN',
  SET_AUTH_USER: 'SET_AUTH_USER',
  REGISTER: 'REGISTER',
  AUTH_FAIL: 'AUTH_FAIL',
  CLEAR_SESSION: 'CLEAR_AUTH_SESSION',
  LOGOUT_USER: 'LOGOUT_USER',
  GET_USER_DETAILS: 'GET_USER_DETAILS',
  GET_USER_DETAILS_SUCCESS: 'GET_USER_DETAILS_SUCCESS',
  GET_USER_DETAILS_ERROR: 'GET_USER_DETAILS_ERROR',
};
const doLogin = payload => ({
  type: AUTH.LOGIN,
  payload,
});

const setAuthenticatedUser = payload => ({
  type: AUTH.SET_AUTH_USER,
  payload,
});

const setAuthError = error => ({
  type: AUTH.AUTH_FAIL,
  error,
});
const getCurrentUser = () => ({
  type: AUTH.GET_USER_DETAILS,
});

const logoutUser = () => {
  console.log('clearing details');
  localStorage.removeItem('user');
  document.cookie = 'csrftoken=; Max-Age=0';
  document.cookie = 'arp_scroll_position=; Max-Age=0';
  document.cookie = 'sessionid=; Max-Age=0';
  window.location.reload();
  return {
    type: AUTH.LOGOUT_USER,
  };
};

export { doLogin, setAuthenticatedUser, setAuthError, logoutUser, getCurrentUser };

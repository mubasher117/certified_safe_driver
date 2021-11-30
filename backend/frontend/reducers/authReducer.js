import { AUTH } from '../actions/authActions.js';

const initialState = {
  url: '/login',
  title: 'Login',
  user: null,
  userDetails: {},
  isAuthenticated: false,
  isLoading: false,
  error: '',
};

const AuthReducer = (state = initialState, action) => {
  switch (action.type) {
    case AUTH.LOGIN:
      return {
        ...state,
        isLoading: true,
        error: '',
      };
    case AUTH.SET_AUTH_USER:
      localStorage.setItem('user', JSON.stringify(action.payload));
      return {
        ...state,
        isLoading: false,
        // user: action.payload.user,
        token: action.payload.token,
        isAuthenticated: true,
      };

    case AUTH.AUTH_FAIL:
      return {
        ...state,
        isLoading: false,
        user: null,
        isAuthenticated: false,
        error: action.error,
      };
    case AUTH.GET_USER_DETAILS:
      return {
        ...state,
        error: '',
      };
    case AUTH.GET_USER_DETAILS_SUCCESS:
      return {
        ...state,
        isLoading: false,
        userDetails: action.response,
        error: '',
      };
    case AUTH.GET_USER_DETAILS_ERROR:
      return {
        ...state,
        isLoading: false,
        userDetails: {},
        error: action.error,
      };

    default:
      return state;
  }
};

export default AuthReducer;

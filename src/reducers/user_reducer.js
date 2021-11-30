import {
  SIGNIN_SUCCESS,
  SIGNOUT_SUCCESS,
  FETCH_USER_PROFILE,
} from '../actions/types';

const INITIAL_STATE = {
  userProfile: null,
  token: null,
  refreshToken: null,
};

export default function (state = INITIAL_STATE, action) {
  console.log('user_reducer.js : action', action);
  switch (action.type) {
    case SIGNIN_SUCCESS: {
      return { ...state, token: action.payload.access, refreshToken: action.payload.refresh_token };
    }
    case SIGNOUT_SUCCESS: {
      return { ...state, ...INITIAL_STATE };
    }
    case FETCH_USER_PROFILE: {
      return { ...state, userProfile: action.payload };
    }
    default:
      return state;
  }
}

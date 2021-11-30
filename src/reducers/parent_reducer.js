import { ERROR, CLEAR_ERROR, INFO, CLEAR_INFO, POPUP, CLEAR_POPUP, SHOW_SELECTOR, HIDE_SELECTOR } from '../actions/types';

const INITIAL_STATE = {
  errorMessage: '',
  infoMessage: '',
  errorAction: null,
  showPopup: false,
  popupChildren: null,
  showSelector:false,
  selectorChildren:null,
};

export default function (state = INITIAL_STATE, action) {
  switch (action.type) {
    case ERROR: {
      if (action.errorAction)
        return { ...state, errorMessage: action.payload, errorAction: action.errorAction };
      else
        return { ...state, errorMessage: action.payload, errorAction: null };
    }
    case CLEAR_ERROR: {
      return { ...state, errorMessage: '', errorAction: null };
    }
    case INFO: {
      console.log('error_reducer.js : INFO:: action.payload::', action.payload);
      return { ...state, infoMessage: action.payload };
    }
    case CLEAR_INFO: {
      return { ...state, infoMessage: '' };
    }
    case POPUP: {
      return { ...state, showPopup: action.payload, popupChildren: action.children };
    }
    case CLEAR_POPUP: {
      return { ...state, showPopup: action.payload, popupChildren: null };
    }
    case SHOW_SELECTOR: {
      return { ...state, showSelector: action.payload, selectorChildren: action.children };
    }
    case HIDE_SELECTOR: {
      return { ...state, showSelector: action.payload, selectorChildren: null };
    }
    default:
      return state;
  }
}

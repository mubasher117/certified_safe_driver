import { ERROR, CLEAR_ERROR, INFO, CLEAR_INFO, POPUP, CLEAR_POPUP, SHOW_SELECTOR, HIDE_SELECTOR } from './types';
import store from '../store';

export const errorMessage = (message, action, object) => store.dispatch(errorHandler(message, action, object))

export const errorHandler = (error, action, object) => (dispatch, getState) => {
  try {
    dispatch({ type: ERROR, payload: error, ErrorObject: object, errorAction: action || null });
  } catch (e) {
    console.log('ERROR in errorHandler, (irony LOL):', e.message);
  }
};

export const clearError = () => (dispatch, getState) => {
  try {
    dispatch({ type: CLEAR_ERROR, payload: '' });
  } catch (e) {
    console.log('ERROR in ClearError:', e.message);
  }
};

export const showPopup = (children) => store.dispatch(_showPopup(children))

export const _showPopup = (children) => (dispatch, getState) => {
  try {
    dispatch({ type: POPUP, payload: true, children });
  } catch (e) {
    console.log('ERROR in showPopup:', e.message);
  }
};

export const hidePopup = () => store.dispatch(_hidePopup())

export const _hidePopup = () => (dispatch, getState) => {
  try {
    dispatch({ type: CLEAR_POPUP, payload: false });
  } catch (e) {
    console.log('ERROR in hidePopup:', e.message);
  }
};

export const infoMessage = (message) => store.dispatch(infoHandler(message))

export const infoHandler = (info) => (dispatch, getState) => {
  console.log('called infohandler');
  //let data=Object.assign({},{message:info})
  try {
    dispatch({ type: INFO, payload: info });
  } catch (e) {
    console.log('ERROR in infoHandler:', e.message);
  }
};

export const clearInfo = () => (dispatch, getState) => {
  try {
    dispatch({ type: CLEAR_INFO, payload: '' });
  } catch (e) {
    console.log('ERROR in clearInfo:', e.message);
  }
};


export const showSelector = (children) => store.dispatch(_showSelector(children))

export const _showSelector = (children) => (dispatch, getState) => {
  try {
    dispatch({ type: SHOW_SELECTOR, payload: true, children });
  } catch (e) {
    console.log('ERROR in _showSelector:', e.message);
  }
};

export const hideSelector = () => store.dispatch(_hideSelector())

export const _hideSelector = () => (dispatch, getState) => {
  try {
    dispatch({ type: HIDE_SELECTOR, payload: false });
  } catch (e) {
    console.log('ERROR in _hideSelector:', e.message);
  }
};
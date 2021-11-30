import { createStore, compose, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import persistedReducers from '../reducers';

export default createStore(
  persistedReducers,
  {}, //state
  compose(
    applyMiddleware(thunk),
  )
);

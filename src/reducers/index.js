import { combineReducers } from 'redux';
import { persistReducer } from 'redux-persist';
import AsyncStorage from '@react-native-community/async-storage';
import userReducer from './user_reducer';
import parentReducer from './parent_reducer';
import listsReducer from './lists_reducer';
import eveluationFlowReducer from './eveluationflow_reducer';
import usersflowReducer from './usersflow_reducer';

const whitelist = [
  'userReducer', 'listsReducer', 'eveluationFlowReducer'
];

const rootReducerConfig = {
  key: 'CSD_Primary',
  storage: AsyncStorage,
  whitelist,
  //blacklist
};

const rootReducer = combineReducers({ userReducer, parentReducer, listsReducer, eveluationFlowReducer, usersflowReducer })

export default persistedReducers = persistReducer(rootReducerConfig, rootReducer);

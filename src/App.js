import React, { Component } from 'react';
import { View, StatusBar, Text, ScrollView, Dimensions, LogBox, AppState } from 'react-native';
import { persistStore } from 'redux-persist';
import { Provider } from 'react-redux'
import { PersistGate } from 'redux-persist/integration/react';
import Nav from './navigation';
import NavigationService from './navigation/NavigationService';
import store from './store'
import ParentWrapper from './components/ParentWrapper';
import { REDUX_STORE_VERSION, PLATFORM_IOS, } from './constants';
import AsyncStorage from '@react-native-community/async-storage';
import { setupHttpConfig } from './utils/http';

LogBox.ignoreLogs([
  'ReactNativeFiberHostComponent',
  'Remote debugger',
  'Animated',
  'Failed prop type: Invalid props.style key `forceFontSize`'
]);
// console.disableYellowBox = true;
let persist = null;

export default class App extends Component {
  state = {
    reHydrated: false,
  };

  async componentDidMount() {
    
    let currentReduxStoreVersion = await AsyncStorage.getItem('CURRENT_REDUX_STORE_VERSION');
    console.log('currentReduxStoreVersion', currentReduxStoreVersion)
    //HACK: to delete redux state.
    // persist = await persistStore(store, null).purge();

    if (currentReduxStoreVersion != REDUX_STORE_VERSION) {
      console.log('store version changed');
      persist = await persistStore(store, null).purge();
      await AsyncStorage.setItem('CURRENT_REDUX_STORE_VERSION', REDUX_STORE_VERSION);
      persist = await persistStore(store, null, async () => {
        this.setState({ reHydrated: true }, () => {
          setupHttpConfig();
          console.log('store', store.getState())
        });
      });
    } else {
      persist = await persistStore(store, null, async () => {
        this.setState({ reHydrated: true }, () => {
          setupHttpConfig();
          console.log('store', store.getState())
        });
      });
    }
  }

  render() {
    if (!this.state.reHydrated) {
      return (
        null
        // <View style={{ flex: 1, backgroundColor: 'pink' }} />
      );
    }

    return (
      <Provider store={store}>
        <PersistGate loading={null} persistor={persist}>
          <ParentWrapper>
            <StatusBar barStyle={'light-content'} translucent={true} backgroundColor='transparent' />
            <Nav ref={navigatorRef => { NavigationService.setTopLevelNavigator(navigatorRef); }} />
          </ParentWrapper>
        </PersistGate>
      </Provider>
    );
  }
}
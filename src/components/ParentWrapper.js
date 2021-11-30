import React from "react";
import { Animated, LayoutAnimation, NativeModules, SafeAreaView, StatusBar, TouchableOpacity, TouchableWithoutFeedback, View, Image, ImageBackground, ActivityIndicator } from 'react-native';
import { connect } from "react-redux";
import { clearError, clearInfo, clearSuccess, hidePopup, fetchUserProfileAction, updateTabChangeErrorMessage, updateLocalUserProfileWithDataAction, expireToken, showPopup, errorMessage, successMessage, hideSelector, showSelector } from '../actions';
import { SCREEN_HEIGHT, STATUSBAR_HEIGHT, VIDEO_CROSS_ICON, ERROR_CROSS_ICON, SUCCESS_CHECK_ICON, SCREEN_WIDTH, PLATFORM_IOS, isIPhoneX, LOCATION_ICON, tapjoy, RIBBON_ICON, IS_TAB } from '../constants';
import store from "../store";
import * as colors from '../styles/colors';
import Text from './Text';
import _, { has } from 'lodash';
import { apiGet, apiPost, request } from "../utils/http";
import Modal from 'react-native-modal';
import Draggable from 'react-native-draggable';
import PopupBase from "./PopupBase";
import moment from 'moment'
import { scale } from "../utils/scale";
import Toast from 'react-native-toast-message';
import { dataParser, dataModalMaker, prodsDataModalMaker } from "../utils/function";
import Header from "./Header";
import { WebView } from 'react-native-webview';
import BTWTest from '../screens/evaluation/preview/BTWTest'
import { Loader } from ".";
const { UIManager } = NativeModules;
UIManager.setLayoutAnimationEnabledExperimental &&
  UIManager.setLayoutAnimationEnabledExperimental(true)

let timeOut = null;
let infoAutoHideTime = 4000;
let ANIMATION_DURATION = 1000;
class ParentWrapper extends React.Component {

  state = {
    showError: false,
    showInfo: false,
    _animated: new Animated.Value(SCREEN_HEIGHT),
    showDeviceInfo: false,
    showPreview: false,
    loading: false
  }

  generateHash() {
    return new Promise((resolve) => {
      setTimeout(() => {
        let k = 0;
        for (let i = 0; i < 1000000000; i++) {
          let j = i * i * i * i * i * i * i * i;
          // console.log('j & i: ', j, i);
        }
        resolve(k);
      }, 0)
    })
  }

  async componentDidMount() {
    this.props.clearError()
    this.props.clearInfo()
    hidePopup();
    hideSelector();
  }

  _showError = () => {
    LayoutAnimation.configureNext(
      LayoutAnimation.create(250, 'easeInEaseOut', 'opacity')
    );
    this.setState({ showError: true })
  }

  _hideError = () => {
    LayoutAnimation.configureNext(
      LayoutAnimation.create(250, 'easeInEaseOut', 'opacity')
    );
    this.setState({ showError: false }, () => {
      console.log('errorAction', this.props.errorAction);
      if (typeof (this.props.errorAction) == 'function')
        this.props.errorAction();

      this.props.clearError();
    })
  }

  _showInfo = () => {
    timeOut = setTimeout(this._hideInfo, infoAutoHideTime);
    Animated.timing(this.state._animated, {
      toValue: 0,
      duration: ANIMATION_DURATION,
    }).start();
    this.setState({ showInfo: true })
  }

  _hideInfo = () => {
    clearTimeout(timeOut);
    Animated.timing(this.state._animated, {
      toValue: SCREEN_HEIGHT,
      duration: ANIMATION_DURATION * 2,
    }).start(() => this.setState({ showInfo: false }, () => this.props.clearInfo()));
  }

  componentDidUpdate(prevProps, prevState) {
    if (this.props.error !== null && this.props.error != '' && (prevState.showError == false && this.state.showError == false)) {
      this._showError();
    }
    if (this.props.info !== null && this.props.info != '' && (prevState.showInfo == false && this.state.showInfo == false)) {
      this._showInfo();
    }
  }

  _renderErrorHandler = () => {
    return (
      <View style={{ position: 'absolute', width: '100%', height: '100%', backgroundColor: 'rgba(0,0,0,0.2)', alignItems: 'center', justifyContent: 'center' }}>
        <View
          // colors={[colors.APP_BACKGROUND_COLOR, colors.APP_BACKGROUND_COLOR]}
          style={{ backgroundColor: 'rgba(192,192,192,0.95)', borderRadius: 10, width: '70%', minHeight: (SCREEN_HEIGHT / 7), maxHeight: SCREEN_HEIGHT / 1.5, justifyContent: 'space-between', alignItems: 'center' }}>
          <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
            <Text style={{ color: 'black', fontSize: 17, margin: 5, textAlign: 'center' }}>{this.props.error}</Text>
          </View>
          <TouchableWithoutFeedback onPress={this._hideError}>
            <View style={{ width: '100%', backgroundColor: 'transparent', borderTopWidth: 1, borderTopColor: 'gray', padding: 0, justifyContent: 'center', alignItems: 'center' }}>
              <Text style={{ color: 'rgb(46,125,246)', fontSize: 18, margin: 10, fontWeight: '500' }}>OK</Text>
            </View>
          </TouchableWithoutFeedback>
        </View>
      </View>
    )
  }

  _renderSelector = () => {
    const { selectorChildren, showSelector } = this.props
    return (
      <Modal
        isVisible={showSelector}
        onBackdropPress={hideSelector}
        style={{
          padding: 0,
          margin: IS_TAB ? scale(30) : scale(15),
          marginVertical: scale(50),
          // marginTop: IS_TAB ? SCREEN_HEIGHT / 3 : 0,
          justifyContent: 'center',
        }}
      >
        <View style={{ flex: 1, backgroundColor: 'white', borderRadius: 20 }}>
          {selectorChildren}
        </View>
      </Modal>
    )
  }
  render() {
    return (
      <View style={{ flex: 1, backgroundColor: 'transparent' }}>
        {this.props.children}
        {/* <SafeAreaView style={{flex:1}}> */}
        <Animated.View style={[{ transform: [{ translateX: this.state._animated }] }, { position: 'absolute', width: '100%', flex: 1, top: STATUSBAR_HEIGHT * 2 }]}>
          <TouchableWithoutFeedback style={{ flex: 1 }} onPress={this._hideInfo}>
            <SafeAreaView
              style={{ flex: 1, backgroundColor: 'transparent', justifyContent: 'flex-end', alignItems: 'flex-end', }}>
              <View style={{ flex: 1, width: '70%', marginRight: -3, borderTopLeftRadius: 15, borderBottomLeftRadius: 15, backgroundColor: colors.APP_DARK_GRAY_COLOR, borderColor: colors.APP_BORDER_GRAY_COLOR, borderRightColor: colors.APP_DARK_GRAY_COLOR, borderWidth: 2, justifyContent: 'center', alignItems: 'center', }}>
                <Text style={{ color: colors.FONT_YELLOW_COLOR, fontSize: 13, margin: 3, textAlign: 'center' }}>{this.props.info}</Text>
              </View>
            </SafeAreaView>
          </TouchableWithoutFeedback>
        </Animated.View>
        {/* </SafeAreaView> */}
        {this._renderSelector()}
        {!!this.props.showPopup &&
          <View style={{ position: 'absolute', width: '100%', height: '100%', backgroundColor: 'rgba(0,0,0,0.7)', alignItems: 'center', justifyContent: 'center' }}>
            {this.props.popupChildren}
          </View>
        }

        {!!this.state.showError && this._renderErrorHandler()}
        {__DEV__ &&
          <Draggable
            x={-SCREEN_WIDTH + 80} y={SCREEN_HEIGHT - 200}
            // x={10} y={ 200}
            onShortPressRelease={() => this.setState({ showDeviceInfo: !this.state.showDeviceInfo })}
          >
            <View style={{
              // position: 'absolute', bottom: 10, left: 0, right: 0,
              padding: 10,
              borderRadius: 20,
              backgroundColor: 'skyblue', width: SCREEN_WIDTH - 20, flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between'
            }}>
              <View style={{ flex: 1 }}>
                <View style={{ flexDirection: 'row', justifyContent: 'space-between', }}>
                  <TouchableOpacity onPress={() => {
                    console.log('store', store.getState());
                  }}>
                    <Text>store</Text>
                  </TouchableOpacity>

                  {/* {this.state.loading ? (
                    // <ActivityIndicator />
                    <Loader />
                  ) : (
                    <TouchableOpacity
                      onPress={async() => {
                        // requestAnimationFrame(async() => {
                          this.setState({ loading: true });
                        //some expensive operation
                        const hash = await this.generateHash()
                        setTimeout(() => {
                          this.setState({ loading: false });
                        }, 1000);
                        // })
                      }}>
                      <Text>loading</Text>
                    </TouchableOpacity>
                  )} */}

                  <TouchableOpacity onPress={() => { errorMessage('test msg') }}>
                    <Text>show error</Text>
                  </TouchableOpacity>
                  {/* <TouchableOpacity onPress={() => console.log('store', store.getState())}>
                    <Text>store</Text>
                  </TouchableOpacity> */}

                  <TouchableOpacity onPress={async () => {
                    // let res = await apiGet('/api/v1/account/profile/')
                    // let res = await apiGet('/api/v1/instructions/class_p/class_a/')
                    // console.log('btw instructions', res)
                    //  res = await apiGet('/api/v1/instructions/pretrips/class_a/')
                    // console.log('pretrips instructions', res)
                    //  res = await apiGet('/api/v1/instructions/swp/')
                    // console.log('swp instructions', res)
                    // res = await apiGet('/api/v1/instructions/vrt/')
                    // console.log('vrt instructions', res)

                    // let _modified = await dataParser('', 'btw')

                    // let _modified = await dataModalMaker('/api/v1/students/11/tests/10/pretrips/bus/', 'pre_trip_bus')
                    // let _modified = await dataModalMaker('', 'swp')
                    let _modified = await dataModalMaker('api/v1/students/33/tests/80/vrt/', 'vrt')
                    console.log('modified', _modified)
                    // // // // // return false;

                    let js = JSON.stringify(_modified)
                    console.log('json', js)
                    // let data = await apiGet('/api/v1/notes/20/')
                    // let data = await apiGet('/api/v1/students/5/tests/')
                    // // let data = await apiGet('/api/v1/swp-list/65/')
                    // console.log('test data', data)
                    //  data = await apiGet('/api/v1/students/5/tests/2/class_p/bus')
                    // let data = await apiGet('/api/v1/students/5/report/')
                    // console.log('info data', data)
                    // this.props.updateTabChangeErrorMessage(false)
                    // this.setState({ showPreview: true })
                    //   let data=[
                    //     ['Shanghai', 24.2],
                    //     ['Beijing', 20.8],
                    //     ['Karachi', 14.9],
                    //     ['Shenzhen', 13.7],
                    //     ['Guangzhou', 13.1],
                    //     ['Istanbul', 12.7],
                    //     ['Mumbai', 12.4],
                    //     ['Moscow', 12.2],
                    //     ['São Paulo', 12.0],
                    //     ['Delhi', 11.7],
                    //     ['Kinshasa', 11.5],
                    //     ['Tianjin', 11.2],
                    //     ['Lahore', 11.1],
                    //     ['Jakarta', 10.6],
                    //     ['Dongguan', 10.6],
                    //     ['Lagos', 10.6],
                    //     ['Bengaluru', 10.3],
                    //     ['Seoul', 9.8],
                    //     ['Foshan', 9.3],
                    //     ['Tokyo', 9.3]
                    // ]
                    // console.log('data', data)

                  }}>
                    <Text>test</Text>
                  </TouchableOpacity>
                </View>
                {this.state.showDeviceInfo && <View style={{ borderTopWidth: 2, marginTop: 5 }}>
                  <Text>dev info</Text>
                  <Text>HEIGHT : {SCREEN_HEIGHT}</Text>
                  <Text>WIDTH : {SCREEN_WIDTH}</Text>
                  <Text>RATIO = {SCREEN_HEIGHT / SCREEN_WIDTH}</Text>
                </View>}
              </View>
              <Image source={require('../assets/icons/move.png')} style={{ width: 30, height: 30 }} />
            </View>
          </Draggable>}
        <Toast ref={(ref) => Toast.setRef(ref)} />
        <Modal
          animationType="slide"
          visible={this.state.showPreview}
          onRequestClose={() => { }}>
          <View style={{ flex: 1 }}>
            <Header>
              <TouchableOpacity onPress={() => this.setState({ showPreview: false })}>
                <Text style={{ marginLeft: 20, fontSize: 16 }}>{'Close'}</Text>
              </TouchableOpacity>

              <Text>Preview</Text>
              <Text>Email</Text>

            </Header>

            <WebView
              // source={{ html: PAS(BTWModal, this.state, eveluationFlowReducer.student_info) }}
              // source={{ html: BTW(BTWModal, this.state, eveluationFlowReducer.student_info, eveluationFlowReducer.company_info, eveluationFlowReducer.selectedTestInfo,) }}
              source={{ html: BTWTest() }}
              ref={ref => { this.WebView = ref; }}
              javaScriptEnabled={true}
              domStorageEnabled={true}
              startInLoadingState={true}
            />
          </View>
        </Modal>
      </View>
    );
  }
}

const mapStateToProps = state => {
  // console.log("state wrapper ", state.parentReducer);
  return {
    error: state.parentReducer.errorMessage,
    errorAction: state.parentReducer.errorAction,
    info: state.parentReducer.infoMessage,
    showPopup: state.parentReducer.showPopup,
    popupChildren: state.parentReducer.popupChildren,
    showSelector: state.parentReducer.showSelector,
    selectorChildren: state.parentReducer.selectorChildren,
    token: state.userReducer.token,
    store: state,
  };
};

export default connect(
  mapStateToProps,
  { clearError, clearInfo, updateTabChangeErrorMessage }
)(ParentWrapper);
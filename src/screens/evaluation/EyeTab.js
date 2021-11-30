import React from 'react';
import { StatusBar, ScrollView, TouchableOpacity, Alert, View } from 'react-native';
import { connect } from 'react-redux';
import { Footer, ScreenWrapper, EvaluationField, Selector, Text } from '../../components';
import SplashScreen from 'react-native-splash-screen'
import { errorMessage, fetchUserProfileAction, updateTabChangeErrorMessage, showPopup, showSelector } from '../../actions';
import { PLATFORM_IOS, SCREEN_HEIGHT, SCREEN_WIDTH } from '../../constants';
import Svg, { G, Path, TSpan } from "react-native-svg"
import { scale } from '../../utils/scale';
import EyeTracker from '../../components/EyeTracker'
import { apiGet, apiPost, apiPatch } from '../../utils/http';
import moment from 'moment'
import { getDataDiff } from '../../utils/function';
import ViewShot from "react-native-view-shot";
import Share from 'react-native-share';
import AsyncStorage from '@react-native-community/async-storage';

class EyeTab extends React.Component {
  // constructor(props) {
  //   super(props);
  //   this.eye = React.createRef();
  // }
  eye = React.createRef();
  state = {
    start_time: null,
    stop_time: null,
  };

  async componentDidMount() {
    this.getEye();
  }

  getEye = async () => {
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/eye/`,
    );
    console.log(`getEye res: `, res);
    if (res && res.data) {
      this.setState({
        start_time: res.data.start_time,
        stop_time: res.data.stop_time,
        eye_actions: res.data.eye_actions,
        apiData: {...res.data},
      });
      if (res.data.eye_actions) this.eye.current.loadData(res.data.eye_actions);
    }
    return true;
  };

  componentDidUpdate(prevProps, prevState) {
    if (
      this.props.shown &&
      prevProps.tabChangeErrorMessage == this.props.tabChangeErrorMessage
    ) {
      const isDiff = getDataDiff({...this.state.apiData}, this.state);
      console.log('isDiff Info', isDiff);
      if (isDiff) {
        if (this.props.tabChangeErrorMessage == false)
          this.props.updateTabChangeErrorMessage(
            'Please save or discard your changes',
          );
      } else {
        if (this.props.tabChangeErrorMessage !== false)
          this.props.updateTabChangeErrorMessage(false);
      }
    }
  }

  shareImg = async () => {
    this.refs.viewShot.capture().then(async (uri) => {
      console.log('do something with ', uri);
      await Share.open({
        url: `${PLATFORM_IOS ? '' : 'file://'}${uri}`,
        title: 'Share PDF',
      });
    });
    // console.log("do something with ", img);
  };

  takeScreenShot = () => {
    alert("Screenshot Captured");
    this.refs.viewShot.capture().then(async (uri) => {
      console.log(uri)
      const jsonValue = JSON.stringify({uri});
      AsyncStorage.setItem('@storage_Key', jsonValue).then((val) => {
        console.log('saving:  ', val);
        AsyncStorage.getAllKeys().then((keys) => {
          console.log('keys: , ', keys);
          AsyncStorage.getItem('@storage_Key').then((valR) =>
            console.log('retrieving: , ', valR),
          );
        });
      });
    });
  };

  saveEye = async () => {
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    const {start_time, stop_time} = this.state;
    const eye_actions = this.eye.current.storeData();
    let data = {
      eye_actions,
      start_time,
      stop_time,
    };
    let res = await apiPatch(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/eye/`,
      data,
      true,
    );
    // console.log('saveEye res', res)
    if (res && res.data) {
      this.setState({
        start_time: res.data.start_time,
        stop_time: res.data.stop_time,
        eye_actions: res.data.eye_actions,
        apiData: {...res.data},
      });
    }
    return true;
  };

  render() {
    const show = {flex: 1, height: undefined};
    const hide = {flex: 0, height: 0};
    const {eveluationFlowReducer} = this.props;
    const {
      company_info,
      student_info,
      instructor_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    const {start_time, stop_time} = this.state;
    return (
      <>
        <ScreenWrapper parentStyle={this.props.shown ? show : hide}>
          <ViewShot
            style={{flex: 1}}
            ref="viewShot"
            // options={{format: 'png', quality: 0.9}}
            options={{ result: "base64" }} 
            >
            <View
              style={{
                paddingHorizontal: 20,
                paddingTop: 10,
                flexDirection: 'row',
                justifyContent: 'space-between',
              }}>
              <Text>{company_info && company_info?.name}</Text>
              <Text>
                {student_info &&
                  `${student_info?.first_name} ${student_info?.last_name}`}
              </Text>
            </View>
            <EyeTracker
              ref={this.eye}
              onUpdate={(data) => {
                this.setState({eye_actions: data});
              }}
            />
            <View
              style={{flexDirection: 'row', justifyContent: 'space-evenly'}}>
              <View style={{justifyContent: 'center', alignItems: 'center'}}>
                <View style={{padding: 4, marginBottom: 5, borderWidth: 1}}>
                  <Text>{start_time ? start_time : '00:00'}</Text>
                </View>
                <TouchableOpacity
                  disabled={start_time && start_time != '00:00'}
                  onPress={() =>
                    this.setState({start_time: moment().format('HH:mm')})
                  }>
                  <Text style={{color: start_time ? 'gray' : 'black'}}>
                    Start
                  </Text>
                </TouchableOpacity>
              </View>
              <View style={{justifyContent: 'center', alignItems: 'center'}}>
                <View style={{padding: 4, marginBottom: 5, borderWidth: 1}}>
                  <Text>{selected_test?.created.split('T')[0]}</Text>
                </View>
              </View>
              <View style={{justifyContent: 'center', alignItems: 'center'}}>
                <View style={{padding: 4, marginBottom: 5, borderWidth: 1}}>
                  <Text>{stop_time ? stop_time : '00:00'}</Text>
                </View>
                <TouchableOpacity
                  // disabled={start_time}
                  onPress={() =>
                    this.setState({stop_time: moment().format('HH:mm')})
                  }
                  // onPress={() => this.eye.current.loadData(["follow_time", "intersections", "left_mirror", "gauges", "follow_time", "intersections", "left_mirror", "gauges", "follow_time", "follow_time", "follow_time", "follow_time",])}
                >
                  <Text>Stop</Text>
                </TouchableOpacity>
              </View>
              <TouchableOpacity
                style={{position: 'absolute', right: 23}}
                onPress={() =>
                  this.setState(
                    {stop_time: '00:00', start_time: '00:00', eye_actions: []},
                    () => this.eye.current.loadData([]),
                  )
                }>
                <Text>Clear</Text>
              </TouchableOpacity>
            </View>
          </ViewShot>
        </ScreenWrapper>
      </>
    );
  }
}

const mapStateToProps = state => {
  return {
    userReducer: state.userReducer,
    eveluationFlowReducer: state.eveluationFlowReducer,
    tabChangeErrorMessage: state.eveluationFlowReducer.tabChangeErrorMessage,
  };
};

export default connect(mapStateToProps, { fetchUserProfileAction, updateTabChangeErrorMessage }, null, { forwardRef: true })(EyeTab);
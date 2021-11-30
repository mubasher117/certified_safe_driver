import React from 'react';
import {
  View,
  TouchableOpacity,
  Image,
  Modal,
  Alert,
  Linking,
} from 'react-native';
import {KeyboardAwareScrollView} from 'react-native-keyboard-aware-scroll-view';
import {connect} from 'react-redux';
import {
  Text,
  Loader,
  ScreenWrapper,
  EvaluationField,
  Evaluation7OptionField,
  DateTimePicker,
  Header,
  SignaturePicker,
  Footer,
  Selector,
} from '../../components';
import SplashScreen from 'react-native-splash-screen';
import {
  fetchUserProfileAction,
  updateTabChangeErrorMessage,
  hideSelector,
  showPopup,
  showSelector,
  setMapData,
} from '../../actions';
import {
  PLATFORM_IOS,
  CALENDAR_ICON,
  PLAY_ICON,
  PAUSE_ICON,
  EXPORT_ICON,
  PLUS_ICON,
  CLOSE_ICON,
  INFO_BLUE_ICON,
} from '../../constants';
import {BTWModalA} from '../../utils/BTWModalA';
import {BTWModalB} from '../../utils/BTWModalB';
import {BTWModalC} from '../../utils/BTWModalC';
import {BTWModalD} from '../../utils/BTWModalD';
// import { BTWModalBUS } from '../../utils/BTWModalBUS';
import {BTWModalBUS1} from '../../utils/BTWModalBUS1';
import _, {isNumber} from 'lodash';
import * as colors from '../../styles/colors';
import {counterToAlpha, getObjectDiff, getDataDiff} from '../../utils/function';
import {apiPut, apiGet, apiPatch} from '../../utils/http';
import {scale} from '../../utils/scale';
import {WebView} from 'react-native-webview';
// import PRETRIP from './preview/'
import ActionSheet from 'react-native-actionsheet';
import BTW from './preview/BTWPreviewHTML';
import {PasDataModals} from '../../utils/PasDataModals';
import NavigationService from '../../navigation/NavigationService';
import RNHTMLtoPDF from 'react-native-html-to-pdf';
import moment from 'moment';
import Share from 'react-native-share';
import AsyncStorage from '@react-native-community/async-storage';
// import PAS from './preview/PASPreviewHTML'

let _class = 'class_a';
let BTWModal = BTWModalA;
let sectionPosition = {};
// let map_data={
//   leftWides: [],
//   leftOks: [],
//   leftShorts: [],
//   rightWides: [],
//   rightOks: [],
//   rightShorts: [],
//   map_screenshot_url:'', //base 64
// }
// [
//   {latitude:'0.0', longitude:'0.0'}
// ]

class BTWTab extends React.Component {
  state = {
    sections: [],
    // ...BTWModal,
    mounting: true,
    showPreview: false,
    isClassSelected: false,
    showPreview: false,
    start_time: false,
    end_time: false,
    totalPointsReceived: 0,
    totalPossiblePoints: 0,
    totalEffPercentage: 0,
    apiData: {},
    instructions: {},
    map_screenshot_img: '',
  };

  async componentDidMount() {
    setTimeout(() => {
      this._classActionSheet.show();
    }, 500);
    // if (__DEV__) {
    //   this.setState({ isClassSelected: true }, this.populateForm)
    // }
  }

  scrolSectionHandler = (num) => {
    console.log(
      'this.myScroll: ',
      num,
      sectionPosition[num.key],
      this.myScroll,
    );
    this.myScroll.scrollToPosition(0, sectionPosition[num.key]);
  };

  componentDidUpdate(prevProps, prevState) {
    if (
      this.props.eveluationFlowReducer.mapData !== null &&
      this.props.eveluationFlowReducer.mapData !=
        prevProps.eveluationFlowReducer.mapData
    ) {
      const {mapData} = this.props.eveluationFlowReducer;
      let formatedMapData = {...mapData};
      delete formatedMapData['map_screenshot_url'];
      console.log('formatedMapData', formatedMapData);
      console.log('mapData', mapData);

      this.setState({
        map_data: JSON.stringify(formatedMapData),
        map_image: mapData.map_screenshot_url,
      });
    }

    if (
      this.props.shown &&
      prevProps.tabChangeErrorMessage == this.props.tabChangeErrorMessage
    ) {
      const isDiff = getDataDiff({...this.state.apiData}, this.state);
      console.log('isDiff BTW', isDiff);
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

  populateForm = (clear) => {
    let state = {};
    state.sections = [];
    _.forEach(BTWModal, (level1Val, level1Key) => {
      let level2State = null;
      if (
        level1Val &&
        level1Val.value === null &&
        level1Val.value !== undefined
      ) {
        //fields with no nesteds
        //  console.log('nulls keys', level1Val.value);
      } else {
        state.sections.push({
          id: level1Key,
          name: level1Val.title,
          key: level1Key,
        });
        level2State = {};
        // console.log('undefined keys', level1Val);
        _.forEach(level1Val, (val, level2Key) => {
          if (level2Key !== 'key' && level2Key !== 'title')
            level2State[level2Key] = val?.value;
        });
      }
      state[level1Key] = level2State;
    });
    console.log('state', state);
    this.setState({...state, start_time: null, end_time: null}, () => {
      if (!clear) this.getData();
    });
  };

  getData = async () => {
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/btw/${_class}/`,
    );
    console.log('btw res', res);
    let instructions = await apiGet(`/api/v1/instructions/btw/${_class}/`);

    if (res && res.data && instructions && instructions.data) {
      console.log('data', res.data);
      let instructionsObjectified = {};
      instructions.data.forEach((_instruction) => {
        instructionsObjectified[_instruction.field_name] =
          _instruction.instruction;
      });
      console.log('btw instructionsObjectified', instructionsObjectified);
      let apiData = res.data;
      _.forEach(apiData, (level1Val, _state) => {
        _.forEach(level1Val, (value, level2Key) => {
          if (
            level2Key == `btw` ||
            level2Key == 'id' ||
            level2Key == 'created' ||
            level2Key == 'updated' ||
            level2Key == 'points_received' ||
            level2Key == 'possible_points'
          )
            delete apiData[_state][level2Key];
        });
      });
      this.setState({
        ...res.data,
        apiData: res.data,
        instructions: instructions.data,
        mounting: false,
      });

      if (res && res.data && res.data.map_data && res.data.map_image) {
        let parsedMapData = JSON.parse(res.data.map_data);
        console.log('parsedMapData', parsedMapData);
        this.props.setMapData({
          ...parsedMapData,
          map_screenshot_url: res.data.map_image,
        });
      } else {
        this.props.setMapData(null);
      }
    } else {
      this.setState({mounting: false});
    }
    return true;
  };

  saveBTW = async () => {
    if (this.state.mounting) return;
    // console.log('state', this.state)
    // return;
    //TODO: how to upload signature

    const isDiff = getDataDiff({...this.state.apiData}, this.state, true);
    if (!isDiff) {
      return;
    }
    //only update what is changed
    let newState = {};
    console.log('isDiff', isDiff);
    isDiff.forEach((key) => {
      // if (key == "start_time") {
      //   console.log('start_time: ', moment(this.state[key]).format('hh:mm:ss'), 'Date without format: ', this.state[key]);
      //   newState[key] = moment(this.state[key]).format('hh:mm:ss') // Error: "Time has wrong format. Use one of these formats instead: hh:mm[:ss[.uuuuuu]]."
      //   // newState[key] = this.state[key]
      // } else {
      //   console.log('start_time: else ', this.state[key]);
      //   newState[key] = this.state[key]
      // }
      newState[key] = this.state[key];
    });
    _.forEach(newState, (level1Val, _state) => {
      if (_state.includes('signature')) {
        if (newState[_state] == null) {
          newState[_state] = 'test';
        }
      }
      _.forEach(level1Val, (value, level2Key) => {
        if (
          level2Key == `btw` ||
          level2Key == 'id' ||
          level2Key == 'created' ||
          level2Key == 'updated' ||
          level2Key == 'percent_effective' ||
          level2Key == 'points_received' ||
          level2Key == 'possible_points'
        )
          delete newState[_state][level2Key];
      });
    });
    // let newAPIDATA = this.state.apiData
    // isDiff.forEach(key => {
    //   // if (key == "start_time") {
    //   //   console.log('start_time: ', moment(this.state[key]).format('hh:mm:ss'), 'Date without format: ', this.state[key]);
    //   //   newState[key] = moment(this.state[key]).format('hh:mm:ss') // Error: "Time has wrong format. Use one of these formats instead: hh:mm[:ss[.uuuuuu]]."
    //   //   // newState[key] = this.state[key]
    //   // } else {
    //   //   console.log('start_time: else ', this.state[key]);
    //   //   newState[key] = this.state[key]
    //   // }
    //   newState[key] = this.state[key]
    // })
    // _.forEach(newAPIDATA, (level1Val, _state) => {
    //   if (_state.includes('signature')) {
    //     if (newAPIDATA[_state] == null) {
    //       newAPIDATA[_state] = ''
    //     }
    //   }
    //   _.forEach(level1Val, (value, level2Key) => {
    //     if (level2Key == `btw` || level2Key == 'id' || level2Key == 'created' || level2Key == 'updated' || level2Key == 'percent_effective' || level2Key == 'points_received' || level2Key == 'possible_points')
    //       delete newAPIDATA[_state][level2Key]
    //   })
    // })

    // const newDIF = getDataDiff(newAPIDATA, this.state, true)
    // console.log('new DIF', newDIF)
    console.log('new state', newState);
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiPatch(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/btw/${_class}/`,
      newState,
      true,
    );
    console.log(`btw patch res: `, res);
    if (res && res.data) {
      this.setState({...res.data, apiData: res.data}, () => {
        // console.log('updated state', this.state)
      });
    }
    return true;
  };

  previewBTW = async () => {
    AsyncStorage.getItem('mapScreenshot').then(async (data) => {
      await this.setState({
        map_screenshot_img: 'data:image/png;base64,' + data,
      });
      const {
        company_info,
        student_info,
        selected_test,
      } = this.props.eveluationFlowReducer;
      // this.setState({ showPreview: true })
      if (this.props.tabChangeErrorMessage) {
        alert(this.props.tabChangeErrorMessage);
        return true;
      } else {
        let res = await apiGet(
          `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/btw/${_class}/accident_probability_graph/`,
        );
        let chartData = [];
        if (res && res.data && res.data.chart_data) {
          _.forEach(res.data.chart_data, (entity) => {
            // `["${level1.title}", ${state[level1.key]['percent_effective'] ? Number(state[level1.key]['percent_effective']) : 5.00}]`
            // chartData.push(`["${entity.title}", ${entity.percentage + ''}]`);
            chartData.push(
              `["${entity.title}", ${entity.new_value}, ${entity.new_percentage}]`,
            );
          });
        }
        console.log('chartData', chartData);
        await this.getData();
        await this.setState({chartData});
        this.setState({showPreview: true});
        return true;
      }
    });
    
  };

  calculatePoints = () => {
    // console.log('this.state', this.state);
    let totalPossiblePoints = 0;
    let totalPointsReceived = 0;
    let totalEffPercentage = 0;
    let check = true;
    _.forEach(this.state, (level1, level1Key) => {
      _.forEach(level1, (level2, key) => {
        if (
          level1Key == 'sections' ||
          level1Key == 'created' ||
          level1Key == 'updated' ||
          level1Key == 'test' ||
          key == 'key' ||
          key == 'title' ||
          key == 'btw' ||
          key == 'possible_points' ||
          key == 'points_received' ||
          key == 'percent_effective' ||
          key == 'created' ||
          key == 'id' ||
          key == 'updated' ||
          key == 'notes'
        ) {
          //ignore these for calculation
        } else {
          if (level2 && isNumber(level2)) {
            // console.log('level2', level2, ' key', key, ' for lvl1', level1Key)
            totalPointsReceived += level2;
            totalPossiblePoints += 5;
            // if (check) {
            //   totalPossiblePoints += level1['possible_points']
            //   check = false
            // }
          }
        }
      });
    });
    totalEffPercentage = (totalPointsReceived / totalPossiblePoints) * 100;
    totalEffPercentage = totalEffPercentage.toFixed(2);
    // console.log('totalPossiblePoints',totalPossiblePoints)
    // console.log('totalPointsReceived',totalPointsReceived)
    this.setState({
      totalPossiblePoints,
      totalPointsReceived,
      totalEffPercentage,
    });
  };

  loadNotificationAlert = (level1) => {
    // console.log('loadNotificationAlert level1', level1)
    let level2Counter = 0;
    let instructionsToShow = '';
    _.forEach(level1, (level2, key) => {
      if (
        key == 'key' ||
        key == 'notes' ||
        key == 'title' ||
        level2.key == 'possible_points' ||
        level2.key == 'points_received' ||
        level2.key == 'percent_effective'
      ) {
        // return null;
      } else {
        ++level2Counter;
        // console.log('loadNotificationAlert key', key)
        if (this.state.instructions[key])
          instructionsToShow += `${counterToAlpha(level2Counter)}. ${
            this.state.instructions[key]
          }\n\n`;
      }
    });
    // console.log('this.state.notifications', this.state.instructions)
    // console.log('instructionsToShow', instructionsToShow)
    if (instructionsToShow) {
      Alert.alert(
        'Notification',
        instructionsToShow,
        [
          {
            text: 'ok',
            onPress: () => console.log('ok Pressed'),
            style: 'cancel',
          },
        ],
        {cancelable: false},
      );
    }
  };

  render() {
    // let totalPointsReceived=0;
    // let totalPossiblePoints=0;
    const {
      totalPointsReceived,
      totalPossiblePoints,
      instructions,
      map_screenshot_img,
    } = this.state;
    const {eveluationFlowReducer} = this.props;
    const {company_info, student_info, selected_test} = eveluationFlowReducer;

    if (this.state.mounting && this.state.isClassSelected == false) {
      return (
        <ScreenWrapper
          contentContainerStyle={{
            justifyContent: 'center',
            alignItems: 'center',
          }}>
          <Text>Please select test class</Text>
          <ActionSheet
            ref={(o) => (this._classActionSheet = o)}
            title={'Select class'}
            options={['A', 'B', 'C', 'P']}
            // cancelButtonIndex={10}
            // destructiveButtonIndex={10}
            onPress={(index) => {
              console.log('Pretrip class actionsheet index', index);
              switch (index) {
                case 0:
                  _class = 'class_a';
                  BTWModal = BTWModalA;
                  break;
                case 1:
                  _class = 'class_b';
                  BTWModal = BTWModalB;
                  break;
                case 2:
                  _class = 'class_c';
                  BTWModal = BTWModalC;
                  break;
                case 3:
                  _class = 'bus';
                  BTWModal = BTWModalBUS1;
                  break;

                default:
                  _class = 'class_a';
                  BTWModal = BTWModalA;
                  break;
              }
              this.setState({isClassSelected: true}, () => {
                this.populateForm();
              });
            }}
          />
        </ScreenWrapper>
      );
    }
    if (this.state.mounting && this.state.isClassSelected) {
      return (
        <ScreenWrapper
          contentContainerStyle={{
            justifyContent: 'center',
            alignItems: 'center',
          }}>
          <Loader />
        </ScreenWrapper>
      );
    }
    let level1Counter = 0;
    let level2Counter = 0;
    const show = {flex: 1, height: undefined};
    const hide = {flex: 0, height: 0};

    return (
      <>
        <ScreenWrapper parentStyle={this.props.shown ? show : hide}>
          <KeyboardAwareScrollView enableAutomaticScroll={false}>
            <Modal
              animationType="slide"
              visible={this.state.showPreview}
              onRequestClose={() => {}}>
              <View style={{flex: 1}}>
                <Header>
                  <TouchableOpacity
                    onPress={async () => {
                      this.setState({showPreview: false});
                    }}>
                    <Text style={{marginLeft: 20, fontSize: 16}}>
                      {'Close'}
                    </Text>
                  </TouchableOpacity>

                  <Text style={{marginRight: scale(23)}}>Preview</Text>
                  <TouchableOpacity
                    onPress={async () => {
                      // const testhtml=BTW(BTWModal, this.state, eveluationFlowReducer.student_info, eveluationFlowReducer.company_info, eveluationFlowReducer.selectedTestInfo, eveluationFlowReducer.instructor_info, eveluationFlowReducer.mapData?.map_screenshot_url,eveluationFlowReducer.mapData, this.state.chartData, true);
                      // console.log(testhtml)
                      // return;
                      let res = await apiGet(
                        `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/btw/${_class}/accident_probability_graph/`,
                      );
                      let chartData = [];
                      if (res && res.data && res.data.chart_data) {
                        _.forEach(res.data.chart_data, (entity) => {
                          chartData.push([
                            `${entity.title}`,
                            entity.new_value,
                            entity.new_percentage,
                          ]);
                        });
                      }
                      console.log('chartData', chartData);
                      let options = {
                        html: BTW(
                          BTWModal,
                          this.state,
                          eveluationFlowReducer.student_info,
                          eveluationFlowReducer.company_info,
                          eveluationFlowReducer.selectedTestInfo,
                          eveluationFlowReducer.instructor_info,
                          eveluationFlowReducer.mapData?.map_screenshot_url,
                          eveluationFlowReducer.mapData,
                          this.state.chartData,
                          true,
                          _class,
                        ),
                        fileName: `student_${eveluationFlowReducer.student_info?.id}_BTW_${_class}`,
                        // directory: 'Documents',
                      };
                      this.setState({showPreview: false});
                      let file = await RNHTMLtoPDF.convert(options);
                      console.log('RNHTMLtoPDF file', file);
                      console.log(
                        'RNHTMLtoPDF file path',
                        `${PLATFORM_IOS ? '' : 'file://'}${file.filePath}`,
                      );
                      await Share.open({
                        url: `${PLATFORM_IOS ? '' : 'file://'}${file.filePath}`,
                        title: 'Share PDF',
                      });
                    }}>
                    {/* <Text style={{ marginRight: 20, fontSize: 16 }}>Share</Text> */}
                    <Image
                      source={EXPORT_ICON}
                      style={{
                        resizeMode: 'contain',
                        height: 20,
                        width: 20,
                        paddingRight: 10,
                      }}
                    />
                  </TouchableOpacity>
                </Header>

                <WebView
                  // source={{ html: PAS(BTWModal, this.state, eveluationFlowReducer.student_info) }}
                  source={{
                    html: BTW(
                      BTWModal,
                      this.state,
                      eveluationFlowReducer.student_info,
                      eveluationFlowReducer.company_info,
                      eveluationFlowReducer.selectedTestInfo,
                      eveluationFlowReducer.instructor_info,
                      eveluationFlowReducer.mapData?.map_screenshot_url,
                      eveluationFlowReducer.mapData,
                      this.state.chartData,
                      true,
                      _class,
                      map_screenshot_img,
                    ),
                  }}
                  // source={require('./preview/btwGenrator.html')}
                  ref={(ref) => {
                    this.WebView = ref;
                  }}
                  javaScriptEnabled={true}
                  domStorageEnabled={true}
                  startInLoadingState={true}
                />
              </View>
            </Modal>

            {_.map(BTWModal, (level1) => {
              // console.log('level1', level1)
              ++level1Counter;
              level2Counter = 0;
              if (level1.value !== undefined) {
                if (level1.title.includes('signature')) {
                  return (
                    <EvaluationField
                      start_time={this.state.start_time}
                      end_time={this.state.end_time}
                      key={`${level1.key}`}
                      title={`${level1Counter}. ${level1.title}`}
                      required
                      onPress={() =>
                        showSelector(
                          <SignaturePicker
                            handleSignature={(signature) => {
                              console.log('signature', signature);
                              this.setState({[level1.key]: signature});
                              hideSelector();
                            }}
                          />,
                        )
                      }
                      component={
                        <View style={{flex: 1}}>
                          <Image
                            source={
                              this.state[level1.key] && {
                                uri: this.state[level1.key],
                              }
                            }
                            style={{
                              width: 100,
                              height: 38,
                              resizeMode: 'cover',
                            }}
                          />
                        </View>
                      }
                    />
                  );
                } else if (
                  level1.title.includes('time') ||
                  level1.title.includes('Time')
                ) {
                  return (
                    <EvaluationField
                      start_time={this.state.start_time}
                      end_time={this.state.end_time}
                      disabled
                      key={`${level1.key}`}
                      title={`${level1Counter}. ${level1.title}`}
                      value={this.state[level1.key]}
                      onChangeText={(value) =>
                        this.setState({[level1.key]: value})
                      }
                    />
                  );
                } else if (
                  level1.title.includes('Date') ||
                  level1.title.includes('date')
                ) {
                  // to find date, look for ate as D can be capital
                  return (
                    <EvaluationField
                      start_time={this.state.start_time}
                      end_time={this.state.end_time}
                      title={`${level1Counter}. ${level1.title}`}
                      key={`${level1.key}`}
                      // required
                      rightArrow
                      onPress={() => {
                        showPopup(
                          <DateTimePicker
                            onConfirm={(date) => {
                              this.setState({[level1.key]: date});
                            }}
                          />,
                        );
                      }}
                      component={
                        <View
                          style={{flexDirection: 'row', alignItems: 'center'}}>
                          <Image
                            source={CALENDAR_ICON}
                            style={{height: scale(34), width: scale(34)}}
                          />
                          <Text>{this.state[level1.key]}</Text>
                        </View>
                      }
                    />
                  );
                } else {
                  return (
                    <EvaluationField
                      start_time={this.state.start_time}
                      end_time={this.state.end_time}
                      key={`${level1.key}`}
                      title={`${level1Counter}. ${level1.title}`}
                      value={this.state[level1.key]}
                      onChangeText={(value) =>
                        this.setState({[level1.key]: value})
                      }
                    />
                  );
                }
              } else {
                {
                  /* this.state.sections.push({ id: level1Counter, name: level1.title }) */
                }
                return (
                  <View
                    onLayout={(event) =>
                      (sectionPosition = {
                        ...sectionPosition,
                        [level1.key]: Math.round(event.nativeEvent.layout.y),
                      })
                    }>
                    <View
                      style={{
                        backgroundColor: colors.APP_LIGHT_BLUE_COLOR,
                        flexDirection: 'row',
                        justifyContent: 'space-between',
                        alignItems: 'center',
                        paddingHorizontal: 10,
                      }}>
                      <Text
                        style={{
                          marginVertical: 5,
                        }}>{`${level1Counter}. ${level1.title}`}</Text>
                      <TouchableOpacity
                        onPress={() => this.loadNotificationAlert(level1)}>
                        <Image
                          source={INFO_BLUE_ICON}
                          style={{height: 20, width: 20, resizeMode: 'contain'}}
                        />
                      </TouchableOpacity>
                    </View>
                    {_.map(level1, (level2, key) => {
                      {
                        /* console.log('level2 test ',level1Counter, level2, ' KEY', key) */
                      }
                      if (
                        key == 'key' ||
                        key == 'title' ||
                        level2.key == 'possible_points' ||
                        level2.key == 'points_received' ||
                        level2.key == 'percent_effective'
                      ) {
                        // if(level2.key == "possible_points"){
                        //   console.log('possible_points',level2, 'for ', level1.title)
                        // }
                        return null;
                      }

                      if (level2.key == 'notes') {
                        return (
                          <EvaluationField
                            start_time={this.state.start_time}
                            end_time={this.state.end_time}
                            key={`${level1.key}+${level2.key}`}
                            oneliner
                            title={level2.title}
                            onChangeText={(newValue) =>
                              this.setState({
                                [level1.key]: {
                                  ...this.state[level1.key],
                                  [level2.key]: newValue,
                                },
                              })
                            }
                            value={this.state[level1.key][level2.key]}
                          />
                        );
                      }
                      ++level2Counter;

                      return (
                        <Evaluation7OptionField
                          start_time={this.state.start_time}
                          end_time={this.state.end_time}
                          key={`${level1.key}+${level2.key}`}
                          title={`${
                            counterToAlpha(level2Counter) == undefined
                              ? ''
                              : counterToAlpha(level2Counter)
                          }. ${level2.title}`}
                          onChange={(newValue) =>
                            this.setState(
                              {
                                [level1.key]: {
                                  ...this.state[level1.key],
                                  [level2.key]: newValue,
                                },
                              },
                              this.calculatePoints,
                            )
                          }
                          value={this.state[level1.key][level2.key]}
                        />
                      );
                    })}
                  </View>
                );
              }
            })}
          </KeyboardAwareScrollView>
        </ScreenWrapper>
        {this.props.shown && (
          <Footer>
            <TouchableOpacity
              onPress={() => NavigationService.navigate('MapScreen')}>
              <Text>Turns</Text>
            </TouchableOpacity>

            {/* <TouchableOpacity onPress={() => {
            showSelector(<Selector
              title={'Section'}
              data={this.state.sections}
              onSelect={(item) => this.setState({ instructor: item.name })}
            />)
          }}>
            <Text>Section</Text>
          </TouchableOpacity> */}

            {!this.state.end_time && (
              <TouchableOpacity
                onPress={() => {
                  console.log('this.state', this.state);
                  if (this.state.start_time) {
                    Alert.alert(
                      'Finish Test',
                      `Are you sure you want to mark the test as complete\nyou will not be able to make changes once a test is completed`,
                      [
                        {
                          text: 'No',
                          onPress: () => console.log('Cancel Pressed'),
                          style: 'cancel',
                        },
                        {
                          text: 'Yes',
                          onPress: () => {
                            this.setState(
                              {end_time: moment().format('HH:mm')},
                              async () => {
                                await this.saveBTW();
                              },
                            );
                          },
                        },
                      ],
                      {cancelable: false},
                    );
                  } else {
                    this.setState({
                      start_time: moment().format('HH:mm'),
                      date: moment().format('YYYY-MM-DD'),
                    }); // MM/DD/YYYY HH:mm:ss
                  }
                }}>
                <Image
                  source={this.state.start_time ? PAUSE_ICON : PLAY_ICON}
                  style={{resizeMode: 'contain', height: 25, width: 25}}
                />
              </TouchableOpacity>
            )}

            {/* <TouchableOpacity onPress={() => {
            Alert.alert(
              'Delete Data',
              `Are you sure you want to clear test data`,
              [
                {
                  text: 'No',
                  onPress: () => console.log('Cancel Pressed'),
                  style: 'cancel',
                },
                {
                  text: 'Yes',
                  onPress: () => {
                    this.populateForm(true)
                  }
                },
              ],
              { cancelable: false },
            )
          }}>
            <Image source={CLOSE_ICON} style={{ resizeMode: 'contain', height: 20, width: 20 }} />
          </TouchableOpacity> */}

            <TouchableOpacity
              onPress={() => {
                Alert.alert(
                  'Info',
                  `${totalPointsReceived} points received from ${totalPossiblePoints} points possible`,
                );
              }}>
              <Text>
                {totalPointsReceived}/{totalPossiblePoints}
              </Text>
            </TouchableOpacity>

            {/* <TouchableOpacity
            // onPress={() => Alert.alert('Options', `Turn Notifications On`,
            //   [
            //     {
            //       text: 'No',
            //       onPress: () => console.log('No Pressed'),
            //       style: 'no',
            //     },
            //     {
            //       text: 'Yes',
            //       onPress: () => console.log('Yes Pressed')
            //     },
            //   ],
            //   { cancelable: false })}
            >
            <Image source={EXPORT_ICON} style={{ resizeMode: 'contain', height: 20, width: 20, paddingRight: 10 }} />
          </TouchableOpacity> */}
          </Footer>
        )}
      </>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    userReducer: state.userReducer,
    eveluationFlowReducer: state.eveluationFlowReducer,
    tabChangeErrorMessage: state.eveluationFlowReducer.tabChangeErrorMessage,
  };
};

export default connect(
  mapStateToProps,
  {fetchUserProfileAction, updateTabChangeErrorMessage, setMapData},
  null,
  {forwardRef: true},
)(BTWTab);

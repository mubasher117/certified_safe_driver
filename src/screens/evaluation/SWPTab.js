import React from 'react';
import {View, TouchableOpacity, Image, Modal, Alert} from 'react-native';
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
  EvaluationYesNoOptionField,
  Footer,
  Selector,
} from '../../components';
import {
  fetchUserProfileAction,
  hideSelector,
  showPopup,
  showSelector,
} from '../../actions';
import {
  CALENDAR_ICON,
  PLAY_ICON,
  PAUSE_ICON,
  EXPORT_ICON,
  CLOSE_ICON,
  INFO_BLUE_ICON,
  PLATFORM_IOS,
} from '../../constants';
import {SwpDataModals} from '../../utils/SwpDataModals';
import _, {sample, isNumber} from 'lodash';
import * as colors from '../../styles/colors';
import {counterToAlpha} from '../../utils/function';
import {apiPatch, apiGet} from '../../utils/http';
import {WebView} from 'react-native-webview';
import {scale} from '../../utils/scale';
import RNHTMLtoPDF from 'react-native-html-to-pdf';
import SWP from './preview/SWPPreviewHTML';
import Share from 'react-native-share';
import moment from 'moment';

let sectionPosition = {};

class SWPTab extends React.Component {
  state = {
    sections: [],
    // ...SwpDataModals,
    signature: null,
    mounting: true,
    showPreview: false,
    start_time: false,
    totalPointsReceived: 0,
    totalPossiblePoints: 0,
    totalEffPercentage: 0,
    instructions: [],
  };

  async componentDidMount() {
    this.populateForm();
  }

  populateForm = (clear) => {
    let state = {};
    _.forEach(SwpDataModals, (level1Val, level1Key) => {
      let level2State = null;
      if (
        level1Val &&
        level1Val.value === null &&
        level1Val.value !== undefined
      ) {
        //fields with no nesteds
        //  console.log('nulls keys', level1Val.value);
      } else {
        level2State = {};
        // console.log('undefined keys', level1Val);
        _.forEach(level1Val, (val, level2Key) => {
          if (level2Key != 'key' && level2Key != 'title') {
            level2State[level2Key] = val?.value;
          }
        });
      }
      state[level1Key] = level2State;
    });
    // console.log('state', state);
    this.setState({...state}, () => {
      if (!clear) {
        this.getData();
      }
    });
  };
  scrolSectionHandler = (num) => {
    // console.log('this.myScroll: ', num, sectionPosition[num.key], this.myScroll);
    this.myScroll.scrollToPosition(0, sectionPosition[num.key]);
  };

  getData = async () => {
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/swp/`,
    );
    // console.log('swp res', res);
    let instructions = await apiGet('/api/v1/instructions/swp/');

    if (res && res.data && instructions && instructions.data) {
      // console.log('data', res.data)
      let instructionsObjectified = {};
      instructions.data.forEach((_instruction) => {
        instructionsObjectified[_instruction.field_name] =
          _instruction.instruction;
      });
      // console.log('instructionsObjectified', instructionsObjectified);
      this.setState({
        ...res.data,
        instructions: instructions.data,
        mounting: false,
      });
    } else {
      this.setState({mounting: false});
    }
    return true;
  };

  saveSWP = async () => {
    //TODO: how to upload signature
    let newState = this.state;
    _.forEach(newState, (value, _state) => {
      if (_state.includes('signature')) {
        if (newState[_state] == null) {
          delete newState[_state];
        }
      }
    });
    _.forEach(newState, (level1Val, _state) => {
      _.forEach(level1Val, (value, level2Key) => {
        if (level2Key == 'swp') {
          delete newState[_state][level2Key];
        }
      });
    });

    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiPatch(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/swp/`,
      newState,
      true,
    );
    // console.log('swp patch res: ', res);
    if (res && res.data) {
      // this.props.navigation.goBack()
      // errorMessage('Student Info Updated')
      // this.getData();
      this.setState({...res.data})
    }
    return true;
  };

  previewSWP = async () => {
    // this.setState({ showPreview: true })
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/swp/injury_probability_graph/`,
    );
    let chartData = [];
    if (res && res.data && res.data.chart_data) {
      _.forEach(res.data.chart_data, (entity) => {
        // `["${level1.title}", ${state[level1.key]['percent_effective'] ? Number(state[level1.key]['percent_effective']) : 5.00}]`
        chartData.push(`["${entity.title}", ${entity.new_value + ''}]`);
      });
    }
    // console.log('chartData', chartData);
    await this.getData();
    await this.setState({chartData});
    this.setState({showPreview: true});
  };

  calculatePoints = () => {
    // console.log('calculatePoints this.state', this.state);
    let totalPossiblePoints = 0;
    let totalPointsReceived = 0;
    let totalEffPercentage = 0;
    // let check = true;
    _.forEach(this.state, (level1, level1Key) => {
      // check = true
      // console.log('calculatePoints level1Key', level1Key);
      _.forEach(level1, (level2, key) => {
        if (
          level1Key == 'sections' ||
          level1Key == 'created' ||
          level1Key == 'updated' ||
          level1Key == 'test' ||
          level1Key == 'student' ||
          level1Key == 'totalEffPercentage' ||
          level1Key == 'start_time' ||
          key == 'key' ||
          key == 'title' ||
          key == 'swp' ||
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
          if (level2 && typeof level2 !== 'string') {
            // console.log(
            //   'level2--',
            //   level2,
            //   '--key--',
            //   key,
            //   '--for lvl1--',
            //   level1Key,
            // );
            if (isNumber(level2)) {
              totalPointsReceived += level2
              totalPossiblePoints += 5
            } 
            // else {
            //   totalPointsReceived += 5
            //   totalPossiblePoints += 5
            // }

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

    // console.log('totalPossiblePoints', totalPossiblePoints);
    // console.log('totalPointsReceived', totalPointsReceived);
    // console.log('totalEffPercentage', totalEffPercentage)

    this.setState({
      totalPossiblePoints,
      totalPointsReceived,
      totalEffPercentage,
    });
  };

  loadNotificationAlert = (level1) => {
    // console.log('level1', level1)
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
        // console.log('key', key)
        if (this.state.instructions[key]) {
          instructionsToShow += `${counterToAlpha(level2Counter)}. ${
            this.state.instructions[key]
          }\n\n`;
        }
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
    if (this.state.mounting) {
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
    const {eveluationFlowReducer} = this.props;
    const {totalPointsReceived, totalPossiblePoints} = this.state;
    const {
      company_info,
      student_info,
      selected_test,
      selectedTestInfo,
      instructor_info,
    } = eveluationFlowReducer;
    return (
      <>
        <ScreenWrapper parentStyle={this.props.shown ? show : hide}>
          <KeyboardAwareScrollView
            enableAutomaticScroll={false}
            ref={(ref) => {
              this.myScroll = ref;
            }}>
            <Modal
              animationType="slide"
              visible={this.state.showPreview}
              onRequestClose={() => {}}>
              <View style={{flex: 1}}>
                <Header>
                  <TouchableOpacity
                    onPress={() => this.setState({showPreview: false})}>
                    <Text style={{marginLeft: 20, fontSize: 16}}>
                      {'Close'}
                    </Text>
                  </TouchableOpacity>

                  <Text style={{marginRight: scale(23)}}>Preview</Text>
                  {/* <Text>Email</Text> */}

                  <TouchableOpacity
                    onPress={async () => {
                      let options = {
                        html: SWP(
                          SwpDataModals,
                          this.state,
                          eveluationFlowReducer.student_info,
                          eveluationFlowReducer.company_info,
                          eveluationFlowReducer.selectedTestInfo,
                          eveluationFlowReducer.instructor_info,
                          this.state.chartData,
                        ),
                        fileName: `student_${student_info?.id}_SWP`,
                        // directory: 'Documents',
                      };

                      let file = await RNHTMLtoPDF.convert(options);
                      // console.log('RNHTMLtoPDF file', file);
                      // console.log(
                      //   'RNHTMLtoPDF file path',
                      //   `${PLATFORM_IOS ? '' : 'file://'}${file.filePath}`,
                      // );
                      await Share.open({
                        url: `${PLATFORM_IOS ? '' : 'file://'}${file.filePath}`,
                        title: 'Share PDF',
                      });
                      // const datapdf= SWP(SwpDataModals, this.state, eveluationFlowReducer.student_info, eveluationFlowReducer.company_info, eveluationFlowReducer.selectedTestInfo, eveluationFlowReducer.instructor_info, this.state.chartData)
                      // console.log('datapdf',datapdf)
                      // PDF.fromHTML(datapdf,'http:localhost')
                      // .then(async data => {
                      //   console.log('data: ', data)
                      //   await Share.open({
                      //     // url: `${PLATFORM_IOS ? '' : 'file://'}${file.filePath}`,
                      //     url:`data:application/pdf;base64,${data}`,
                      //     title: 'Share PDF'
                      //   })
                      // }) // WFuIGlzIGRpc3Rpbm....
                      // .catch(err => console.log('error->', err))
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
                  // source={require('./preview/swp.html')}
                  source={{
                    html: SWP(
                      SwpDataModals,
                      this.state,
                      eveluationFlowReducer.student_info,
                      eveluationFlowReducer.company_info,
                      eveluationFlowReducer.selectedTestInfo,
                      eveluationFlowReducer.instructor_info,
                      this.state.chartData,
                    ),
                  }}
                  ref={(ref) => {
                    this.WebView = ref;
                  }}
                  javaScriptEnabled={true}
                  domStorageEnabled={true}
                  startInLoadingState={true}
                />
              </View>
            </Modal>

            {_.map(SwpDataModals, (level1) => {
              // console.log('level1', level1)
              ++level1Counter;
              level2Counter = 0;
              if (level1.value !== undefined) {
                if (level1.title.includes('signature')) {
                  return (
                    <EvaluationField
                    isSignature
                      start_time={this.state.start_time}
                      end_time={this.state.end_time}
                      key={`${level1.key}`}
                      title={`${level1Counter}. ${level1.title}`}
                      required
                      onPress={() =>
                        showSelector(
                          <SignaturePicker
                            handleSignature={(signature) => {
                              // console.log('signature', signature);
                              this.setState({[level1.key]: signature});
                              hideSelector();
                            }}
                          />,
                        )
                      }
                      component={
                        <View style={{flex: 1, height: 100}}>
                          <Image
                            source={
                              this.state[level1.key] && {
                                uri: this.state[level1.key],
                              }
                            }
                            style={{
                              width: 100,
                              height: 78,
                              resizeMode: 'cover',
                            }}
                          />
                        </View>
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
                      // required
                      rightArrow
                      title={`${level1Counter}. ${level1.title}`}
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
                this.state.sections.push({
                  id: level1Counter,
                  name: level1.title,
                  key: level1.key,
                });
                return (
                  <View
                    onLayout={(event) =>
                      (sectionPosition = {
                        ...sectionPosition,
                        [level1.key]: Math.round(event.nativeEvent.layout.y),
                      })
                    }>
                    {/* <View style={{ backgroundColor: colors.APP_LIGHT_BLUE_COLOR }}>
                    <Text style={{ marginHorizontal: 10, marginVertical: 5, }}>{`${level1Counter}. ${level1.title}`}</Text>
                  </View> */}
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
                      // console.log('level2', level2, ' KEY', key)
                      if (
                        key == 'key' ||
                        key == 'title' ||
                        level2.key == 'possible_points' ||
                        level2.key == 'points_received' ||
                        level2.key == 'percent_effective'
                      ) {
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
                      if (level1.title == 'Employees interview') {
                        return (
                          <EvaluationYesNoOptionField
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
                      }
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
              onPress={() => {
                showSelector(
                  <Selector
                    title={'Section'}
                    data={this.state.sections}
                    onSelect={this.scrolSectionHandler}
                  />,
                );
              }}>
              <Text>Section</Text>
            </TouchableOpacity>

            {!this.state.end_time && (
              <TouchableOpacity
                onPress={() => {
                  // console.log('this.state', this.state);
                  if (this.state.start_time) {
                    Alert.alert(
                      'Finish Test',
                      'Are you sure you want to mark the test as complete\nyou will not be able to make changes once a test is completed',
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
                                await this.saveSWP();
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

            {/* <TouchableOpacity>
            <Image source={CLOSE_ICON} style={{ resizeMode: 'contain', height: 20, width: 20 }} />
          </TouchableOpacity> */}

            {/* <TouchableOpacity onPress={() => {
            Alert.alert("Info", "0 points received from 0 points possible");
          }}>
            <Text>0/0</Text>
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

            <TouchableOpacity
              onPress={() =>
                Alert.alert(
                  'Options',
                  'Turn Notifications On',
                  [
                    {
                      text: 'No',
                      onPress: () => console.log('No Pressed'),
                      style: 'no',
                    },
                    {
                      text: 'Yes',
                      onPress: () => console.log('Yes Pressed'),
                    },
                  ],
                  {cancelable: false},
                )
              }>
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
  };
};

export default connect(mapStateToProps, {fetchUserProfileAction}, null, {
  forwardRef: true,
})(SWPTab);

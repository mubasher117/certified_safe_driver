import React from 'react';
import {View, TouchableOpacity, Image, Modal, Alert} from 'react-native';
import {KeyboardAwareScrollView} from 'react-native-keyboard-aware-scroll-view';
import {connect} from 'react-redux';
import {
  Text,
  Loader,
  ScreenWrapper,
  EvaluationField,
  Header,
  DateTimePicker,
  Selector,
  SignaturePicker,
  EvaluationImpOptionField,
  Evaluation4OptionField,
  EvaluationYesNoOptionField,
  Footer,
} from '../../components';
import {
  fetchUserProfileAction,
  hideSelector,
  showPopup,
  showSelector,
} from '../../actions';
import {
  RIGHT_ARROW_ICON,
  CALENDAR_ICON,
  PLAY_ICON,
  PAUSE_ICON,
  EXPORT_ICON,
  INFO_BLUE_ICON,
  CLOSE_ICON,
  PLATFORM_IOS,
} from '../../constants';
import {VRTDataModals} from '../../utils/VRTDataModals';
import _ from 'lodash';
import * as colors from '../../styles/colors';
import {counterToAlpha} from '../../utils/function';
import {scale} from '../../utils/scale';
import {WebView} from 'react-native-webview';
import {apiPatch, apiGet} from '../../utils/http';
import VRT from './preview/VRTPreviewHTML';
import RNHTMLtoPDF from 'react-native-html-to-pdf';
import Share from 'react-native-share';
import moment from 'moment';

class VRTTab extends React.Component {
  state = {
    // ...VRTDataModals,
    sections: [],
    mounting: true,
    showPreview: false,
    start_time: false,
    instructions: [],
  };
  async componentDidMount() {
    this.populateForm();
  }
  populateForm = (clear) => {
    let state = {};
    _.forEach(VRTDataModals, (level1Val, level1Key) => {
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
          if (level2Key != 'key' && level2Key != 'title')
            level2State[level2Key] = val?.value;
        });
      }
      state[level1Key] = level2State;
    });
    console.log('state', state);
    this.setState({...state}, () => {
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
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/vrt/`,
    );
    let instructions = await apiGet(`/api/v1/instructions/vrt/`);

    if (res && res.data && instructions && instructions.data) {
      console.log('data', res.data);
      let instructionsObjectified = {};
      instructions.data.forEach((_instruction) => {
        instructionsObjectified[_instruction.field_name] =
          _instruction.instruction;
      });
      console.log('instructionsObjectified', instructionsObjectified);

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

  saveVRT = async () => {
    //TODO: how to upload signature
    let newState = this.state;
    _.forEach(newState, (value, _state) => {
      if (_state.includes('signature'))
        if (newState[_state] == null) {
          // delete newState[_state]
          delete newState[_state];
        }
    });
    _.forEach(newState, (level1Val, _state) => {
      _.forEach(level1Val, (value, level2Key) => {
        if (level2Key == 'vrt') delete newState[_state][level2Key];
      });
    });

    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiPatch(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/vrt/`,
      newState,
      true,
    );
    console.log(`vrt patch res: `, res);
    if (res && res.data) {
      // this.props.navigation.goBack()
      // errorMessage('Student Info Updated')
      // this.getData();
    }
    return true;
  };

  previewVRT = async () => {
    await this.getData();
    this.setState({showPreview: true});
  };

  loadNotificationAlert = (level1) => {
    console.log('level1', level1);
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
        console.log('key', key);
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
                        html: VRT(
                          VRTDataModals,
                          this.state,
                          eveluationFlowReducer.student_info,
                          eveluationFlowReducer.company_info,
                          eveluationFlowReducer.selectedTestInfo,
                          eveluationFlowReducer.instructor_info,
                          true,
                        ),
                        fileName: `student_${eveluationFlowReducer.student_info?.id}_VRT`,
                        // directory: 'Documents',
                      };

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
                  source={{
                    html: VRT(
                      VRTDataModals,
                      this.state,
                      eveluationFlowReducer.student_info,
                      eveluationFlowReducer.company_info,
                      eveluationFlowReducer.selectedTestInfo,
                      eveluationFlowReducer.instructor_info,
                    ),
                  }}
                  // source={require('./preview/vrt.html')}
                  ref={(ref) => {
                    this.WebView = ref;
                  }}
                  javaScriptEnabled={true}
                  domStorageEnabled={true}
                  startInLoadingState={true}
                />
              </View>
            </Modal>

            {_.map(VRTDataModals, (level1) => {
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
                } else if (level1.title === 'Qualified') {
                  return (
                    <EvaluationYesNoOptionField
                      start_time={this.state.start_time}
                      end_time={this.state.end_time}
                      key={`${level1.key}`}
                      title={`${level1Counter}. ${level1.title}`}
                      onChange={(newValue) =>
                        this.setState({[level1.key]: newValue})
                      }
                      value={this.state[level1.key]}
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
                      key={`${level1.key}`}
                      title={`${level1Counter}. ${level1.title}`}
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
                } else if (level1.title === 'Equiment used') {
                  return (
                    <>
                      <EvaluationField
                        start_time={this.state.start_time}
                        end_time={this.state.end_time}
                        key={`${level1.key}`}
                        // required
                        title={`${level1Counter}. Equiment used`}
                        onPress={() => {
                          const {
                            company_info,
                            student_info,
                            selected_test,
                          } = this.props.eveluationFlowReducer;
                          showSelector(
                            <Selector
                              title={'Equiment used'}
                              resultPath={'data'}
                              // displayKey={'power_unit_number'}
                              displayComponent={(item) => (
                                <Text>{item.power_unit_number}</Text>
                              )}
                              endpoint={`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/equips/`}
                              onSelect={(quip_used) =>
                                this.setState({
                                  [level1.key]: quip_used.power_unit_number,
                                })
                              }
                            />,
                          );
                          //   showSelector(<Selector
                          //   title={'Equiment used'}
                          //   data={[
                          //     { id: 1, name: '232, tracter' },
                          //     { id: 2, name: 'B' },
                          //     { id: 3, name: 'C' },
                          //   ]}
                          //   onSelect={(quip_used) => this.setState({ [level1.key]: quip_used })}
                          // />)
                        }}
                        component={
                          <View
                            style={{
                              flexDirection: 'row',
                              alignItems: 'center',
                              justifyContent: 'space-between',
                              flex: 1,
                            }}>
                            <Text>{this.state[level1.key]}</Text>
                            <Image
                              source={RIGHT_ARROW_ICON}
                              style={{height: scale(12), width: scale(12)}}
                            />
                          </View>
                        }
                      />
                      {/* <EvaluationYesNoOptionField
            start_time={this.state.start_time}
            end_time={this.state.end_time}
                      title={`Qualified`}
                      onChange={(qualified) => this.setState({ qualified })}
                      value={this.state.qualified}
                    /> */}
                    </>
                  );
                } else {
                  let isInputDisabled = false;
                  if (
                    level1.title === 'Remarks' &&
                    this.state.qualified &&
                    this.state.qualified !== false
                  ) {
                    isInputDisabled = true;
                  }
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
                      disabled={isInputDisabled}
                      required={!isInputDisabled}
                    />
                  );
                }
              } else {
                this.state.sections.push({
                  id: level1Counter,
                  name: level1.title,
                });
                // this.setState({ sections: { id: level1Counter, name: level1.title } })
                return (
                  <View>
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
                      ++level2Counter;
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
                        // } else if (level2.key == "serv_brake_test" || level2.key == "raise_landing_gear" || level2.key == "check_gauges" || level2.key == "seat_belt" || level2.key == "coast" || level2.key == "timing_down" || level2.key == "hv_when_stopped_traffic" || level2.key == "does_not_hit_dock" || level2.key == "engine_off_pull_key" || level2.key == "defensive_driving" || level2.key == "leaks" || level2.key == "verify_firm_to_ground") {
                      } else if (level2.key == 'score') {
                        return (
                          <>
                            <View
                              style={{
                                width: '100%',
                                height: 2,
                                backgroundColor: 'black',
                                marginTop: 5,
                              }}
                            />
                            <Evaluation4OptionField
                              start_time={this.state.start_time}
                              end_time={this.state.end_time}
                              key={`${level1.key}+${level2.key}`}
                              title={`${level2.title}`}
                              onChange={(newValue) =>
                                this.setState({
                                  [level1.key]: {
                                    ...this.state[level1.key],
                                    [level2.key]: newValue,
                                  },
                                })
                              }
                              value={this.state[level1.key][level2.key]}
                            />

                            <View
                              style={{
                                width: '100%',
                                height: 2,
                                backgroundColor: 'black',
                                marginTop: 3,
                              }}
                            />
                          </>
                        );
                      }
                      return (
                        <EvaluationImpOptionField
                          start_time={this.state.start_time}
                          end_time={this.state.end_time}
                          key={`${level1.key}+${level2.key}`}
                          title={`${
                            counterToAlpha(level2Counter) == undefined
                              ? ''
                              : counterToAlpha(level2Counter)
                          }. ${level2.title}`}
                          onChange={(newValue) =>
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
                    })}
                  </View>
                );
              }
            })}
          </KeyboardAwareScrollView>
        </ScreenWrapper>
        {this.props.shown && (
          <Footer>
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
                                await this.saveVRT();
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

            <TouchableOpacity
              onPress={() => {
                Alert.alert('Info', '0 points received from 0 points possible');
              }}>
              <Text>0/0</Text>
            </TouchableOpacity>

            {/* <TouchableOpacity
            onPress={() => Alert.alert('Options', `Turn Notifications On`,
              [
                {
                  text: 'No',
                  onPress: () => console.log('No Pressed'),
                  style: 'no',
                },
                {
                  text: 'Yes',
                  onPress: () => console.log('Yes Pressed')
                },
              ],
              { cancelable: false })}>
            <Image source={EXPORT_ICON} style={{ resizeMode: 'contain', height: 20, width: 20, paddingRight: 10 }} />
          </TouchableOpacity> */}
          </Footer>
        )}
      </>
    );
  }
}

const mapStateToProps = (state) => {
  // console.log('student_info Redux: ', state.eveluationFlowReducer.student_info);

  return {
    userReducer: state.userReducer,
    eveluationFlowReducer: state.eveluationFlowReducer,
  };
};

export default connect(mapStateToProps, {fetchUserProfileAction}, null, {
  forwardRef: true,
})(VRTTab);

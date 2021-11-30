import React from 'react';
import {
  StatusBar,
  View,
  Image,
  ScrollView,
  TouchableOpacity,
  Modal,
  Alert,
  TextInput,
  Button,
} from 'react-native';
import {connect} from 'react-redux';
import SplashScreen from 'react-native-splash-screen';
import {
  errorMessage,
  fetchUserProfileAction,
  showPopup,
  showSelector,
} from '../../../actions';
import {
  PLATFORM_IOS,
  INFO_ICON,
  PAUSE_ICON,
  PLAY_ICON,
  CLOSE_ICON,
  PLUS_ICON,
  EXPORT_ICON,
} from '../../../constants';
import * as colors from '../../../styles/colors';
import {
  Loader,
  Text,
  Header,
  Footer,
  ScreenWrapper,
  EvaluationField,
  CheckboxGroup,
  EvaluationTrueFalseOptionField,
  CheckBoxGroup,
} from '../../../components';
import {
  SEARCH_ICON,
  SCREEN_WIDTH,
  CALENDAR_ICON,
  RIGHT_ARROW_ICON,
  ALL_US_STATES,
} from '../../../constants';
import {scale} from '../../../utils/scale';
import {apiGet, apiPatch, apiPut, apiPost} from '../../../utils/http';
import _ from 'lodash';
import {getObjectDiff, getDataDiff} from '../../../utils/function';
import moment from 'moment';
import {dayTruckQuiz} from '../questions/dayTruckQuiz';
import {WebView} from 'react-native-webview';
import RNHTMLtoPDF from 'react-native-html-to-pdf';
import Share from 'react-native-share';
import TruckDrivingSchoolPreview from './preview/TruckDrivingSchoolPreview';

const styles = {
  dayHoursTitle: {width: 120, fontWeight: 'bold'},
  hoursContainer: {
    flexDirection: 'row',
    marginLeft: 20,
    justifyContent: 'center',
  },
  hours: {width: 100, textAlign: 'center'},
};

class DaysTruckSchoolTab extends React.Component {
  state = {
    start_time: '12:30 AM',
    date: '',
    driverName: '',
    trainerName: '',
    history: '',
    checkBoxState: {},
    mounting: true,
    _dayTruckSchoolQuiz: dayTruckQuiz,
    truckDrvingSchool: {},
    showPreview: false,
    comments: {}
  };

  async componentDidMount() {
    const {
      company_info,
      student_info,
      selected_test,
      instructor_info,
    } = this.props.eveluationFlowReducer;
    this.props.eveluationFlowReducer;
    this.setState({
      mounting: false,
      driverName: `${student_info?.first_name}  ${student_info?.last_name}`,
      trainerName: instructor_info?.full_name,
    });
    this.getTruckDrivingSchoolData();
    this.getTestDate();
  }

  componentDidUpdate(previousProps) {
    if (this.props.shown !== previousProps.shown && this.props.shown === true) {
      this.getTruckDrivingSchoolData();
      this.getTestDate();
    }
  }

  handleGenderCheckBox = (event) => {
    console.log('event: ', event);

    let quizes = this.state._dayTruckSchoolQuiz;

    quizes.forEach((data) => {
      if (data.type == 'checkbox') {
        data.option.forEach((data) => {
          if (data.label === event.label) {
            data.isChecked = !data.isChecked;
          }
        });
      }
    });
    this.setState({_dayTruckSchoolQuiz: quizes});
  };

  saveDistractedQuiz = async () => {
    //TODO: how to upload signature
    let newState = this.state;
    // _.forEach(newState, (level1Val, _state) => {
    //   _.forEach(level1Val, (value, level2Key) => {
    //     if (level2Key == 'vrt')
    //       delete newState[_state][level2Key]
    //   })
    // })
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiPatch(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/distracted-quiz/`,
      newState,
      true,
    );
    console.log('vrt patch res: ', res);
    if (res && res.data) {
      // this.props.navigation.goBack()
      // errorMessage('Student Info Updated')
      // this.getData();
    }
    return true;
  };
  getTestDate = async () => {
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/`,
    );
    if (res && res.data) {
      this.setState({
        date: res.data.created.split('T')[0],
      });
    }
    return true;
  };

  getDayComment = (day) => {
    console.log('_+_+_+_+_+_+_+ COMMENT FUNC _+_+_+_+_+_+_+_');
    console.log(day);
    let commentIndex = this.state.truckDrvingSchool?.comments?.findIndex(
      (item) => item.day === day,
    );
    if (commentIndex !== -1) {
      console.log(this.state.truckDrvingSchool?.comments[commentIndex]);
      return this.state.truckDrvingSchool?.comments[commentIndex];
    }
    return '';
  };

  getTruckDrivingSchoolData = async () => {
    //TODO: how to upload signature
    let newState = this.state;
    // _.forEach(newState, (level1Val, _state) => {
    //   _.forEach(level1Val, (value, level2Key) => {
    //     if (level2Key == 'vrt')
    //       delete newState[_state][level2Key]
    //   })
    // })
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/training-records/`,
    );
    if (res && res.data) {
      let tempComments = {}
      res.data?.comments.map((item, index) => {
        tempComments[item.day] = item.body;
      })
      this.setState({
        truckDrvingSchool: res.data,
        comments: tempComments
      });
    }
    return true;
  };
  render() {
    const {
      start_time,
      date,
      driverName,
      trainerName,
      history,
      _dayTruckSchoolQuiz,
      truckDrvingSchool,
    } = this.state;
    const {
      company_info,
      student_info,
      selected_test,
      instructor_info,
    } = this.props.eveluationFlowReducer;

    const show = {flex: 1, height: undefined};
    const hide = {flex: 0, height: 0};
    let level1Counter = 0;
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
    return (
      <>
        <ScreenWrapper parentStyle={this.props.shown ? show : hide}>
          <ScrollView style={{flex: 1}}>
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
                      console.log(student_info);
                      let options = {
                        html: TruckDrivingSchoolPreview(
                          this.state.truckDrvingSchool,
                          this.state,
                          student_info,
                          company_info,
                          instructor_info,
                          INFO_ICON,
                        ),
                        fileName: `Driving_School_Record_${student_info?.first_name}`,
                        // directory: 'Documents',
                      };
                      this.setState({showPreview: false});
                      let file = await RNHTMLtoPDF.convert(options);
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
                  // source={require('./preview/notes.html')}
                  source={{
                    html: TruckDrivingSchoolPreview(
                      this.state.truckDrvingSchool,
                      this.state,
                      student_info,
                      company_info,
                      instructor_info,
                      INFO_ICON,
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

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Driver Name'}
              onChangeText={(driverName) => this.setState({driverName})}
              value={driverName}
            />
            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Trainer Name'}
              onChangeText={(trainerName) => this.setState({trainerName})}
              value={trainerName}
            />
            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Date'}
              onChangeText={(date) => this.setState({date})}
              value={date}
            />
            {truckDrvingSchool?.days?.map((elem, index) => {
              const drivingSchool = truckDrvingSchool.day_list[elem];
              return (
                <>
                  <View
                    style={{
                      backgroundColor: colors.APP_LIGHT_BLUE_COLOR,
                      flexDirection: 'row',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                      paddingHorizontal: 10,
                    }}>
                    <Text style={{marginVertical: 5, fontWeight: 'bold'}}>
                      Day {elem}
                    </Text>
                    {/* <View style={{
                      alignSelf: 'flex-end'
                    }}>
                      <Text>Planned</Text>
                      <Text>Actual</Text>
                    </View> */}
                    <View>
                      <View style={{flexDirection: 'row'}}>
                        <View>
                          <Text style={styles.dayHoursTitle}></Text>
                        </View>
                        <View style={styles.hoursContainer}>
                          <Text style={styles.hours}>Planned</Text>
                          <Text style={styles.hours}>Actual</Text>
                        </View>
                      </View>

                      <View style={{flexDirection: 'row'}}>
                        <View>
                          <Text style={styles.dayHoursTitle}>Total</Text>
                        </View>
                        <View style={styles.hoursContainer}>
                          <Text style={styles.hours}>
                            {truckDrvingSchool?.counters[index]?.total_planned}
                          </Text>
                          <Text style={styles.hours}>
                            {truckDrvingSchool?.counters[index]?.total_actual}
                          </Text>
                        </View>
                      </View>

                      <View style={{flexDirection: 'row'}}>
                        <View>
                          <Text style={styles.dayHoursTitle}>Classroom</Text>
                        </View>
                        <View style={styles.hoursContainer}>
                          <Text style={styles.hours}>
                            {
                              truckDrvingSchool?.counters[index]
                                .classroom_total_planned
                            }
                          </Text>
                          <Text style={styles.hours}>
                            {
                              truckDrvingSchool?.counters[index]
                                .classroom_total_actual
                            }
                          </Text>
                        </View>
                      </View>

                      <View style={{flexDirection: 'row'}}>
                        <View>
                          <Text style={styles.dayHoursTitle}>On Road</Text>
                        </View>
                        <View style={styles.hoursContainer}>
                          <Text style={styles.hours}>
                            {
                              truckDrvingSchool?.counters[index]
                                .on_road_total_planned
                            }
                          </Text>
                          <Text style={styles.hours}>
                            {
                              truckDrvingSchool?.counters[index]
                                .on_road_total_actual
                            }
                          </Text>
                        </View>
                      </View>
                      <View style={{flexDirection: 'row'}}>
                        <View>
                          <Text style={styles.dayHoursTitle}>Yard</Text>
                        </View>
                        <View style={styles.hoursContainer}>
                          <Text style={styles.hours}>
                            {
                              truckDrvingSchool?.counters[index]
                                .yard_total_planned
                            }
                          </Text>
                          <Text style={styles.hours}>
                            {
                              truckDrvingSchool?.counters[index]
                                .yard_total_actual
                            }
                          </Text>
                        </View>
                      </View>

                      <View style={{flexDirection: 'row'}}>
                        <View>
                          <Text style={styles.dayHoursTitle}>BTW</Text>
                        </View>
                        <View style={styles.hoursContainer}>
                          <Text style={styles.hours}>
                            {
                              truckDrvingSchool?.counters[index]
                                .btw_total_planned
                            }
                          </Text>
                          <Text style={styles.hours}>
                            {
                              truckDrvingSchool?.counters[index]
                                .btw_total_actual
                            }
                          </Text>
                        </View>
                      </View>
                    </View>
                  </View>

                  {/* Update starts from here */}
                  {drivingSchool?.map((entity, mappingIndex) => {
                    return (
                      <>
                        <View
                          style={{
                            backgroundColor: colors.APP_LIGHT_GRAY_COLOR,
                          }}>
                          <Text
                            style={{
                              marginVertical: 5,
                              fontWeight: '500',
                              paddingHorizontal: scale(14),
                            }}>
                            {entity.title}
                          </Text>
                        </View>

                        <View
                          style={{
                            flex: 1,
                            flexDirection: 'row',
                            paddingHorizontal: scale(9),
                          }}>
                          <View style={{flex: 0.5, paddingVertical: 8}}>
                            <Text
                              style={{
                                fontWeight: '500',
                                fontSize: 16,
                                flex: 1,
                                borderWidth: 0.5,
                                padding: 6.4,
                              }}>
                              {'Location'}
                            </Text>
                            <Text
                              style={{
                                fontWeight: '500',
                                fontSize: 16,
                                flex: 1,
                                borderWidth: 0.5,
                                padding: 6.4,
                              }}>
                              {'Planned'}
                            </Text>
                            <Text
                              style={{
                                fontWeight: '500',
                                fontSize: 16,
                                flex: 1,
                                borderWidth: 0.5,
                                padding: 6.4,
                              }}>
                              {'Actual'}
                            </Text>
                            <Text
                              style={{
                                fontWeight: '500',
                                fontSize: 16,
                                flex: 1,
                                borderWidth: 0.5,
                                padding: 6.4,
                              }}>
                              {'Initials'}
                            </Text>
                          </View>
                          <View style={{flex: 0.5, paddingVertical: 8}}>
                            <TextInput
                              style={{
                                flex: 1,
                                borderWidth: 0.5,
                                paddingHorizontal: 5,
                              }}
                              placeholder={entity.location}
                              onChangeText={(location) => {
                                var data = truckDrvingSchool;
                                truckDrvingSchool.day_list[elem][
                                  mappingIndex
                                ].location = location;
                                this.setState({
                                  truckDrvingSchool: data,
                                });
                              }}
                              value={entity.location}
                            />

                            <TextInput
                              style={{
                                flex: 1,
                                borderWidth: 0.5,
                                paddingHorizontal: 5,
                              }}
                              onChangeText={(planned) => {
                                planned = planned.replace(/[^0-9.]/g, '');
                                var data = truckDrvingSchool;
                                truckDrvingSchool.day_list[elem][
                                  mappingIndex
                                ].planned = planned;
                                this.setState({
                                  truckDrvingSchool: data,
                                });
                              }}
                              value={entity.planned?.toString()}
                              keyboardType="numeric"
                            />

                            <TextInput
                              style={{
                                flex: 1,
                                borderWidth: 0.5,
                                paddingHorizontal: 5,
                              }}
                              onChangeText={(actual) => {
                                actual = actual.replace(/[^0-9.]/g, '');
                                var data = truckDrvingSchool;
                                truckDrvingSchool.day_list[elem][
                                  mappingIndex
                                ].actual = actual;
                                this.setState({
                                  truckDrvingSchool: data,
                                });
                              }}
                              value={entity.actual?.toString()}
                            />

                            <TextInput
                              style={{
                                flex: 1,
                                borderWidth: 0.5,
                                paddingHorizontal: 5,
                              }}
                              onChangeText={(initials) => {
                                // initials = initials.replace(/[^0-9.]/g, '');
                                var data = truckDrvingSchool;
                                truckDrvingSchool.day_list[elem][
                                  mappingIndex
                                ].initials = initials;
                                this.setState({
                                  truckDrvingSchool: data,
                                });
                              }}
                              value={entity.initials?.toString()}
                            />
                          </View>
                        </View>
                      </>
                    );
                  })}

                  <View style={{width: 100, height: 30}} />
                  <Text
                    style={{
                      fontSize: 20,
                      fontWeight: 'bold',
                    }}>
                    Comment
                  </Text>
                  <EvaluationField
                    start_time={this.state.start_time}
                    end_time={this.state.end_time}
                    // key={
                    //   truckDrvingSchool.day_list[elem][mappingIndex]
                    //     .comment
                    // }
                    title={''}
                    value={this.state.comments[elem]}
                    onChangeText={(text) => {
                      let tempComments = this.state.comments;
                      tempComments[elem] = text;
                      this.setState({
                        comments: tempComments,
                      });
                    }}
                  />
                  <View style={{width: 100, height: 30}} />
                  <EvaluationField
                    start_time={this.state.start_time}
                    end_time={this.state.end_time}
                    title=""
                    disabled={true}
                  />
                </>
              );
            })}
          </ScrollView>
        </ScreenWrapper>
        {this.props.shown && (
          <Footer>
            <TouchableOpacity
              onPress={() =>
                Alert.alert(
                  'Notification',
                  'secore reflect what the instructor needed to insure the drivers demonstration and understanding of each element \n \n 5 = No correction with no reinforcement \n \n 4 = Reinforcement understanding \n \n 3 = Corrected and reinforced understanding \n \n 2 = Multiple corrections needed until demonstrated correctly, reinforced understanding \n \n 1 = unacceptale and cretical error, driver failed to demonstrate element correctly or failed to convey understanding \n \n NA = Element was not applicable',
                )
              }>
              <Image
                source={INFO_ICON}
                style={{
                  resizeMode: 'contain',
                  height: 20,
                  width: 20,
                  paddingLeft: 10,
                }}
              />
            </TouchableOpacity>

            {/* <TouchableOpacity
              onPress={() => {
                this.setState({
                  start_time: moment().format('HH:mm'),
                  date: moment().format('YYYY-MM-DD'),
                });
              }}>
              <Image
                source={this.state.start_time ? PAUSE_ICON : PLAY_ICON}
                style={{resizeMode: 'contain', height: 25, width: 25}}
              />
            </TouchableOpacity> */}

            <View />
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
    // student_info: state.eveluationFlowReducer.student_info,
  };
};

export default connect(mapStateToProps, {fetchUserProfileAction}, null, {
  forwardRef: true,
})(DaysTruckSchoolTab);

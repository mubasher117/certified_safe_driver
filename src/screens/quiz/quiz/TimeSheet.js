/* eslint-disable prettier/prettier */
/* eslint-disable react-native/no-inline-styles */
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
  StyleSheet,
  Dimensions,
} from 'react-native';
import {connect} from 'react-redux';
import SplashScreen from 'react-native-splash-screen';
import {
  errorMessage,
  fetchUserProfileAction,
  hideSelector,
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
  SignaturePicker,
  DateTimePicker,
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
import TimesheetPreview from './preview/TimesheetPreview';

const {width, height} = Dimensions.get('window');
const data = [
  {
    title: 'Classroom',
    planned: '14.13',
    actual: '0.0',
  },
  {
    title: 'Yard Skills	',
    planned: '38.12',
    actual: '0.0',
  },
  {
    title: 'Behind the Wheel',
    planned: '55.75',
    actual: '0.0',
  },
];

const TdsStats = ({title, planned, actual}) => {
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
        <Text style={{marginVertical: 5, fontWeight: 'bold'}}>{title}</Text>
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
        </View>
        <View style={{flex: 0.5, paddingVertical: 8}}>
          <Text
            style={{
              flex: 1,
              borderWidth: 0.5,
              paddingHorizontal: 5,
            }}>
            {planned}
          </Text>

          <Text
            style={{
              flex: 1,
              borderWidth: 0.5,
              paddingHorizontal: 5,
            }}>
            {actual}
          </Text>
        </View>
      </View>
    </>
  );
};

class TimeSheet extends React.Component {
  state = {
    start_time: '12:30 AM',
    date: '',
    driverName: '',
    trainerName: '',
    history: '',
    checkBoxState: {},
    mounting: true,
    _dayTruckSchoolQuiz: dayTruckQuiz,
    startDate: '',
    endDate: '',
    totalDays: '',
    remarks: 'Temp',
    data_set: {
      en1: '',
      en2: '',
      en3: '',
      en1_1: '',
      en2_1: '',
      en3_1: '',
    },
    signature: null,
    timesheet_data: {},
    calculated_data: {},
    truckDrvingSchool: null,
    reloaded: false,
    showPreview: false,
    totalCalculation: {}
  };

  async componentDidMount() {
    const {
      company_info,
      student_info,
      selected_test,
      instructor_info,
    } = this.props.eveluationFlowReducer;
    this.setState({
      mounting: false,
      driverName: `${student_info?.first_name}  ${student_info?.last_name}`,
      trainerName: instructor_info?.full_name,
      truckDrvingSchool: this.props.truckDrvingSchool,
    });
    this.getTimesheetData();
    this.getTruckDrivingSchoolData();
  }
  saveInfo = async () => {
    let newState = this.state;
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    const apiInputData = {
      driver_trainer_signature: this.state.signature,
      start_date: this.state.timesheet_data.start_date,
      end_date: this.state.timesheet_data.end_date,
      remarks: this.state.timesheet_data.remarks,
      completed_statisfactorily_on: this.state.timesheet_data
        .completed_statisfactorily_on,
    };
    let res = await apiPatch(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/school-hours/`,
      apiInputData,
      true,
    );
    console.log('timesheet res: ', res);
    if (res && res.data) {
      // this.props.navigation.goBack()
      // errorMessage('Student Info Updated')
      // this.getData();
    }
    return true;
  };
  roundToTwo(num) {
    return +(Math.round(num + 'e+2') + 'e-2');
  }
  saveCalculatedData = (tdsData) => {
    const countDict = {
      classroomPlanned: 0,
      classroomActual: 0,
      yardPlanned: 0,
      yardActual: 0,
      btwPlanned: 0,
      btwActual: 0,
      totalPlanned: 0,
      totalActual: 0,
    };
    tdsData.map((data, index) => {
      countDict.classroomPlanned = this.roundToTwo(
        countDict.classroomPlanned + data.classroom_total_planned,
      );
      countDict.classroomActual = this.roundToTwo(
        countDict.classroomActual + data.classroom_total_actual,
      );
      countDict.yardPlanned = this.roundToTwo(
        countDict.yardPlanned + data.yard_total_planned,
      );
      countDict.yardActual = this.roundToTwo(
        countDict.yardActual + data.yard_total_actual,
      );
      countDict.btwPlanned = this.roundToTwo(
        countDict.btwPlanned + data.btw_total_planned,
      );
      countDict.btwActual = this.roundToTwo(
        countDict.btwActual + data.btw_total_actual,
      );
      // countDict.onRoadPlanned = this.roundToTwo(
      //   countDict.onRoadPlanned + data.btw_total_planned,
      // );
      // countDict.onRoadActual = this.roundToTwo(
      //   countDict.Actual + data.btw_total_actual,
      // );
      countDict.totalPlanned = this.roundToTwo(
        countDict.totalPlanned + data.total_planned,
      );
      countDict.totalActual = this.roundToTwo(
        countDict.totalActual + data.total_actual,
      );
    });
    this.setState({calculated_data: countDict});
  };
  componentDidUpdate(previousProps) {
    if (this.props.shown !== previousProps.shown && this.props.shown === true) {
      this.getTimesheetData();
      this.getTruckDrivingSchoolData();
    }
  }
  getTruckDrivingSchoolData = async () => {
    //TODO: how to upload signature
    let newState = this.state;
    // _.forEach(newState, (level1Val, _state) => {
    //   _.forEach(level1Val, (value, level2Key) => {
    //     if (level2Key == 'vrt')
    //       delete newState[_state][level2Key]
    //   })
    // })
    console.log('************ IN GET TRDC ************');
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/training-records/`,
    );
    if (res && res.data) {
      console.log('************* TRAINING RECORDS DATA OUT ****************');
      console.log(res.data);
      this.saveCalculatedData(res.data.counters);
      this.setState({
        totalDays: res.data?.days?.length,
        totalCalculation: res.data?.total
      });
    }
    return true;
  };
  getTimesheetData = async () => {
    let newState = this.state;
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/school-hours/`,
    );
    if (res && res.data) {
      console.log('******** Time Sheet Data ********');
      console.log(res.data);
      this.setState({
        timesheet_data: res.data,
        signature: res.data.driver_trainer_signature,
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
      startDate,
      endDate,
      totalDays,
      remarks,
      signature,
      timesheet_data,
      calculated_data,
      showPreview,
      totalCalculation
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
                        html: TimesheetPreview(
                          calculated_data,
                          timesheet_data,
                          this.state,
                          student_info,
                          company_info,
                          instructor_info,
                          INFO_ICON,
                        ),
                        fileName: `Timesheet_${student_info?.first_name}`,
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
                  // source={require('./preview/notes.html')}
                  source={{
                    html: TimesheetPreview(
                      calculated_data,
                      timesheet_data,
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
              title={'Trainee Name'}
              value={driverName}
              disabled={true}
            />

            {/* <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Start Date'}
              value={timesheet_data.start_date}
              disabled={true}
            /> */}
            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              rightArrow
              title={'Start Date'}
              onPress={() => {
                showPopup(
                  <DateTimePicker
                    onConfirm={(date) => {
                      console.log("DATE is: ", date)
                      this.setState({
                        timesheet_data: {...timesheet_data, start_date: date},
                      });
                    }}
                    date={this.state.timesheet_data.start_date}
                  />,
                );
              }}
              component={
                <View style={{flexDirection: 'row', alignItems: 'center'}}>
                  <Image
                    source={CALENDAR_ICON}
                    style={{height: scale(34), width: scale(34)}}
                  />
                  <Text>{this.state.timesheet_data.start_date}</Text>
                </View>
              }
            />
            {/* <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Finish Date'}
              value={timesheet_data.end_date}
              disabled={true}
            /> */}

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              rightArrow
              title={'End Date'}
              onPress={() => {
                showPopup(
                  <DateTimePicker
                    onConfirm={(date) => {
                      this.setState({
                        timesheet_data: {...timesheet_data, end_date: date},
                      });
                    }}

                    date={this.state.timesheet_data.end_date}
                  />,
                );
              }}
              component={
                <View style={{flexDirection: 'row', alignItems: 'center'}}>
                  <Image
                    source={CALENDAR_ICON}
                    style={{height: scale(34), width: scale(34)}}
                  />
                  <Text>{this.state.timesheet_data.end_date}</Text>
                </View>
              }
            />
            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Total Days'}
              disabled={true}
              hideInputField={true}
            />
            <Text style={styles.totalDays}>{totalDays}</Text>
            <TdsStats
              title="Total Training"
              planned={calculated_data.totalPlanned}
              actual={calculated_data.totalActual}
            />
            <TdsStats
              title="Classroom"
              planned={calculated_data.classroomPlanned}
              actual={calculated_data.classroomActual}
            />
            <TdsStats
              title="Yard Skills"
              planned={calculated_data.yardPlanned}
              actual={calculated_data.yardActual}
            />
            <TdsStats
              title="Behind the Wheel"
              planned={calculated_data.btwPlanned}
              actual={calculated_data.btwActual}
            />
            <TdsStats
              title="On Road"
              planned={totalCalculation.on_road_total_planned}
              actual={totalCalculation.on_road_total_actual}
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Remarks'}
              // onChangeText={(remarks) => this.setState({remarks})}
              value={remarks}
              hideInputField={true}
            />
            <View style={styles.remarksContainer}>
              <TextInput
                style={styles.remarks}
                multiline={true}
                value={timesheet_data.remarks}
                onChangeText={(remarks) =>
                  this.setState({
                    timesheet_data: {...timesheet_data, remarks: remarks},
                  })
                }
              />
            </View>

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Driver Trainer completed Satisfactorily on'}
              onChangeText={(value) => this.setState({
                timesheet_data: {...timesheet_data, completed_statisfactorily_on: value},
              })}
              value={timesheet_data.completed_statisfactorily_on}
            />
            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Driver Trainer Signature'}
              required
              onPress={() =>
                showSelector(
                  <SignaturePicker
                    handleSignature={(signature) => {
                      console.log('signature', signature);
                      this.setState({signature});
                      hideSelector();
                    }}
                  />,
                )
              }
              component={
                <View style={{flex: 1}}>
                  <Image
                    source={this.state.signature && {uri: this.state.signature}}
                    style={{width: 100, height: 38, resizeMode: 'cover'}}
                  />
                </View>
              }
            />
            <View style={styles.pageThreshold} />
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
})(TimeSheet);

const styles = StyleSheet.create({
  remarksContainer: {
    width: width,
    alignItems: 'center',
  },
  totalDays: {
    marginTop: 5,
    marginBottom: 5,
    marginLeft: 20,
  },
  remarks: {
    height: 100,
    width: '90%',
  },
  breakLine: {
    width: width,
    height: 1,
    backgroundColor: 'black',
  },
  pageThreshold: {
    width: width,
    height: 30,
  },
});

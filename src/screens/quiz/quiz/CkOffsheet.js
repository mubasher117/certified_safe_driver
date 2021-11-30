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
  EXPORT_ICON
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
import CkOffsheetPreview from './preview/CkOffsheetPreview';

const {width, height} = Dimensions.get('window');
// const data = [
//   {
//     title: 'Application',
//     department: 'HR',
//     initials: 'kfskf',
//     date: '22-44',
//   },
//   {
//     title: 'Reference Requests',
//     department: 'HR',
//     initials: '343',
//     date: 'rr3',
//   },
//   {
//     title: 'Road Test ',
//     department: 'HR',
//     initials: 'Trainer',
//     date: '12-43',
//   },
//   {
//     title: 'Pre Employment Drug Test',
//     department: 'HR',
//     initials: 'e2e23',
//     date: '33-44',
//   },
// ];

// const trainee_book_data = [
//   {
//     title: 'Drug & Alcohol Testing Handbook',
//     department: 'HR',
//     initials: 'kfskf',
//     date: '22-44',
//   },
//   {
//     title: "Knowledge Quiz's",
//     department: 'HR',
//     initials: '343',
//     date: 'rr3',
//   },
//   {
//     title: 'Road Test ',
//     department: 'HR',
//     initials: 'Trainer',
//     date: '12-43',
//   },
//   {
//     title:
//       'Completed Road Test from day 5 on largest equipment the driver is qualified to drive.	',
//     department: 'HR',
//     initials: 'e2e23',
//     date: '33-44',
//   },
// ];

class CkOffsheet extends React.Component {
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
    remarks: '',
    data_set: {},
    data: [],
    trainee_book_data: [],
    dfq_requirements: [],
    showPreview: false,
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
    });
    this.getDfqRequirements();
    this.getTraineeBookData();
  }

  componentDidUpdate(previousProps) {
    if (this.props.shown !== previousProps.shown && this.props.shown === true) {
      this.getDfqRequirements();
      this.getTraineeBookData();
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

  

  getDfqRequirements = async () => {
    let newState = this.state;
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/dqf-requirements/`,
    );
    if (res && res.data) {
      this.setState({
        dfq_requirements: res.data,
      });
    }
    return true;
  };
  getTraineeBookData = async () => {
    let newState = this.state;
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/trainee-book/`,
    );

    if (res && res.data) {
      console.log("*(*(*(*(*(*(*(*(*(*( TRAINEEE DATA *)*)*)*)*)*)*)*)*)")
      console.log(res.data)
      this.setState({
        trainee_book_data: res.data,
      });
    }
    return true;
  };

  saveInfo = async () => {
    let newState = this.state;
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    this.state.dfq_requirements?.map(async (dqf_requirement) => {
      let req_id = dqf_requirement.id;
      var apiInputData = {
        initials: dqf_requirement.initials,
        date: dqf_requirement.date,
        item: dqf_requirement.item?.id,
      };
      var res = await apiPatch(
          `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/dqf-requirements/${req_id}/`,
          apiInputData,
          true,
        );
    })
    this.state.trainee_book_data?.map(async (dqf_requirement) => {
      let req_id = dqf_requirement.id;
      var apiInputData = {
        initials: dqf_requirement.initials,
        date: dqf_requirement.date,
        item: dqf_requirement.item?.id,
      };
      var res = await apiPatch(
          `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/trainee-book/${req_id}/`,
          apiInputData,
          true,
        );
    })
    // const apiInputData = {
    //   driver_trainer_signature: this.state.signature,
    //   start_date: this.state.timesheet_data.start_date,
    //   end_date: this.state.timesheet_data.end_date,
    //   remarks: this.state.timesheet_data.remarks,
    //   completed_statisfactorily_on: this.state.timesheet_data.completed_statisfactorily_on,
    // };
    // let res = await apiPut(
    //   `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/school-hours/`,
    //   apiInputData,
    //   true,
    // );
    // console.log('timesheet res: ', res);
    // if (res && res.data) {
    //   // this.props.navigation.goBack()
    //   // errorMessage('Student Info Updated')
    //   // this.getData();
    // }
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
      data,
      trainee_book_data,
      dfq_requirements,

    showPreview,
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
                        html: CkOffsheetPreview(
                          dfq_requirements,
                          trainee_book_data,
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
                    html: CkOffsheetPreview(
                      dfq_requirements,
                      trainee_book_data,
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
              title={'Driver'}
              onChangeText={(driverName) => this.setState({driverName})}
              value={driverName}
            />
            <View style={styles.breakLine} />
            <View style={styles.titleContainer}>
              <Text style={styles.title}>DQF Requirements</Text>
            </View>
            {dfq_requirements.map((training, index) => {
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
                      {training.item.title}
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
                        {'Department'}
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
                      <Text
                        style={{
                          fontWeight: '500',
                          fontSize: 16,
                          flex: 1,
                          borderWidth: 0.5,
                          padding: 6.4,
                        }}>
                        {'Date'}
                      </Text>
                    </View>
                    <View style={{flex: 0.5, paddingVertical: 8}}>
                      <TextInput
                        style={{
                          flex: 1,
                          borderWidth: 0.5,
                          paddingHorizontal: 5,
                        }}
                        onChangeText={(department) => {
                          const tempData = dfq_requirements;
                          tempData[index].department = department;
                          this.setState({
                            dfq_requirements: tempData,
                          });
                        }}
                        value={dfq_requirements[
                          index
                        ].item.department_display_name?.toString()}
                      />

                      <TextInput
                        style={{
                          flex: 1,
                          borderWidth: 0.5,
                          paddingHorizontal: 5,
                        }}
                        onChangeText={(initials) => {
                          const tempData = dfq_requirements;
                          tempData[index].initials = initials;
                          this.setState({
                            dfq_requirements: tempData,
                          });
                        }}
                        value={dfq_requirements[index].initials?.toString()}
                      />

                      <TextInput
                        style={{
                          flex: 1,
                          borderWidth: 0.5,
                          paddingHorizontal: 5,
                        }}
                        onChangeText={(date) => {
                          const tempData = dfq_requirements;
                          tempData[index].date = date;
                          this.setState({
                            dfq_requirements: tempData,
                          });
                        }}
                        value={dfq_requirements[index].date?.toString()}
                      />
                    </View>
                  </View>
                </>
              );
            })}

            <View style={styles.titleContainer}>
              <Text style={styles.title}>Trainee Book</Text>
            </View>

            {trainee_book_data.map((training, index) => {
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
                      {training.item.title}
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
                        {'Department'}
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
                      <Text
                        style={{
                          fontWeight: '500',
                          fontSize: 16,
                          flex: 1,
                          borderWidth: 0.5,
                          padding: 6.4,
                        }}>
                        {'Date'}
                      </Text>
                    </View>
                    <View style={{flex: 0.5, paddingVertical: 8}}>
                      <TextInput
                        style={{
                          flex: 1,
                          borderWidth: 0.5,
                          paddingHorizontal: 5,
                        }}
                        onChangeText={(department) => {
                          const tempData = trainee_book_data;
                          tempData[index].department = department;
                          this.setState({
                            trainee_book_data: tempData,
                          });
                        }}
                        value={trainee_book_data[
                          index
                        ].item?.department_display_name?.toString()}
                      />

                      <TextInput
                        style={{
                          flex: 1,
                          borderWidth: 0.5,
                          paddingHorizontal: 5,
                        }}
                        onChangeText={(initials) => {
                          const tempData = trainee_book_data;
                          tempData[index].initials = initials;
                          this.setState({
                            trainee_book_data: tempData,
                          });
                        }}
                        value={trainee_book_data[index].initials?.toString()}
                      />

                      <TextInput
                        style={{
                          flex: 1,
                          borderWidth: 0.5,
                          paddingHorizontal: 5,
                        }}
                        onChangeText={(date) => {
                          const tempData = trainee_book_data;
                          tempData[index].date = date;
                          this.setState({
                            trainee_book_data: tempData,
                          });
                        }}
                        value={trainee_book_data[index].date?.toString()}
                      />
                    </View>
                  </View>
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
})(CkOffsheet);

const styles = StyleSheet.create({
  titleContainer: {
    width: width,
    alignItems: 'center',
    marginTop: 20,
    marginBottom: 10,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
  },
  breakLine: {
    width: width,
    height: 1,
    backgroundColor: 'black',
  },
});

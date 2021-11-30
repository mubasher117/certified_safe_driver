/* eslint-disable comma-dangle */
/* eslint-disable prettier/prettier */
import React from 'react';
import {
  StatusBar,
  View,
  Image,
  ScrollView,
  TouchableOpacity,
  Modal,
  Alert,
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
  Selector,
  UserField,
  DateTimePicker,
  ScreenWrapper,
  EvaluationField,
  EvaluationYesNoOptionField,
  TestSelector,
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
import {
  updateCompanyInfo,
  updateStudentInfo,
  updateInstructorInfo,
  updateGroupInfo,
  updateGroupModeInfo,
  updateSelectedTest,
  updateSelectedTestInfo,
  updateTabChangeErrorMessage,
} from '../../../actions';
import _ from 'lodash';
import {getObjectDiff, getDataDiff} from '../../../utils/function';
import moment from 'moment';
import {Switch} from 'react-native-gesture-handler';

import { WebView } from 'react-native-webview';
import RNHTMLtoPDF from 'react-native-html-to-pdf';
import Share from 'react-native-share';
import InfoPreview from './preview/InfoPreview';
class InfoTab extends React.Component {
  state = {
    date: '',
    company: null,
    instructor: null,
    student: '',
    driver_license_expire_date: '',
    driver_license_num: 0,
    history_reviewed: false,
    class: '',
    endorsements: false,
    dot_expire_date: '',
    start_time: '',
    end_time: '',
    location: '',
    corrective_lens_required: false,
    restrictions: '',
    comments: '',
    change_job: false,
    defensive_driving_quiz: false,
    distracted_quiz: false,
    injury_date: '',
    accident_date: '',
    taw_start_date: '',
    taw_end_date: '',
    lost_start_time: '',
    return_to_work_date: '',
    notes: '',
    notesImage: '',
    driver_class: '',
    FSLoading: false,
    showPreview: false
  };

  async componentDidMount() {
    if (this.props.eveluationFlowReducer.student_info) {
      // this.setState({
      //   company: this.props.eveluationFlowReducer.company_info,
      //   instructor: this.props.eveluationFlowReducer.instructor_info,
      //   student: this.props.eveluationFlowReducer.student_info,
      // })

      this.getInfo();
    }
    // if (__DEV__) {

    //   this.setState({ power_unit_no: 23 })
    // }
  }

  DataPapulate = async (data) => {
    // await this.props.updateSelectedTestInfo(data)
    // console.log('updateSelectedTestInfo DataPapulate: ', data);
    this.setState({
      company: this.props.eveluationFlowReducer.company_info,
      instructor: this.props.eveluationFlowReducer.instructor_info,
      student: this.props.eveluationFlowReducer.student_info,
      date: data.date_of_hire,
      driver_license_expire_date: data.driver_license_expire_date,
      driver_license_num: data.driver_license_number,
      history_reviewed: data.history_reviewed,
      class: data.driver_license_class,
      endorsements: data.endorsements,
      dot_expire_date: data.dot_expiration_date,
      start_time: data.start_time,
      end_time: data.end_time,
      // location: data.location,
      location:
        this.props.eveluationFlowReducer.selectedTestInfo &&
        this.props.eveluationFlowReducer.selectedTestInfo.location,
      corrective_lens_required: data.corrective_lense_required,
      restrictions: data.restrictions,
      comments: data.comments,
      change_job: data.change_job,
      defensive_driving_quiz: data.defensive_driving_quiz,
      distracted_quiz: data.distracted_quiz,
      taw_start_date: data.taw_start_date,
      taw_end_date: data.taw_end_date,
      injury_date: data.injury_date,
      accident_date: data.accident_date,
      lost_start_time: data.lost_time_start_date,
      return_to_work_date: data.return_work_date,
      notes: '',
      driver_class: data.driver_license_class,
    });
  };

  FieldClears = async (student) => {
    await this.props.updateSelectedTestInfo(null);
    if (student) {
      this.setState({student: ''});
      await this.props.updateStudentInfo(null);
    }
    this.setState(
      {
        date: '',
        instructor: '',
        // student: '',
        driver_license_expire_date: '',
        driver_license_num: '',
        history_reviewed: false,
        class: '',
        endorsements: false,
        dot_expire_date: '',
        start_time: '',
        end_time: '',
        location: '',
        corrective_lens_required: false,
        restrictions: '',
        comments: '',
        change_job: false,
        change_of_equipment: false,
        distracted_quiz: false,
        taw_start_date: '',
        taw_end_date: '',
        injury_date: '',
        accident_date: '',
        lost_start_time: '',
        return_to_work_date: '',
        notes: '',
        driver_class: '',
      },
      () => {
        this.props.updateTabChangeErrorMessage(false);
      },
    );
  };

  reload = async () => {
    await this.loadTest(this.state.loadedTest);
    return true;
  };

  getInfo = async () => {
    this.setState({FSLoading: true});
    let res = await apiGet(
      `/api/v1/students/${this.props.eveluationFlowReducer.student_info?.id}/tests/`,
    );
    this.setState({FSLoading: false});
    console.log('student tests res: ', res);
    if (res && res.data && res.data.results) {
      // let student=
      const pendingTest = _.find(
        res.data.results,
        (res) => res.status == 'pending',
      );
      if (pendingTest) {
        this.loadTest(pendingTest);
      } else {
        //if no pending test
        alert('No pending test found');
        this.props.updateTabChangeErrorMessage('Please start a test');
        if (res.data.results && res.data.results[0])
          {this.loadTest(res.data.results[0]);}
        // this.createNewTest()
      }
    } else {
      alert('could not load test information');
    }
  };

  loadTest = async (pendingTest) => {
    console.log('loading test', pendingTest);
    this.setState({loadedTest: pendingTest});
    let res = await apiGet(
      `/api/v1/students/${this.props.eveluationFlowReducer.student_info?.id}/tests/${pendingTest.id}/info/`,
    );
    if (res && res.data) {
      console.log('student test info', res.data);
      await this.props.updateCompanyInfo(res.data.info.company);
      let data = {...pendingTest, instructor: res.data.instructor};
      this.processTestInfo(data);
      this.props.updateSelectedTestInfo(res.data);
      this.DataPapulate({...res.data, ...pendingTest.student.info});
    }
    return true;
  };

  createNewTest = async () => {
    let res = await apiPost(
      `/api/v1/students/${this.state.student.id}/tests/`,
      {name: new Date().toUTCString()},
    );
    console.log('add new test res', res);
    if (res && res.data) {
      const pendingTest = res.data;
      res = await apiGet(
        `/api/v1/students/${this.props.eveluationFlowReducer.student_info?.id}/tests/${pendingTest.id}/info/`,
      );
      if (res && res.data) {
        let data = {...pendingTest, instructor: res.data.instructor};
        this.processTestInfo(data);
        this.props.updateSelectedTestInfo(res.data);
        this.DataPapulate({...res.data, ...pendingTest.student.info});
      }
      return true;
    } else {
      //could not create new test
      return false;
    }
  };

  // componentDidUpdate(prevProps, prevState) {
  //   if (this.props.shown && prevProps.tabChangeErrorMessage == this.props.tabChangeErrorMessage) {
  //     const isDiff = getDataDiff({ ...this.state.apiData }, this.state)
  //     console.log('isDiff Info', isDiff)
  //     if (isDiff) {
  //       if (this.props.tabChangeErrorMessage == false)
  //         this.props.updateTabChangeErrorMessage('Please save or discard your changes')
  //     } else {
  //       if (this.props.tabChangeErrorMessage !== false)
  //         this.props.updateTabChangeErrorMessage(false)
  //     }
  //   }
  // }

  componentDidUpdate(prevProps, prevState) {
    if (
      this.props.shown &&
      prevProps.tabChangeErrorMessage == this.props.tabChangeErrorMessage
    ) {
      const isDiff = getObjectDiff(prevState, this.state);
      // console.log('isDiff', isDiff)
      if (isDiff) {
        if (this.props.tabChangeErrorMessage == false)
          {this.props.updateTabChangeErrorMessage(
            'Please save or discard your changes',
          );}
      } else {
        if (this.props.tabChangeErrorMessage !== false)
          {this.props.updateTabChangeErrorMessage(false);}
      }
    }
  }

  processTestInfo = async (pendingTest) => {
    await this.props.updateSelectedTest(pendingTest);
    await this.props.updateStudentInfo(pendingTest.student);
    await this.props.updateInstructorInfo(pendingTest.instructor);
  };

  startTest = async () => {
    let date = new Date();
    let hours = date.getHours();
    let minutes = date.getMinutes();
    console.log('time', `${hours}:${minutes}`);
    this.setState({start_time: `${hours}:${minutes}`});
  };

  saveInfo = async () => {
    let data = {
      // "user": {
      //   "first_name": this.state.student.first_name,
      //   "last_name": this.state.student.last_name,
      //   "middle_name": this.state.student.middle_name,
      //   "email": this.state.student.email,
      //   // "username": this.state.student.username, // this.state.student.first_name + this.state.student.first_name + '@',
      //   "is_student": true
      // },
      date_of_hire: this.state.date,
      // "driver_license_number": this.state.driver_license_num,
      // "driver_license_expire_date": this.state.driver_license_expire_date,
      // "endorsements": this.state.endorsements,
      // "driver_license_class": this.state.class,
      location: this.state.location,
      // "corrective_lense_required": this.state.corrective_lens_required,
      // "dot_expiration_date": this.state.dot_expire_date,
      history_reviewed: this.state.history_reviewed,
      start_time: this.state.start_time, // this.state.start_time,
      end_time: this.state.end_time, // this.state.end_time,
      restrictions: this.state.restrictions,
      comments: this.state.comments,
      change_job: this.state.change_job,
      defensive_driving_quiz: this.state.defensive_driving_quiz,
      distracted_quiz: this.state.distracted_quiz,
      injury_date: this.state.injury_date,
      accident_date: this.state.accident_date,
      taw_start_date: this.state.taw_start_date,
      taw_end_date: this.state.taw_end_date,
      lost_time_start_date: this.state.lost_start_time,
      return_work_date: this.state.return_to_work_date,
      // "company": this.state.company.id
    };
    if (this.state.instructor && this.state.instructor.id)
      {data.instructor = this.state.instructor.id;}

    console.log('saveInfo data', data);
    let endpoint = '';
    if (this.props.eveluationFlowReducer.selected_test) {
      endpoint = `/api/v1/students/${this.state.student.id}/tests/${this.props.eveluationFlowReducer.selected_test?.id}/info/`;
      const res = apiPatch(endpoint, data, true);
      if (res && res.data) {
        console.log('************* INFO DATA OUT ****************');
        console.log(res.data);
      }
      Alert.alert('Test Info Saved Successfuly.');
    } else {
      //if no pending test
      return false;
    }

    // let res = await apiPatch(endpoint, data, true)
    // console.log(`patchTestInfo res: `, res)
    // if (res && res.data) {
    //   // this.props.navigation.goBack()
    //   // errorMessage('Student Info Updated')
    //   // this.getInfo();
    //   await this.props.updateSelectedTestInfo(res.data)
    // }
    return true;
  };
  preview = async() => {
    await this.getDataForPreview();
    this.setState({showPreview: true});


  }
  getDataForPreview = async() => {
    // getDfqRequirements
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
    // trainee book data
      res = await apiGet(
        `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/trainee-book/`,
      );

      if (res && res.data) {
        console.log('*(*(*(*(*(*(*(*(*(*( TRAINEEE DATA *)*)*)*)*)*)*)*)*)');
        console.log(res.data);
        this.setState({
          trainee_book_data: res.data,
        });
      }
      // truck driving school
      res = await apiGet(
        `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/training-records/`,
      );
      if (res && res.data) {
        this.saveCalculatedData(res.data.counters);
        let tempComments = {}
        res.data?.comments.map((item, index) => {
          tempComments[item.day] = item.body;
        })
        this.setState({
          truckDrvingSchool: res.data,
          comments: tempComments
        });
      }

      // timesheet data 
      res = await apiGet(
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

      await this.getDefensiveQuizQuestions();
      await this.getDistractedQuizQuestions();




      return true;

  }
  roundToTwo(num) {
    return +(Math.round(num + 'e+2') + 'e-2');
  }

  getDefensiveQuizQuestions = async () => {
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet('/api/v1/quizes/defensive_driving_questions/');
    if (res && res.data) {
      // console.log(res.data);

      res.data.map((question, idx) => {
        res.data[idx].isTrue = null;
        if (question?.correct_choices?.length > 1) {
          res.data[idx].remainingCorrectChoices =
            question?.correct_choices?.length;
        }
        question.choices.map((choice, innerIdx) => {
          res.data[idx].choices[innerIdx].isChecked = false;
        });
      });
      this.setState({
        _defenseQuizes: res.data,
      });
    }
    return true;
  };

  getDistractedQuizQuestions = async () => {
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet('/api/v1/quizes/distracted_questions/');
    if (res && res.data) {
      // console.log(res.data);

      res.data.map((question, idx) => {
        res.data[idx].isTrue = null;
        if (question?.correct_choices?.length > 1) {
          res.data[idx].remainingCorrectChoices =
            question?.correct_choices?.length;
        }
        question.choices.map((choice, innerIdx) => {
          res.data[idx].choices[innerIdx].isChecked = false;
          res.data[idx].choices[innerIdx].isTrue = null;
        });
      });
      this.setState({
        _distractedQuizes: res.data,
      });
    }
    return true;
  };

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
      countDict.totalPlanned = this.roundToTwo(
        countDict.totalPlanned + data.total_planned,
      );
      countDict.totalActual = this.roundToTwo(
        countDict.totalActual + data.total_actual,
      );
    });
    this.setState({calculated_data: countDict});
  };

  render() {
    const {
      date,
      company,
      instructor,
      student,
      driver_license_expire_date,
      driver_license_num,
      driver_class,
      endorsements,
      dot_expire_date,
      start_time,
      end_time,
      location,
      comments,
      restrictions,
      dfq_requirements,
      trainee_book_data,
      truckDrvingSchool,
      timesheet_data,
      calculated_data
    } = this.state;

    const {
      company_info,
      student_info,
      selected_test,
      group_info, groupMode,
      instructor_info
    } = this.props.eveluationFlowReducer;
    const show = {flex: 1, height: undefined};
    const hide = {flex: 0, height: 0};
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
                      let options = {
                        html: InfoPreview(
                          this.state,
                          student_info,
                          company_info,
                          instructor_info,
                          dfq_requirements,
                          trainee_book_data,
                          truckDrvingSchool,
                          timesheet_data,
                          calculated_data,
                        ),
                        fileName: `student_${student_info?.id}_NOTES`,
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
                    html: InfoPreview(
                      this.state,
                      student_info,
                      company_info,
                      instructor_info,
                      dfq_requirements,
                      trainee_book_data,
                      truckDrvingSchool,
                      timesheet_data,
                      calculated_data,
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
              // required
              rightArrow
              title={'Date'}
              onPress={() => {
                showPopup(
                  <DateTimePicker
                    onConfirm={(date) => {
                      this.setState({date: date});
                    }}
                  />,
                );
              }}
              component={
                <View style={{flexDirection: 'row', alignItems: 'center'}}>
                  <Image
                    source={CALENDAR_ICON}
                    style={{height: scale(34), width: scale(34)}}
                  />
                  <Text>{date}</Text>
                </View>
              }
            />

            {groupMode ? (
              <EvaluationField
                start_time={true}
                end_time={false}
                // required
                backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                title={'Group'}
                onPress={() =>
                  showSelector(
                    <Selector
                      title={'Groups'}
                      endpoint={'/api/v1/student-groups/'}
                      onSelect={async (item) => {
                        // console.log('item company: ', item);
                        // this.setState({ group_info: item });
                        await this.props.updateGroupInfo(item);
                        // await this.props.updateCompanyInfo(item);
                        this.FieldClears(true);
                      }}
                    />,
                  )
                }
                component={
                  <View
                    style={{
                      flexDirection: 'row',
                      alignItems: 'center',
                      justifyContent: 'space-between',
                      flex: 1,
                    }}>
                    <Text>{group_info && `${group_info.name}`}</Text>
                    <Image
                      source={RIGHT_ARROW_ICON}
                      style={{height: scale(12), width: scale(12)}}
                    />
                  </View>
                }
              />
            ) : (
              <EvaluationField
                start_time={true}
                end_time={false}
                // required
                backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                title={'Company'}
                onPress={() =>
                  showSelector(
                    <Selector
                      title={'Companies'}
                      endpoint={'/api/v1/companies/'}
                      onSelect={async (item) => {
                        // console.log('item company: ', item);
                        this.setState({company: item});
                        await this.props.updateCompanyInfo(item);
                        this.FieldClears(true);
                      }}
                    />,
                  )
                }
                component={
                  <View
                    style={{
                      flexDirection: 'row',
                      alignItems: 'center',
                      justifyContent: 'space-between',
                      flex: 1,
                    }}>
                    <Text>{company && `${company.name}`}</Text>
                    <Image
                      source={RIGHT_ARROW_ICON}
                      style={{height: scale(12), width: scale(12)}}
                    />
                  </View>
                }
              />
            )}

            <EvaluationField
              start_time={true}
              end_time={false}
              // required
              backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
              title={'Student'}
              onPress={() => {
                if (groupMode) {
                  if (group_info == null) {
                    errorMessage('Please select group first!');
                    return;
                  }
                } else if (company == null) {
                  errorMessage('Please select company first!');
                  return;
                }
                showSelector(
                  <Selector
                    title={'Student'}
                    // displayKey={'first_name'}
                    displayComponent={(item) => (
                      <Text>
                        {item.first_name} {item.last_name}
                      </Text>
                    )}
                    endpoint={
                      groupMode
                        ? `/api/v1/students/?group_id=${group_info.id}`
                        : `/api/v1/students/?company_id=${company.id}`
                    }
                    // endpoint={`/api/v1/students/`}
                    onSelect={async (item) => {
                      // console.log('item student: ', item);
                      this.setState({student: item});
                      await this.props.updateStudentInfo(item);
                      this.FieldClears();
                      this.getInfo();
                    }}
                  />,
                );
              }}
              component={
                <View
                  style={{
                    flexDirection: 'row',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    flex: 1,
                  }}>
                  <Text>
                    {student && `${student.first_name} ${student.last_name}`}
                  </Text>
                  <Image
                    source={RIGHT_ARROW_ICON}
                    style={{height: scale(12), width: scale(12)}}
                  />
                </View>
              }
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              rightArrow
              title={'Driver License Expiration Date'}
              onPress={() => {
                errorMessage(
                  'Notification \n \n Driver License Expiration Date can\'t be changed. it can be updated by editing the student info!',
                );
              }}
              component={
                <View style={{flexDirection: 'row', alignItems: 'center'}}>
                  <Image
                    source={CALENDAR_ICON}
                    style={{height: scale(34), width: scale(34)}}
                  />
                  <Text>{driver_license_expire_date}</Text>
                </View>
              }
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              title={'Driver License Number'}
              onPress={() => {
                errorMessage(
                  'Notification \n \n Driver license number can\'t be changed. it can be updated by editing the student info!',
                );
              }}
              component={<Text>{driver_license_num}</Text>}
            />

            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'History Reviewed'}
              onChange={(item) => this.setState({history_reviewed: item})}
              value={this.state.history_reviewed}
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              title={'Class'}
              onPress={() => {
                errorMessage('Change in student data');
              }}
              component={
                <Text>
                  {driver_class && driver_class.name
                    ? driver_class.name
                    : driver_class}
                </Text>
              }
            />

            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Endorsements'}
              // onChange={(endorsements) => this.setState({ endorsements })}
              onPress={() => {
                errorMessage('Change in student data');
              }}
              value={endorsements}
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              rightArrow
              title={'DOT Expiration Date'}
              onPress={() => {
                errorMessage('Change in student data');
              }}
              component={<Text>{dot_expire_date}</Text>}
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              title={'Start Time'}
              editable={false}
              onChangeText={(start_time) => this.setState({start_time})}
              value={start_time}
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              title={'End Time'}
              editable={false}
              onChangeText={(end_time) => this.setState({end_time})}
              value={end_time}
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              title={'Location'}
              onChangeText={(location) => this.setState({location})}
              value={location}
            />

            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Corrective lens required'}
              // onChange={(corrective_lens_required) => this.setState({ corrective_lens_required })}
              onPress={() => {
                errorMessage('Change in student data');
              }}
              value={this.state.corrective_lens_required}
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              title={'Restrictions'}
              onChangeText={(restrictions) => this.setState({restrictions})}
              value={restrictions}
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              disabled
              // required
              backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
              title={'Instructor'}
              onPress={() =>
                showSelector(
                  <Selector
                    title={'Instructor'}
                    endpoint={`/api/v1/instructors/?company_id=${company.id}`}
                    displayComponent={(item) => (
                      <Text>
                        {item.first_name} {item.last_name}
                      </Text>
                    )}
                    onSelect={async (item) => {
                      console.log('item Instructor: ', item);
                      await this.props.updateInstructorInfo(item);
                      this.setState({instructor: item});
                    }}
                  />,
                )
              }
              component={
                <View
                  style={{
                    flexDirection: 'row',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    flex: 1,
                  }}>
                  <Text>
                    {instructor &&
                      `${instructor.first_name} ${instructor.last_name}`}
                  </Text>
                  {/* <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} /> */}
                </View>
              }
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              title={'Comments'}
              onChangeText={(comments) => this.setState({comments})}
              value={comments}
            />

            {/* <View style={{backgroundColor: colors.APP_LIGHT_BLUE_COLOR}}>
              <Text
                style={{
                  marginHorizontal: 10,
                  marginVertical: 5,
                  fontSize: 14,
                }}>{'Select the type of training completed'}</Text>
            </View>

            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Defensive Driving Quiz'}
              onChange={(change_job) => this.setState({change_job})}
              value={this.state.change_job}
            />
            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Defensive Driving Quiz'}
              onChange={(defensive_driving_quiz) =>
                this.setState({defensive_driving_quiz})
              }
              value={this.state.defensive_driving_quiz}
            />
            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Distracted Quiz'}
              onChange={(distracted_quiz) => this.setState({distracted_quiz})}
              value={this.state.distracted_quiz}
            /> */}

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Notes'}
              onChangeText={(notes) => this.setState({notes})}
              value={this.state.notes}
            />
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

            {this.props.eveluationFlowReducer.selected_test &&
              this.props.eveluationFlowReducer.selected_test.status ==
                'pending' && (
                <TouchableOpacity
                  onPress={() => {
                    console.log('this.state', this.state);
                    if (this.state.student) {
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
                                  {
                                    end_time: moment().format('HH:mm'),
                                    FSLoading: true,
                                  },
                                  async () => {
                                    await this.saveInfo();
                                    const res = await apiPatch(
                                      `/api/v1/students/${this.state.student.id}/tests/${this.props.eveluationFlowReducer.selected_test?.id}/`,
                                      {status: 'completed'},
                                      true,
                                    );
                                    if (res && res.data) {
                                      this.loadTest(res.data);
                                    }
                                    // await this.props.updateSelectedTest(res.data)
                                    this.setState({FSLoading: false});
                                  },
                                );
                              },
                            },
                          ],
                          {cancelable: false},
                        );
                      } else {
                        this.setState({start_time: moment().format('HH:mm')});
                      }
                    } else {
                      alert('Select a student');
                    }
                  }}>
                  <Image
                    source={start_time ? PAUSE_ICON : PLAY_ICON}
                    style={{resizeMode: 'contain', height: 25, width: 25}}
                  />
                </TouchableOpacity>
              )}
            {/* TODO:delete test option */}

            {/* {this.props.eveluationFlowReducer.selected_test.status == 'pending' && <TouchableOpacity onPress={async () => {
            if (this.state.end_time) {
              const res = await apiPatch(`/api/v1/students/${this.state.student.id}/tests/${this.props.eveluationFlowReducer.selected_test?.id}/`, { status: 'complete' })
              if (res && res.data)
                await this.props.updateSelectedTest(res.data)
            } else {
              Alert.alert('Stop the test first')
            }

          }}>
            <Image source={CLOSE_ICON} style={{ resizeMode: 'contain', height: 20, width: 20 }} />
          </TouchableOpacity>} */}

            <View style={{flexDirection: 'row', alignItems: 'center'}}>
              <Text style={{marginRight: 5}}>Group</Text>
              <Switch
                // trackColor={{ false: "#767577", true: "#81b0ff" }}
                // thumbColor={isEnabled ? "#f5dd4b" : "#f4f3f4"}
                // ios_backgroundColor="#3e3e3e"
                onValueChange={(groupMode) => {
                  this.props.updateGroupModeInfo(groupMode);
                  this.FieldClears(true);
                }}
                value={groupMode}
              />
            </View>

            <TouchableOpacity
              onPress={() => {
                if (this.props.eveluationFlowReducer.student_info) {
                  showSelector(
                    <TestSelector
                      // topComponent={}
                      title={'Tests'}
                      createNewTest={this.createNewTest}
                      // endpoint={`/api/v1/students/${this.props.eveluationFlowReducer.student_info?.id}/tests/`}
                      studentId={
                        this.props.eveluationFlowReducer.student_info?.id
                      }
                      onSelect={async (item) => {
                        console.log('previosu test item: ', item);
                        this.loadTest(item);
                        //TODO:add option to create new test
                      }}
                    />,
                  );
                  showPopup;
                } else {
                  Alert.alert('Please select student');
                }
              }}
              // onPress={() => Alert.alert(
              //   'Notification',
              //   `\nCurrent class is not saved and changes will be lost. Do you want to continue?`,
              //   [
              //     {
              //       text: 'Cancel',
              //       onPress: () => console.log('Cancel Pressed'),
              //       style: 'cancel',
              //     },
              //     {
              //       text: 'Yes',
              //       onPress: () => console.log('Yes Pressed')
              //     },
              //   ],
              //   { cancelable: false },
              // )}
            >
              <Image
                source={PLUS_ICON}
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
        <Modal
          animationType="fade"
          transparent={true}
          visible={this.state.FSLoading}
          onRequestClose={() => {}}>
          <View
            style={{
              flex: 1,
              justifyContent: 'center',
              alignItems: 'center',
              backgroundColor: 'rgba(0,0,0,0.2)',
            }}>
            <Loader color={'white'} />
          </View>
        </Modal>
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

export default connect(
  mapStateToProps,
  {
    fetchUserProfileAction,
    updateCompanyInfo,
    updateStudentInfo,
    updateInstructorInfo,
    updateGroupInfo,
    updateGroupModeInfo,
    updateSelectedTest,
    updateSelectedTestInfo,
    updateTabChangeErrorMessage,
  },
  null,
  {forwardRef: true},
)(InfoTab);

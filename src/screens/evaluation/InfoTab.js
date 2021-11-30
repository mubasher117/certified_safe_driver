import React from 'react';
import { StatusBar, View, Image, ScrollView, TouchableOpacity, Modal, Alert } from 'react-native';
import { connect } from 'react-redux';
import SplashScreen from 'react-native-splash-screen'
import { errorMessage, fetchUserProfileAction, showPopup, showSelector } from '../../actions';
import { PLATFORM_IOS, INFO_ICON, PAUSE_ICON, PLAY_ICON, CLOSE_ICON, PLUS_ICON, EXPORT_ICON } from '../../constants';
import * as colors from '../../styles/colors';
import { Loader, Text, Header, Footer, Selector, UserField, DateTimePicker, ScreenWrapper, EvaluationField, EvaluationYesNoOptionField, TestSelector } from '../../components';
import { SEARCH_ICON, SCREEN_WIDTH, CALENDAR_ICON, RIGHT_ARROW_ICON, ALL_US_STATES} from '../../constants';
import { scale } from '../../utils/scale';
import { apiGet, apiPatch, apiPut, apiPost } from '../../utils/http';
import { updateCompanyInfo, updateStudentInfo, updateInstructorInfo, updateGroupInfo, updateGroupModeInfo, updateSelectedTest, updateSelectedTestInfo, updateTabChangeErrorMessage } from '../../actions'
import _, {isNumber} from 'lodash';
import { getObjectDiff, getDataDiff } from '../../utils/function';
import moment from 'moment'
import { Switch } from 'react-native-gesture-handler';
import { PreTripsDataModalA } from '../../utils/PreTripsDataModalA';
import {BTWModalA} from '../../utils/BTWModalA';
import {SwpDataModals} from '../../utils/SwpDataModals';
import {VRTDataModals} from '../../utils/VRTDataModals';
import AsyncStorage from '@react-native-community/async-storage';


let _class = 'class_a';

let PreTripsDataModal = PreTripsDataModalA;
let BTWModal = BTWModalA;

import { WebView } from 'react-native-webview';
import RNHTMLtoPDF from 'react-native-html-to-pdf';
import Share from 'react-native-share';
import INFO from './preview/INFOPreviewHTML';
import SWPPreviewHTML from './preview/SWPPreviewHTML';

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
    equipement: false,
    pre_post_trip: false,
    behind_the_wheel: false,
    eye_movement: false,
    safe_work_practice: false,
    production: false,
    vehicle_road_test: false,
    passenger_evacuation: false,
    passenger_pre_trip: false,
    new_hire: false,
    near_miss: false,
    incident_follow_up: false,
    change_job: false,
    change_of_equipment: false,
    annual: false,
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
    showPreview: false,
    apiData: {},
    instructions: [],
    eye_screenshot: '',
    map_screenshot_img: '',
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
      equipement: data.equipement,
      pre_post_trip: data.pre_post_trip,
      behind_the_wheel: data.behind_the_wheel,
      eye_movement: data.eye_movement,
      safe_work_practice: data.safe_work_practice,
      production: data.production,
      vehicle_road_test: data.vehicle_road_test,
      passenger_evacuation: data.passenger_evacuation,
      passenger_pre_trip: data.passenger_pre_trip,
      new_hire: data.new_hire,
      near_miss: data.near_miss,
      incident_follow_up: data.incident_follow_up,
      change_job: data.change_job,
      change_of_equipment: data.change_of_equipment,
      annual: data.annual,
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
        equipement: false,
        pre_post_trip: false,
        behind_the_wheel: false,
        eye_movement: false,
        safe_work_practice: false,
        production: false,
        vehicle_road_test: false,
        passenger_evacuation: false,
        passenger_pre_trip: false,
        new_hire: false,
        near_miss: false,
        incident_follow_up: false,
        change_job: false,
        change_of_equipment: false,
        annual: false,
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
    // console.log(`student tests res: `, res);
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
        alert(`No pending test found`);
        this.props.updateTabChangeErrorMessage('Please start a test');
        if (res.data.results && res.data.results[0])
          this.loadTest(res.data.results[0]);
        // this.createNewTest()
      }
    } else {
      alert('could not load test information');
    }
  };

  loadTest = async (pendingTest) => {
    // console.log('loading test', pendingTest);
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
          this.props.updateTabChangeErrorMessage(
            'Please save or discard your changes',
          );
      } else {
        if (this.props.tabChangeErrorMessage !== false)
          this.props.updateTabChangeErrorMessage(false);
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
      equipement: this.state.equipement,
      pre_post_trip: this.state.pre_post_trip,
      behind_the_wheel: this.state.behind_the_wheel,
      eye_movement: this.state.eye_movement,
      safe_work_practice: this.state.safe_work_practice,
      production: this.state.production,
      vehicle_road_test: this.state.vehicle_road_test,
      passenger_evacuation: this.state.passenger_evacuation,
      passenger_pre_trip: this.state.passenger_pre_trip,
      new_hire: this.state.new_hire,
      near_miss: this.state.near_miss,
      incident_follow_up: this.state.incident_follow_up,
      change_job: this.state.change_job,
      change_of_equipment: this.state.change_of_equipment,
      annual: this.state.annual,
      injury_date: this.state.injury_date,
      accident_date: this.state.accident_date,
      taw_start_date: this.state.taw_start_date,
      taw_end_date: this.state.taw_end_date,
      lost_time_start_date: this.state.lost_start_time,
      return_work_date: this.state.return_to_work_date,
      // "company": this.state.company.id
    };
    if (this.state.instructor && this.state.instructor.id)
      data['instructor'] = this.state.instructor.id;

    console.log('saveInfo data', data);
    let endpoint = '';
    if (this.props.eveluationFlowReducer.selected_test) {
      endpoint = `/api/v1/students/${this.state.student.id}/tests/${this.props.eveluationFlowReducer.selected_test?.id}/info/`;
    } else {
      //if no pending test
      return false;
    }

    let res = await apiPatch(endpoint, data, true);
    console.log(`patchTestInfo res: `, res);
    if (res && res.data) {
      // this.props.navigation.goBack()
      // errorMessage('Student Info Updated')
      // this.getInfo();
      await this.props.updateSelectedTestInfo(res.data);
    }
    return true;
  };
  // methods for preview
  previewInfo = async () => {
    await AsyncStorage.getItem('mapScreenshot').then(async (data) => {
      await this.setState({
        map_screenshot_img: 'data:image/png;base64,' + data,
      });
      await AsyncStorage.getItem('@storage_Key').then(async (jsonValue) => {
        console.log('retrieving: , ', jsonValue);
        const eyeData = jsonValue != null ? JSON.parse(jsonValue) : null;
        await this.setState({
          eye_screenshot: 'data:image/png;base64,' + eyeData?.uri,
        });
        await this.getNotesInfo();
        await this.getPreTripData();
        await this.getBTWData();
        await this.getSwpData();
        this.setState({showPreview: true});
        return
      });
    });
  };
  getNotesInfo = async () => {
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/notes/`,
    );
    // console.log(`getInfoUser res: `, res);
    if (res && res.data && res.data.results) {
      this.setState({studentNotes: res.data.results});
      // this.DataPapulate(res.data);
      // this.props.navigation.goBack()
      // errorMessage('Student Info Fetch')
    }
    return;
  };
  getPreTripData = async () => {
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/pretrips/${_class}/`,
    );
    let instructions = await apiGet(`/api/v1/instructions/pretrips/${_class}/`);

    if (res && res.data && instructions && instructions.data) {
      // console.log('data', res.data)
      let instructionsObjectified = {};
      instructions.data.forEach((_instruction) => {
        instructionsObjectified[_instruction.field_name] =
          _instruction.instruction;
      });
      console.log('pretrip instructionsObjectified', instructionsObjectified);
      await this.setState({
        ...res.data,
        apiData: res.data,
        instructions: instructions.data,
        mounting: false,
      });
    } else {
      await this.setState({mounting: false});
    }
    let totalPossiblePoints = 0;
    let totalPointsReceived = 0;
    let totalEffPercentage = 0;
    // let check = true;
    _.forEach(this.state, (level1, level1Key) => {
      // check = true
      _.forEach(level1, (level2, key) => {
        if (
          level1Key == 'sections' ||
          level1Key == 'created' ||
          level1Key == 'updated' ||
          level1Key == 'test' ||
          key == 'key' ||
          key == 'title' ||
          key == `pre_trip_${_class}` ||
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

    // console.log('totalPossiblePoints', totalPossiblePoints)
    // console.log('totalPointsReceived', totalPointsReceived)
    // console.log('totalEffPercentage', totalEffPercentage)

    this.setState({
      totalPossiblePoints,
      totalPointsReceived,
      totalEffPercentage,
    });
    return true;
  };
  getBTWData = async () => {
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
      await this.setState({
        ...res.data,
        apiData_btw: res.data,
        instructions_btw: instructions.data,
        mounting: false,
      });

      // if (res && res.data && res.data.map_data && res.data.map_image) {
      //   let parsedMapData = JSON.parse(res.data.map_data);
      //   console.log('parsedMapData', parsedMapData);
      //   this.props.setMapData({
      //     ...parsedMapData,
      //     map_screenshot_url: res.data.map_image,
      //   });
      // } else {
      //   this.props.setMapData(null);
      // }
    } else {
      this.setState({mounting: false});
    }

    res = await apiGet(
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

    await this.setState({charData_btw: chartData});

    return true;
  };

  getSwpData = async () => {
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/swp/`,
    );
    console.log('swp res', res);
    let instructions = await apiGet('/api/v1/instructions/swp/');

    if (res && res.data && instructions && instructions.data) {
      // console.log('data', res.data)
      let instructionsObjectified = {};
      instructions.data.forEach((_instruction) => {
        instructionsObjectified[_instruction.field_name] =
          _instruction.instruction;
      });
      console.log('instructionsObjectified', instructionsObjectified);
      this.setState({
        ...res.data,
        instructionsSwp: instructions.data,
        mounting: false,
      });
    } else {
      this.setState({mounting: false});
    }

    res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/swp/injury_probability_graph/`,
    );
    let chartData = [];
    if (res && res.data && res.data.chart_data) {
      _.forEach(res.data.chart_data, (entity) => {
        // `["${level1.title}", ${state[level1.key]['percent_effective'] ? Number(state[level1.key]['percent_effective']) : 5.00}]`
        chartData.push(`["${entity.title}", ${entity.new_value + ''}]`);
      });
    }
    console.log('chartData', chartData);
    await this.setState({charData_swp: chartData});

    return true;
  };

  getVrtData = async () => {
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
        instructionsVrt: instructions.data,
        mounting: false,
      });
    } else {
      this.setState({mounting: false});
    }
    return true;
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
      eye_screenshot,
      map_screenshot_img,
    } = this.state;
    const {
      company_info,
      student_info,
      instructor_info,
      selectedTestInfo,
      group_info,
      groupMode,
    } = this.props.eveluationFlowReducer;

    const {eveluationFlowReducer} = this.props;
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
                        html: INFO(
                          this.state.studentNotes,
                          this.state,
                          student_info,
                          company_info,
                          instructor_info,
                          INFO_ICON,
                          PreTripsDataModal,
                          selectedTestInfo,
                          this.state.chartData,
                          true,
                          BTWModal,
                          this.state.charData_btw,
                          eveluationFlowReducer.mapData,
                          eveluationFlowReducer.mapData?.map_screenshot_url,
                          SwpDataModals,
                          this.state.charData_swp,
                          VRTDataModals,
                          eye_screenshot,
                          map_screenshot_img,
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
                    html: INFO(
                      this.state.studentNotes,
                      this.state,
                      student_info,
                      company_info,
                      instructor_info,
                      INFO_ICON,
                      PreTripsDataModal,
                      selectedTestInfo,
                      this.state.chartData,
                      true,
                      BTWModal,
                      this.state.charData_btw,
                      eveluationFlowReducer.mapData,
                      eveluationFlowReducer.mapData?.map_screenshot_url,
                      SwpDataModals,
                      this.state.charData_swp,
                      VRTDataModals,
                      eye_screenshot,
                      map_screenshot_img,
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
                  `Notification \n \n Driver License Expiration Date can't be changed. it can be updated by editing the student info!`,
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
                  `Notification \n \n Driver license number can't be changed. it can be updated by editing the student info!`,
                );
              }}
              component={<Text>{driver_license_num}</Text>}
            />

            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={`History Reviewed`}
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
              title={`Endorsements`}
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
              title={`Corrective lens required`}
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

            <View style={{backgroundColor: colors.APP_LIGHT_BLUE_COLOR}}>
              <Text
                style={{
                  marginHorizontal: 10,
                  marginVertical: 5,
                  fontSize: 14,
                }}>{`Select the type of training completed`}</Text>
            </View>

            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={`Equipment`}
              onChange={(equipement) => this.setState({equipement})}
              value={this.state.equipement}
            />
            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={`Eye Movement`}
              onChange={(eye_movement) => this.setState({eye_movement})}
              value={this.state.eye_movement}
            />
            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={`Production`}
              onChange={(production) => this.setState({production})}
              value={this.state.production}
            />
            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={`Pre/Trip - Post/Trip`}
              onChange={(pre_post_trip) => this.setState({pre_post_trip})}
              value={this.state.pre_post_trip}
            />
            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={`Behind the Wheel`}
              onChange={(behind_the_wheel) => this.setState({behind_the_wheel})}
              value={this.state.behind_the_wheel}
            />
            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={`Safe Work Practice`}
              onChange={(safe_work_practice) =>
                this.setState({safe_work_practice})
              }
              value={this.state.safe_work_practice}
            />
            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={`Vehicle Road Test`}
              onChange={(vehicle_road_test) =>
                this.setState({vehicle_road_test})
              }
              value={this.state.vehicle_road_test}
            />
            {/* <EvaluationYesNoOptionField
            start_time={this.state.start_time}
            end_time={this.state.end_time}
              title={`Passenger Evaluation`}
              onChange={(passenger_evacuation) => this.setState({ passenger_evacuation })}
              value={this.state.passenger_evacuation}
            />
            <EvaluationYesNoOptionField
            start_time={this.state.start_time}
            end_time={this.state.end_time}
              title={`Pessenger Pre/Trip`}
              onChange={(passenger_pre_trip) => this.setState({ passenger_pre_trip })}
              value={this.state.passenger_pre_trip}
            /> */}

            <View style={{backgroundColor: colors.APP_LIGHT_BLUE_COLOR}}>
              <Text
                style={{
                  marginHorizontal: 10,
                  marginVertical: 5,
                  fontSize: 14,
                }}>{`Select the reason for training and enter dates if applicable`}</Text>
            </View>

            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={`New Hire`}
              onChange={(new_hire) => this.setState({new_hire})}
              value={this.state.new_hire}
            />
            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={`Near Miss`}
              onChange={(near_miss) => this.setState({near_miss})}
              value={this.state.near_miss}
            />
            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={`Incident Follow-up`}
              onChange={(incident_follow_up) =>
                this.setState({incident_follow_up})
              }
              value={this.state.incident_follow_up}
            />
            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={`Change Job`}
              onChange={(change_job) => this.setState({change_job})}
              value={this.state.change_job}
            />
            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={`Change of Equipment`}
              onChange={(change_of_equipment) =>
                this.setState({change_of_equipment})
              }
              value={this.state.change_of_equipment}
            />
            <EvaluationYesNoOptionField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={`Annual`}
              onChange={(annual) => this.setState({annual})}
              value={this.state.annual}
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              rightArrow
              title={'Injury Date'}
              backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
              onPress={() => {
                showPopup(
                  <DateTimePicker
                    onConfirm={(injury_date) => {
                      this.setState({injury_date});
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
                  <Text>{this.state.injury_date}</Text>
                </View>
              }
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              rightArrow
              title={'Accident Date'}
              backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
              onPress={() => {
                showPopup(
                  <DateTimePicker
                    onConfirm={(accident_date) => {
                      this.setState({accident_date});
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
                  <Text>{this.state.accident_date}</Text>
                </View>
              }
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              rightArrow
              title={'TAW Start Date'}
              backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
              onPress={() => {
                showPopup(
                  <DateTimePicker
                    onConfirm={(taw_start_date) => {
                      this.setState({taw_start_date});
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
                  <Text>{this.state.taw_start_date}</Text>
                </View>
              }
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              rightArrow
              title={'TAW End Date'}
              backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
              onPress={() => {
                showPopup(
                  <DateTimePicker
                    onConfirm={(taw_end_date) => {
                      this.setState({taw_end_date});
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
                  <Text>{this.state.taw_end_date}</Text>
                </View>
              }
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              rightArrow
              title={'Lost Time Start Date'}
              backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
              onPress={() => {
                showPopup(
                  <DateTimePicker
                    onConfirm={(lost_start_time) => {
                      this.setState({lost_start_time});
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
                  <Text>{this.state.lost_start_time}</Text>
                </View>
              }
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              rightArrow
              title={'Return to Work Date'}
              backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
              onPress={() => {
                showPopup(
                  <DateTimePicker
                    onConfirm={(return_to_work_date) => {
                      this.setState({return_to_work_date});
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
                  <Text>{this.state.return_to_work_date}</Text>
                </View>
              }
            />

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
                  `secore reflect what the instructor needed to insure the drivers demonstration and understanding of each element \n \n 5 = No correction with no reinforcement \n \n 4 = Reinforcement understanding \n \n 3 = Corrected and reinforced understanding \n \n 2 = Multiple corrections needed until demonstrated correctly, reinforced understanding \n \n 1 = unacceptale and cretical error, driver failed to demonstrate element correctly or failed to convey understanding \n \n NA = Element was not applicable`,
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

const mapStateToProps = state => {
  return {
    userReducer: state.userReducer,
    eveluationFlowReducer: state.eveluationFlowReducer,
    tabChangeErrorMessage: state.eveluationFlowReducer.tabChangeErrorMessage,
    // student_info: state.eveluationFlowReducer.student_info,
  };
};

export default connect(mapStateToProps, { fetchUserProfileAction, updateCompanyInfo, updateStudentInfo, updateInstructorInfo, updateGroupInfo, updateGroupModeInfo, updateSelectedTest, updateSelectedTestInfo, updateTabChangeErrorMessage }, null, { forwardRef: true })(InfoTab);
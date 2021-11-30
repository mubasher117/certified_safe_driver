import React from 'react';
import { View, TouchableOpacity, Image, ScrollView, Modal, Alert } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
import { connect } from 'react-redux';
import { Text, Loader, ScreenWrapper, EvaluationField, Evaluation7OptionField, DateTimePicker, Header, SignaturePicker, Footer, Selector } from '../../components';
import { fetchUserProfileAction, hideSelector, showPopup, showSelector, updateTabChangeErrorMessage } from '../../actions';
import { CALENDAR_ICON, PLAY_ICON, PAUSE_ICON, EXPORT_ICON, INFO_BLUE_ICON, CLOSE_ICON, PLATFORM_IOS, } from '../../constants';
import { PreTripsDataModalA } from '../../utils/PreTripsDataModalA';
import { PreTripsDataModalB } from '../../utils/PreTripsDataModalB';
import { PreTripsDataModalC } from '../../utils/PreTripsDataModalC';
import { PreTripsDataModalD } from '../../utils/PreTripsDataModalD';
import { PreTripsDataModalBUS } from '../../utils/PreTripsDataModalBUS';
import _, { sample, isNumber } from 'lodash';
import * as colors from '../../styles/colors';
import { counterToAlpha, getDataDiff } from '../../utils/function';
import { apiGet, apiPut, apiPatch } from '../../utils/http';
import { WebView } from 'react-native-webview';
import { scale } from '../../utils/scale';
import PRETRIP from './preview/PRETripPreviewHTML'
import ActionSheet from 'react-native-actionsheet'
import RNHTMLtoPDF from 'react-native-html-to-pdf';
import Share from 'react-native-share';
import moment from 'moment';

let _class = 'class_a';
let PreTripsDataModal = PreTripsDataModalA;
let sectionPosition = {};

class PreTripTab extends React.Component {

  state = {
    sections: [],
    // ...PreTripsDataModal,
    mounting: true,
    signature: null,
    showPreview: false,
    isClassSelected: false,
    start_time: false,
    totalPointsReceived: 0,
    totalPossiblePoints: 0,
    totalEffPercentage: 0,
    apiData: {},
    instructions: []
  }

  async componentDidMount() {
    setTimeout(() => {
      this._classActionSheet.show()
    }, 500);
  }

  scrolSectionHandler = (num) => {
    console.log('this.myScroll: ', num, sectionPosition[num.key], this.myScroll);
    this.myScroll.scrollToPosition(0, sectionPosition[num.key]);
  };

  populateForm = (clear) => {
    // set base state 
    // level 2 nested states
    let state = {}
    state.sections = []
    _.forEach(PreTripsDataModal, (level1Val, level1Key) => {
      let level2State = null;
      if (level1Val && level1Val.value === null && level1Val.value !== undefined) {
        //fields with no nesteds
        //  console.log('nulls keys', level1Val.value);
      } else {
        state.sections.push({ id: level1Key, name: level1Val.title, key: level1Key })
        level2State = {}
        // console.log('undefined keys', level1Val);
        _.forEach(level1Val, (val, level2Key) => {
          if (level2Key != 'key' && level2Key != 'title')
            level2State[level2Key] = val?.value
        })
      }
      state[level1Key] = level2State
    })
    console.log('base state', state);
    // this.setState({ ...state, mounting:false })
    this.setState({ ...state }, () => {
      if (!clear)
        this.getData()
    })
  }

  // componentDidUpdate(prevProps, prevState) {
  //   if (prevProps.shown != this.props.shown) {
  //     setTimeout(() => {
  //       this._classActionSheet.show()
  //     }, 500);
  //   }
  // }

  componentDidUpdate(prevProps, prevState) {
    if (this.props.shown && prevProps.tabChangeErrorMessage == this.props.tabChangeErrorMessage) {
      const isDiff = getDataDiff({ ...this.state.apiData }, this.state)
      console.log('isDiff', isDiff)
      if (isDiff) {
        if (this.props.tabChangeErrorMessage == false)
          this.props.updateTabChangeErrorMessage('Please save or discard your changes')
      } else {
        if (this.props.tabChangeErrorMessage !== false)
          this.props.updateTabChangeErrorMessage(false)
      }
    }
  }

  getData = async () => {
    const { company_info, student_info, selected_test } = this.props.eveluationFlowReducer
    let res = await apiGet(`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/pretrips/${_class}/`)
    let instructions = await apiGet(`/api/v1/instructions/pretrips/${_class}/`);

    if (res && res.data && instructions && instructions.data) {
      console.log('data', res.data)
      let instructionsObjectified = {}
      instructions.data.forEach(_instruction => {
        instructionsObjectified[_instruction.field_name] = _instruction.instruction
      });
      console.log('pretrip instructionsObjectified', instructionsObjectified)
      this.setState({ ...res.data, apiData: res.data, instructions: instructions.data, mounting: false })
    } else {
      this.setState({ mounting: false })
    }
    return true;
  }

  savePreTrip = async () => {
    let newState = {}
    const isDiff = getDataDiff({ ...this.state.apiData }, this.state)
    if (!isDiff) {
      return
    }
    //only update what is changed
    isDiff.forEach(key => {
      // if (key == "start_time") {
      //   console.log('start_time: ', moment(this.state[key]).format('hh:mm:ss'), 'Date without format: ', this.state[key]);
      //   newState[key] = moment(this.state[key]).format('hh:mm:ss') // Error: "Time has wrong format. Use one of these formats instead: hh:mm[:ss[.uuuuuu]]."
      //   // newState[key] = this.state[key]
      // } else {
      //   console.log('start_time: else ', this.state[key]);
      //   newState[key] = this.state[key]
      // }
      newState[key] = this.state[key]
    })

    _.forEach(newState, (level1Val, _state) => {
      if (_state.includes('signature')) {
        if (newState[_state] == null) {
          delete newState[_state]
        }
      }
      _.forEach(level1Val, (value, level2Key) => {
        if (level2Key == `pre_trip_${_class}` || level2Key == 'created' || level2Key == 'updated' || level2Key == 'percent_effective' || level2Key == 'points_received' || level2Key == 'possible_points') {
          delete newState[_state][level2Key]
        }
      })
    })

    console.log('newState', newState)
    const { company_info, student_info, selected_test } = this.props.eveluationFlowReducer
    let res = await apiPatch(`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/pretrips/${_class}/`, newState, true)
    console.log(`pretrip patch res: `, res)
    if (res && res.data) {
      //HACK: invalid data returned from patch, always returns initial data
      // this.setState({...res.data, apiData: res.data,})
      this.getData();
    }
    return true;
  }

  previewPreTrip = async () => {

    // this.setState({ showPreview: true })

    const { company_info, student_info, selected_test } = this.props.eveluationFlowReducer
    let res = await apiGet(`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/pretrips/${_class}/accident_probability_graph/`)
    console.log('chartData res', res);
    let chartData = []
    if (res && res.data && res.data.chart_data) {
      _.forEach(res.data.chart_data, (entity => {
        // `["${level1.title}", ${state[level1.key]['percent_effective'] ? Number(state[level1.key]['percent_effective']) : 5.00}]`
        chartData.push(`["${entity.title}", ${entity.new_value + ''}]`)
      }))
    }
    console.log('chartData', chartData);
    await this.getData();
    await this.setState({ chartData })
    this.setState({ showPreview: true })
  }

  calculatePoints = () => {
    console.log('this.state', this.state);
    let totalPossiblePoints = 0;
    let totalPointsReceived = 0;
    let totalEffPercentage = 0;
    // let check = true;
    _.forEach(this.state, (level1, level1Key) => {
      // check = true
      _.forEach(level1, (level2, key) => {
        if (level1Key == 'sections' || level1Key == 'created' || level1Key == 'updated' || level1Key == 'test'
          || key == 'key' || key == 'title' || key == `pre_trip_${_class}` || key == "possible_points" || key == "points_received" || key == "percent_effective" || key == 'created' || key == 'id' || key == 'updated' || key == 'notes') {
          //ignore these for calculation
        } else {
          if (level2 && isNumber(level2)) {
            // console.log('level2', level2, ' key', key, ' for lvl1', level1Key)
            totalPointsReceived += level2
            totalPossiblePoints += 5
            // if (check) {
            //   totalPossiblePoints += level1['possible_points']
            //   check = false
            // }
          }
        }
      })
    })

    totalEffPercentage = totalPointsReceived / totalPossiblePoints * 100
    totalEffPercentage = totalEffPercentage.toFixed(2);

    // console.log('totalPossiblePoints', totalPossiblePoints)
    // console.log('totalPointsReceived', totalPointsReceived)
    // console.log('totalEffPercentage', totalEffPercentage)

    this.setState({ totalPossiblePoints, totalPointsReceived, totalEffPercentage })
  }

  loadNotificationAlert = (level1) => {
    // console.log('level1: naveed: ', level1)
    let level2Counter = 0;
    let instructionsToShow = ''
    _.forEach(level1, (level2, key) => {
      if (key == 'key' || key == 'notes' || key == 'title' || level2.key == "possible_points" || level2.key == "points_received" || level2.key == "percent_effective") {
        // return null;
      } else {
        ++level2Counter;
        // console.log('key', key)
        if (this.state.instructions[key])
          instructionsToShow += `${counterToAlpha(level2Counter)}. ${this.state.instructions[key]}\n\n`
      }
    })
    // console.log('this.state.notifications', this.state.instructions)
    // console.log('instructionsToShow', instructionsToShow)
    if (instructionsToShow) {
      Alert.alert(
        'Notification',
        instructionsToShow
        ,
        [
          {
            text: 'ok',
            onPress: () => console.log('ok Pressed'),
            style: 'cancel',
          }
        ],
        { cancelable: false },
      )
    }
  }

  render() {
    if (this.state.mounting && this.state.isClassSelected == false) {
      return (
        <ScreenWrapper contentContainerStyle={{ justifyContent: 'center', alignItems: 'center' }}>
          <Text>
            Please select test class
          </Text>
          <ActionSheet
            ref={o => this._classActionSheet = o}
            title={'Select class'}
            options={['A', 'B', 'C', 'P']}
            // cancelButtonIndex={10}
            // destructiveButtonIndex={10}
            onPress={(index) => {
              console.log('Pretrip class actionsheet index', index);
              switch (index) {
                case 0:
                  _class = 'class_a'
                  PreTripsDataModal = PreTripsDataModalA
                  break;
                case 1:
                  _class = 'class_b'
                  PreTripsDataModal = PreTripsDataModalB
                  break;
                case 2:
                  _class = 'class_c'
                  PreTripsDataModal = PreTripsDataModalC
                  break;
                case 3:
                  _class = 'class_p'
                  PreTripsDataModal = PreTripsDataModalBUS
                  break;

                default:
                  _class = 'a'
                  PreTripsDataModal = PreTripsDataModalA
                  break;
              }
              this.setState({ isClassSelected: true }, () => {
                this.populateForm()
              })
            }}
          />
        </ScreenWrapper>
      )
    }
    if (this.state.mounting && this.state.isClassSelected) {
      return (
        <ScreenWrapper contentContainerStyle={{ justifyContent: 'center', alignItems: 'center' }}>
          <Loader />
        </ScreenWrapper>
      )
    }
    let level1Counter = 0;
    let level2Counter = 0;
    const show = { flex: 1, height: undefined }
    const hide = { flex: 0, height: 0 }
    const { eveluationFlowReducer } = this.props;
    const { totalPointsReceived, totalPossiblePoints } = this.state
    const { company_info, student_info, selected_test, selectedTestInfo, instructor_info } = eveluationFlowReducer
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
              onRequestClose={() => { }}>
              <View style={{ flex: 1 }}>
                <Header>
                  <TouchableOpacity onPress={() => this.setState({ showPreview: false })}>
                    <Text style={{ marginLeft: 20, fontSize: 16 }}>{'Close'}</Text>
                  </TouchableOpacity>

                  <Text style={{ marginRight: scale(23) }}>Preview</Text>
                  {/* <Text>Email</Text> */}

                  <TouchableOpacity onPress={async () => {
                    let options = {
                      html: PRETRIP(PreTripsDataModal, this.state, student_info, company_info, selectedTestInfo, instructor_info, this.state.chartData, true),
                      fileName: `student_${student_info?.id}_PRETRIP_${_class}`,
                      // directory: 'Documents',
                    };

                    let file = await RNHTMLtoPDF.convert(options)
                    console.log('RNHTMLtoPDF file', file);
                    console.log('RNHTMLtoPDF file path', `${PLATFORM_IOS ? '' : 'file://'}${file.filePath}`);
                    await Share.open({
                      url: `${PLATFORM_IOS ? '' : 'file://'}${file.filePath}`,
                      title: 'Share PDF'
                    })
                  }}>
                    {/* <Text style={{ marginRight: 20, fontSize: 16 }}>Share</Text> */}
                    <Image source={EXPORT_ICON} style={{ resizeMode: 'contain', height: 20, width: 20, paddingRight: 10 }} />
                  </TouchableOpacity>

                </Header>

                <WebView
                  source={{ html: PRETRIP(PreTripsDataModal, this.state, student_info, company_info, selectedTestInfo, instructor_info, this.state.chartData) }}
                  // source={require('./preview/preTrip.html')}
                  ref={ref => { this.WebView = ref; }}
                  javaScriptEnabled={true}
                  domStorageEnabled={true}
                  startInLoadingState={true}
                />
              </View>
            </Modal>

            {_.map(PreTripsDataModal, (level1) => {
              // console.log('level1 in render', level1)
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
                      onPress={() => showSelector(
                        <SignaturePicker handleSignature={(signature) => {
                          console.log('signature', signature)
                          this.setState({ [level1.key]: signature }); hideSelector()
                        }} />
                      )}
                      component={
                        <View
                          style={{ flex: 1 }}>
                          <Image source={this.state[level1.key] && { uri: this.state[level1.key] }} style={{ width: 100, height: 38, resizeMode: 'cover' }} />
                        </View>
                      }
                    />
                  )
                } else if (level1.title.includes('Date') || level1.title.includes('date')) {
                  // to find date, look for ate as D can be capital
                  return (
                    <EvaluationField
                      start_time={this.state.start_time}
                      end_time={this.state.end_time}
                      key={`${level1Counter}. ${level1.title}`}
                      // required
                      rightArrow
                      title={`${level1Counter}. ${level1.title}`}
                      onPress={() => {
                        showPopup(
                          <DateTimePicker
                            onConfirm={(date) => {
                              this.setState({ [level1.key]: date })
                            }}
                          />
                        )
                      }}
                      component={
                        <View style={{ flexDirection: 'row', alignItems: 'center' }}>
                          <Image source={CALENDAR_ICON} style={{ height: scale(34), width: scale(34) }} />
                          <Text>{this.state[level1.key]}</Text>
                        </View>
                      }
                    />
                  )
                } else {
                  return (
                    <EvaluationField
                      start_time={this.state.start_time}
                      end_time={this.state.end_time}
                      key={`${level1.key}`}
                      title={`${level1Counter}. ${level1.title}`}
                      value={this.state[level1.key]}
                      onChangeText={value => this.setState({ [level1.key]: value })}
                    />
                  )
                }
              } else {
                return (<View
                  onLayout={(event) =>
                    sectionPosition = {
                      ...sectionPosition, [level1.key]: Math.round(event.nativeEvent.layout.y)
                    }}>

                  <View style={{ backgroundColor: colors.APP_LIGHT_BLUE_COLOR, flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', paddingHorizontal: 10 }}>
                    <Text style={{ marginVertical: 5, }}>{`${level1Counter}. ${level1.title}`}</Text>
                    <TouchableOpacity onPress={() => this.loadNotificationAlert(level1)}>
                      <Image source={INFO_BLUE_ICON} style={{ height: 20, width: 20, resizeMode: 'contain' }} />
                    </TouchableOpacity>
                  </View>

                  {_.map(level1, (level2, key) => {
                    // console.log('level2', level2, ' KEY', key)
                    if (key == 'key' || key == 'title' || level2.key == "possible_points" || level2.key == "points_received" || level2.key == "percent_effective") {
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
                          onChangeText={newValue => this.setState({ [level1.key]: { ...this.state[level1.key], [level2.key]: newValue } })}
                          value={this.state[level1.key][level2.key]}
                        />
                      )
                    }
                    ++level2Counter
                    // console.log('counterToAlpha(level2Counter)', counterToAlpha(level2Counter));
                    return (
                      <Evaluation7OptionField
                        start_time={this.state.start_time}
                        end_time={this.state.end_time}
                        key={`${level1.key}+${level2.key}`}
                        title={`${counterToAlpha(level2Counter) == undefined ? '' : counterToAlpha(level2Counter)}. ${level2.title}`}
                        onChange={(newValue) => this.setState({ [level1.key]: { ...this.state[level1.key], [level2.key]: newValue } }, this.calculatePoints)}
                        value={this.state[level1.key][level2.key]}
                      />
                    )
                  })}
                </View>)
              }
            })}
          </KeyboardAwareScrollView>
        </ScreenWrapper>
        {this.props.shown && <Footer>

          <TouchableOpacity onPress={() => {
            showSelector(<Selector
              title={'Section'}
              data={this.state.sections}
              onSelect={this.scrolSectionHandler}
            // onSelect={(item) => this.setState({ instructor: item.name })}
            />)
          }}>
            <Text>Section</Text>
          </TouchableOpacity>

          {!this.state.end_time && <TouchableOpacity
            onPress={() => {
              console.log('this.state', this.state)
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
                        this.setState({ end_time: moment().format('HH:mm') }, async () => {
                          await this.savePreTrip();
                        })
                      }
                    },
                  ],
                  { cancelable: false },
                )
              } else {
                this.setState({ start_time: moment().format('HH:mm'), date: moment().format('YYYY-MM-DD') }) // MM/DD/YYYY HH:mm:ss
              }

            }}
          >
            <Image source={this.state.start_time ? PAUSE_ICON : PLAY_ICON} style={{ resizeMode: 'contain', height: 25, width: 25 }} />
          </TouchableOpacity>}
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

          <TouchableOpacity onPress={() => {
            Alert.alert("Info", `${totalPointsReceived} points received from ${totalPossiblePoints} points possible`);
          }}>
            <Text>{totalPointsReceived}/{totalPossiblePoints}</Text>
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
        </Footer>}
      </>
    )
  }
}

const mapStateToProps = state => {
  return {
    userReducer: state.userReducer,
    eveluationFlowReducer: state.eveluationFlowReducer,
    tabChangeErrorMessage: state.eveluationFlowReducer.tabChangeErrorMessage,
  };
};

export default connect(mapStateToProps, { fetchUserProfileAction, updateTabChangeErrorMessage }, null, { forwardRef: true })(PreTripTab);
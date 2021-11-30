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
import {defenseQuiz} from '../questions/defenseQuiz';
import { WebView } from 'react-native-webview';
import RNHTMLtoPDF from 'react-native-html-to-pdf';
import Share from 'react-native-share';
import DefensiveQuizPreview from './preview/DefensiveQuizPreview';
class DefenseQuizTab extends React.Component {
  state = {
    start_time: '12:30 AM',
    date: '',
    name: '',
    history: '',
    checkBoxState: {},
    mounting: true,
    _defenseQuizes: defenseQuiz,

    signature: null,
    correct: null,
    possible: null,
    effective: null,
    review: null,
    showPreview: false,
  };

  preview = async () => {
    this.setState({showPreview: true});
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
      name: `${student_info?.first_name}  ${student_info?.last_name}`,
      date: selected_test?.created
        ? selected_test.created.split('T')[0]
        : 'N/A',
      // trainerName: instructor_info?.full_name,
    });
    this.getQuizQuestions();
  }

  handleGenderCheckBox = (event) => {
    console.log('event: ', event);
    let quizes = this.state._defenseQuizes;
    quizes.forEach((question) => {
      // if (data.type == 'checkbox') {

      // console.log('question: ', question);
      if (question.correct_choices?.length > 0) {
        question.choices.forEach((data) => {
          if (data.title === event.title && data.question === event.question) {
            data.isChecked = true;
            if (question.question_type === 'single') {
              if (
                event.question === question.correct_choices[0].question &&
                event.title === question.correct_choices[0].title
              ) {
                question.isTrue = true;
              } else {
                question.isTrue = false;
              }
            } else {
              let isMarkedCorrect = false;
              if (question.remainingCorrectChoices) {
                question.remainingCorrectChoices--;
              }
              question.correct_choices.map((correct_choice, index) => {
                if (event.title === correct_choice.title) {
                  isMarkedCorrect = true;
                }
              });
              if (isMarkedCorrect) {
                data.isTrue = true;
              } else {
                data.isTrue = false;
              }
            }
          } else {
            // data.isChecked = false;
          }
        });
      } else if (question.id === event.question) {
        alert('No correct answer. Please add from the admin panel.');
      }
      // }
    });
    this.setState({_defenseQuizes: quizes});
  };

  saveDefenseQuiz = async () => {
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
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/defense-quiz/`,
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
  getQuizQuestions = async () => {
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
  getQuizStats = async () => {
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiGet(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/quizes/defensive_driving/get-answers/`,
    );
    if (res && res.data) {
      // console.log()
      console.log(res.data);
      this.setState({
        correct: res.data.total_correct_answers?.toString(),
        possible: res.data.total_questions?.toString(),
        effective: res.data.percentage?.toString(),
        review: 'Yes',
      });
    }
    return true;
  };
  submitQuiz = async () => {
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let quizData = [];
    this.state._defenseQuizes.map((question, index) => {
      let quizAnswer = {
        question: question.id,
        answers: [],
      };
      question.choices.map((choice, idx) => {
        if (choice.isChecked === true) {
          quizAnswer.answers.push(choice.id);
        }
      });
      quizData.push(quizAnswer);
    });
    console.log('*************** QUIZ DATA ***************');
    console.log(quizData);
    let res = await apiPost(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/quizes/defensive_driving/submit-answers/`,
      quizData,
    );
    if (res && res.data) {
      console.log(res.data);
    }
    return true;
  };
  render() {
    const {
      start_time,
      date,
      name,
      history,
      _defenseQuizes,
      signature,
      correct,
      possible,
      effective,
      review,
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
    console.log("******** STUDENT DATA *************");
    console.log(student_info);

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
          <Modal
            animationType="slide"
            visible={this.state.showPreview}
            onRequestClose={() => {}}>
            <View style={{flex: 1}}>
              <Header>
                <TouchableOpacity
                  onPress={() => this.setState({showPreview: false})}>
                  <Text style={{marginLeft: 20, fontSize: 16}}>{'Close'}</Text>
                </TouchableOpacity>

                <Text style={{marginRight: scale(23)}}>Preview</Text>
                {/* <Text>Email</Text> */}

                <TouchableOpacity
                  onPress={async () => {
                    let options = {
                      html: DefensiveQuizPreview(
                        this.state,

                        student_info,
                        company_info,
                        instructor_info,
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
                  html: DefensiveQuizPreview(this.state, 
                    student_info,
                    company_info,
                    instructor_info,),
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
          <ScrollView style={{flex: 1}}>
            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Name'}
              onChangeText={(name) => this.setState({name})}
              value={name}
            />
            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Date'}
              onChangeText={(date) => this.setState({date})}
              value={date}
            />
            {_.map(_defenseQuizes, (level1, idxOuter) => {
              // console.log('level1 :', level1);
              ++level1Counter;
              if (level1.choices) {
                // console.log('_(_(_(_(_(_(_ QUESTION  _)_)_)_)_)_)_)', idxOuter);
                // console.log(level1);
                return (
                  <View>
                    <View
                      style={{backgroundColor: colors.APP_LIGHT_GRAY_COLOR}}>
                      <Text
                        style={{
                          marginVertical: 5,
                          fontWeight: '600',
                          paddingHorizontal: scale(14),
                        }}>{`${level1Counter}) ${level1.title}`}</Text>
                    </View>
                    {level1.remainingCorrectChoices ? (
                      <Text
                        style={{
                          margingTop: 10,
                          marginLeft: 20,
                          color: 'red',
                        }}>
                        {level1.remainingCorrectChoices} choices remaining
                      </Text>
                    ) : <View/>}
                    <View style={{paddingHorizontal: 16, paddingBottom: 10}}>
                      {_.map(level1.choices, (data, index) => {
                        if (level1.question_type === 'single') {
                          let optionColor = null;
                          if (
                            level1.isTrue === true &&
                            data.isChecked === true
                          ) {
                            optionColor = 'green';
                          }
                          if (
                            level1.isTrue === false &&
                            data.isChecked === true
                          ) {
                            optionColor = 'red';
                          }
                          // if (
                          //   level1.isTrue === false &&
                          //   level1.correct_choices[0].title === data.title
                          // ) {
                          //   optionColor = 'green';
                          // }
                          return (
                            <CheckBoxGroup
                              style={{marginTop: 10}}
                              selected={data.isChecked}
                              // onPress={() => console.log('CheckBoxxxx',this.state.checkBoxState[`${item.id_fmm_registration_fields}-values`][data.field_value_id])}
                              onPress={() => {
                                if (level1.isTrue === null) {
                                  this.handleGenderCheckBox(data);
                                }
                              }}
                              text={data.title}
                              textStyle={{marginLeft: 5, color: optionColor}}
                              tintColor={optionColor}
                            />
                          );
                        } else {
                          let optionColor = null;
                          if (data.isTrue === true && data.isChecked === true) {
                            optionColor = 'green';
                          } else if (
                            data.isTrue === false &&
                            data.isChecked === true
                          ) {
                            optionColor = 'red';
                          }
                          return (
                            <CheckBoxGroup
                              style={{marginTop: 10}}
                              selected={data.isChecked}
                              // onPress={() => console.log('CheckBoxxxx',this.state.checkBoxState[`${item.id_fmm_registration_fields}-values`][data.field_value_id])}
                              onPress={() => this.handleGenderCheckBox(data)}
                              text={data.title}
                              textStyle={{marginLeft: 5, color: optionColor}}
                              tintColor={optionColor}
                            />
                          );
                        }
                      })}
                    </View>
                  </View>
                );
              }
              // else if (level1.type == 'boolean') {
              //   return (
              //     <EvaluationTrueFalseOptionField
              //       start_time={this.state.start_time}
              //       end_time={this.state.end_time}
              //       title={`${level1Counter}) ${level1.question}`}
              //       onChange={(value) => this.setState({[level1.key]: value})}
              //       value={this.state[level1.key]}
              //     />
              //   );
              // }
            })}

            {/* components start */}

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'# Correct'}
              onChangeText={(correct) => this.setState({correct})}
              value={correct}
              disabled={true}
            />
            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Possible'}
              onChangeText={(possible) => this.setState({possible})}
              value={possible}
              disabled={true}
            />
            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'% Effective'}
              onChangeText={(effective) => this.setState({effective})}
              value={effective}
              disabled={true}
            />
            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              title={'Review to 100%'}
              onChangeText={(review) => this.setState({review})}
              value={review}
              disabled={true}
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
          </ScrollView>
        </ScreenWrapper>
        {this.props.shown && (
          <Footer>
            {/* <TouchableOpacity
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

            <TouchableOpacity
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
            </TouchableOpacity>
            <View /> */}
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
})(DefenseQuizTab);

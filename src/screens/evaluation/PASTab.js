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
  Selector,
  SignaturePicker,
  Footer,
} from '../../components';
import SplashScreen from 'react-native-splash-screen';
import {
  fetchUserProfileAction,
  hideSelector,
  showPopup,
  showSelector,
} from '../../actions';
import {
  PLATFORM_IOS,
  CALENDAR_ICON,
  PLAY_ICON,
  PAUSE_ICON,
  EXPORT_ICON,
  PLUS_ICON,
  CLOSE_ICON,
} from '../../constants';
import {PasDataModals} from '../../utils/PasDataModals';
import _ from 'lodash';
import * as colors from '../../styles/colors';
import {counterToAlpha} from '../../utils/function';
import {apiPatch, apiGet} from '../../utils/http';
import {WebView} from 'react-native-webview';
import {scale} from '../../utils/scale';
import PAS from './preview/PASPreviewHTML';
import moment from 'moment';

class PASTab extends React.Component {
  state = {
    sections: [],
    // ...PasDataModals,
    signature: null,
    mounting: true,
    showPreview: false,
    start_time: false,
  };
  async componentDidMount() {
    this.populateForm();
  }

  populateForm = (clear) => {
    let state = {};
    _.forEach(PasDataModals, (level1Val, level1Key) => {
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
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/prod/`,
    );
    if (res && res.data) {
      console.log('data', res.data);
      this.setState({...res.data, mounting: false});
    } else {
      this.setState({mounting: false});
    }
    return true;
  };

  savePAS = async () => {
    //TODO: how to upload signature
    let newState = this.state;
    _.forEach(newState, (value, _state) => {
      if (_state.includes('signature')) delete newState[_state];
    });
    _.forEach(newState, (level1Val, _state) => {
      _.forEach(level1Val, (value, level2Key) => {
        if (level2Key == 'pas') delete newState[_state][level2Key];
      });
    });

    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    let res = await apiPatch(
      `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/pas/`,
      newState,
      true,
    );
    console.log(`pas patch res: `, res);
    if (res && res.data) {
      // this.props.navigation.goBack()
      // errorMessage('Student Info Updated')
      // this.getData();
    }
    return true;
  };

  previewPAS = async () => {
    await this.savePAS();
    await this.getData();
    this.setState({showPreview: true});
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
                  <Text>Email</Text>
                </Header>

                <WebView
                  source={{
                    html: PAS(
                      PasDataModals,
                      this.state,
                      eveluationFlowReducer.student_info,
                      eveluationFlowReducer.company_info,
                      eveluationFlowReducer.selectedTestInfo,
                      false,
                    ),
                  }}
                  // source={require('./preview/pas.html')}
                  ref={(ref) => {
                    this.WebView = ref;
                  }}
                  javaScriptEnabled={true}
                  domStorageEnabled={true}
                  startInLoadingState={true}
                />
              </View>
            </Modal>

            {_.map(PasDataModals, (level1) => {
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
                });
                return (
                  <View>
                    <View
                      style={{backgroundColor: colors.APP_LIGHT_BLUE_COLOR}}>
                      <Text
                        style={{
                          marginHorizontal: 10,
                          marginVertical: 5,
                        }}>{`${level1Counter}. ${level1.title}`}</Text>
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
                      // console.log('counterToAlpha(level2Counter)', counterToAlpha(level2Counter));
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
            <TouchableOpacity>
              <Text>Turns</Text>
            </TouchableOpacity>

            <TouchableOpacity
              onPress={() => {
                showSelector(
                  <Selector
                    title={'Section'}
                    data={this.state.sections}
                    onSelect={(item) => this.setState({instructor: item.name})}
                  />,
                );
              }}>
              <Text>Section</Text>
            </TouchableOpacity>

            <TouchableOpacity
              onPress={() => {
                console.log('this.state', this.state);
                this.setState({
                  start_time: moment().format('MM/DD/YYYY HH:mm'),
                }); // MM/DD/YYYY HH:mm
              }}>
              <Image
                source={this.state.start_time ? PAUSE_ICON : PLAY_ICON}
                style={{resizeMode: 'contain', height: 25, width: 25}}
              />
            </TouchableOpacity>

            <TouchableOpacity>
              <Image
                source={CLOSE_ICON}
                style={{resizeMode: 'contain', height: 20, width: 20}}
              />
            </TouchableOpacity>

            <TouchableOpacity
              onPress={() => {
                Alert.alert('Info', '0 points received from 0 points possible');
              }}>
              <Text>0/0</Text>
            </TouchableOpacity>

            <TouchableOpacity
              onPress={() =>
                Alert.alert(
                  'Options',
                  `Turn Notifications On`,
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
})(PASTab);

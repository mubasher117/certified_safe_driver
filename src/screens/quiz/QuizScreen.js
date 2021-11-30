/* eslint-disable prettier/prettier */
import React from 'react';
import {
  View,
  TouchableOpacity,
  TouchableWithoutFeedback,
  NativeModules,
  Image,
  Alert,
} from 'react-native';
import {connect} from 'react-redux';
import {Loader, Text, Header} from '../../components';
import {
  IS_TAB,
  SCREEN_WIDTH,
  PREVIEW_ICON,
  SAVE_ICON,
  UNDO_ICON,
} from '../../constants';
import * as colors from '../../styles/colors';
import NavigationService from '../../navigation/NavigationService';
import ActionSheet from 'react-native-actionsheet';
import InfoTab from './quiz/InfoTab';
import DefenseQuizTab from './quiz/DefenseQuizTab';
import DistractedQuizTab from './quiz/DistractedQuizTab';
import DaysTruckSchoolTab from './quiz/DaysTruckSchoolTab';
import TimeSheet from './quiz/TimeSheet';
import {scale} from '../../utils/scale';
import CkOffsheet from './quiz/CkOffsheet';
import {apiPatch, apiPost} from '../../utils/http';
import _ from 'lodash';

const {UIManager} = NativeModules;
UIManager.setLayoutAnimationEnabledExperimental &&
  UIManager.setLayoutAnimationEnabledExperimental(true);

const tabs = [
  'Info Tab',
  'CK Offsheet',
  'Truck Driving School',
  'Timesheet',
  'Defensive Driving Quiz',
  'Distracted Quiz',
];
class QuizScreen extends React.Component {
  state = {
    selectedTab: 'Info Tab',
    saving: false,
    discarding: false,
    previewing: false,
    DistractedMounted: false,
    accessableTabs: [
      'Info Tab',
      'CK Offsheet',
      'Truck Driving School',
      'Timesheet',
      'Defensive Driving Quiz',
      'Distracted Quiz',
    ],
    truckDriver: React.createRef(),
  };
  async componentDidMount() {}
  componentDidUpdate(prevProps, prevState) {
    if (prevProps.student_info != this.props.student_info) {
      this.setState(
        {
          selectedTab: 'Info Tab',
          saving: false,
          previewing: false,
          DistractedMounted: false,
        },
        () => {
          if (this.props.student_info == null) {
            this.setState({
              accessableTabs: [
                'Info Tab',
                'CK Offsheet',
                'Timesheet',
                'Truck Driving School',
                'Defensive Driving Quiz',
                'Distracted Quiz',
              ],
            });
          }
        },
      );
    }
  }
  updateTruckDrivingSchoolInfo = (tds_data) => {
    const {
      company_info,
      student_info,
      selected_test,
    } = this.props.eveluationFlowReducer;
    console.log(student_info?.id);
    console.log(selected_test?.id);
    tds_data.days.map((day, index) => {
      tds_data.day_list[day].map((driving_record, inner_index) => {
        const test_id = driving_record.id;
        const data = {
          location: driving_record.location,
          planned: driving_record.planned,
          actual: driving_record.actual,
          initials: driving_record.initials,
        };
        apiPatch(
          `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/training-records/${test_id}/`,
          data,
          true,
        );
      });
    });
    console.log(this.state.truckDriver?.current?.state?.comments)
    _.forEach(this.state.truckDriver?.current?.state?.comments, (value, key) => {
      apiPost(
            `/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/tdc/training-records/comments/`, 
            {
              "day": parseInt(key),
              "body": value
            }
            )
          })

  };
  renderHeaderRight = () => {
    const {selectedTab, saving, discarding, previewing} = this.state;
    const {
      tabChangeErrorMessage,
      eveluationFlowReducer,
      userReducer,
    } = this.props;
    switch (selectedTab) {
      case 'Info Tab': {
        return (
          <View
            style={{
              flexDirection: 'row',
              justifyContent: 'center',
              alignItems: 'center',
            }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({discarding: true});
                await this._infoTab.reload();
                this.setState({discarding: false});
              }}>
              {discarding ? (
                <Loader />
              ) : (
                <Image source={UNDO_ICON} style={{height: 30, width: 30}} />
              )}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                if (
                  eveluationFlowReducer &&
                  eveluationFlowReducer.selected_test.status != 'pending'
                ) {
                  Alert.alert('You cannot edit a completed test');
                  this._infoTab.reload();
                  return;
                } else if (
                  userReducer &&
                  userReducer.userProfile.id !==
                    eveluationFlowReducer.instructor_info.id
                ) {
                  // id or instructor id evaulationred id  !=  id
                  Alert.alert('You are not instructor for this test');
                  // you are instructor
                  return;
                }
                this.setState({saving: true});
                await this._infoTab.saveInfo();
                this.setState({saving: false});
              }}>
              {saving ? (
                <Loader />
              ) : (
                <Image
                  source={SAVE_ICON}
                  style={{height: 26, width: 26, marginHorizontal: 10}}
                />
              )}
            </TouchableOpacity>

            <TouchableOpacity
              onPress={async () => {
                this.setState({previewing: true});
                await this._infoTab.preview();
                this.setState({previewing: false});
              }}>
              {previewing ? (
                <Loader />
              ) : (
                <Image
                  source={PREVIEW_ICON}
                  style={{
                    height: 25,
                    width: 25,
                    marginRight: 4,
                  }}
                />
              )}
            </TouchableOpacity>
          </View>
        );
      }
      case 'Truck Driving School': {
        return (
          <View
            style={{
              flexDirection: 'row',
              justifyContent: 'center',
              alignItems: 'center',
            }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({discarding: true});
                // await this._dayzTruckSchoolTab.reload();
                this.setState({selectedTab: 'Info Tab'});
                this.setState({discarding: false});
              }}>
              {discarding ? (
                <Loader />
              ) : (
                <Image source={UNDO_ICON} style={{height: 30, width: 30}} />
              )}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                if (
                  eveluationFlowReducer &&
                  eveluationFlowReducer.selected_test.status != 'pending'
                ) {
                  Alert.alert('You cannot edit a completed test');
                  this._dayzTruckSchoolTab.reload();
                  return;
                } else if (
                  userReducer &&
                  userReducer.userProfile.id !==
                    eveluationFlowReducer.instructor_info.id
                ) {
                  // id or instructor id evaulationred id  !=  id
                  // Alert.alert('You are not instructor for this test');
                  this.updateTruckDrivingSchoolInfo(
                    this.state.truckDriver.current.state.truckDrvingSchool,
                  );
                  Alert.alert('Saved successfully');
                  // this.setState({selectedTab: 'Info Tab'});
                  // you are instructor
                  return;
                }
                this.updateTruckDrivingSchoolInfo(
                  this.state.truckDriver.current.state.truckDrvingSchool,
                );
                Alert.alert('Saved successfully');
                // this.setState({selectedTab: 'Info Tab'});

                this.setState({saving: false});
                // this.setState({saving: true});
                // await this._dayzTruckSchoolTab.saveInfo();
                // this.setState({saving: false});
              }}>
              {saving ? (
                <Loader />
              ) : (
                <Image
                  source={SAVE_ICON}
                  style={{height: 26, width: 26, marginHorizontal: 10}}
                />
              )}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                this.state.truckDriver.current.setState({showPreview: true});
              }}>
              <Image
                source={PREVIEW_ICON}
                style={{height: 25, width: 25, marginRight: 4}}
              />
            </TouchableOpacity>
          </View>
        );
      }
      case 'Defensive Driving Quiz': {
        return (
          <View
            style={{
              flexDirection: 'row',
              justifyContent: 'center',
              alignItems: 'center',
            }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({discarding: true});
                await this._defenseTab.reload();
                this.setState({discarding: false});
              }}>
              {discarding ? (
                <Loader />
              ) : (
                <Image source={UNDO_ICON} style={{height: 30, width: 30}} />
              )}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                if (
                  eveluationFlowReducer &&
                  eveluationFlowReducer.selected_test.status != 'pending'
                ) {
                  Alert.alert('You cannot edit a completed test');
                  this._defenseTab.reload();
                  return;
                } else if (
                  userReducer &&
                  userReducer.userProfile.id !==
                    eveluationFlowReducer.instructor_info.id
                ) {
                  // id or instructor id evaulationred id  !=  id
                  Alert.alert('You are not instructor for this test');
                  // you are instructor
                  return;
                }
                this.setState({saving: true});
                await this._defenseTab.submitQuiz();
                this.setState({saving: false});
                this._defenseTab.getQuizStats();
              }}>
              {saving ? (
                <Loader />
              ) : (
                <Image
                  source={SAVE_ICON}
                  style={{height: 26, width: 26, marginHorizontal: 10}}
                />
              )}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                this.setState({previewing: true});
                await this._defenseTab.preview();
                this.setState({previewing: false});
              }}>
              {previewing ? (
                <Loader />
              ) : (
                <Image
                  source={PREVIEW_ICON}
                  style={{
                    height: 25,
                    width: 25,
                    marginRight: 4,
                  }}
                />
              )}
            </TouchableOpacity>
          </View>
        );
      }
      case 'Distracted Quiz': {
        return (
          <View
            style={{
              flexDirection: 'row',
              justifyContent: 'center',
              alignItems: 'center',
            }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({discarding: true});
                await this._distractedTab.getDistractedInfo();
                this.setState({discarding: false});
              }}>
              {discarding ? (
                <Loader />
              ) : (
                <Image source={UNDO_ICON} style={{height: 30, width: 30}} />
              )}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                if (
                  eveluationFlowReducer &&
                  eveluationFlowReducer.selected_test.status != 'pending'
                ) {
                  Alert.alert('You cannot edit a completed test');
                  return;
                } else if (
                  userReducer &&
                  userReducer.userProfile.id !==
                    eveluationFlowReducer.instructor_info.id
                ) {
                  // id or instructor id evaulationred id  !=  id
                  Alert.alert('You are not instructor for this test');
                  // you are instructor
                  return;
                }
                this.setState({saving: true});
                await this._distractedTab.submitQuiz();
                await this._distractedTab.getQuizStats();
                this.setState({saving: false});
              }}>
              {saving ? (
                <Loader />
              ) : (
                <Image
                  source={SAVE_ICON}
                  style={{height: 26, width: 26, marginHorizontal: 10}}
                />
              )}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                this.setState({previewing: true});
                await this._distractedTab.preview();
                this.setState({previewing: false});
              }}>
              {previewing ? (
                <Loader />
              ) : (
                <Image
                  source={PREVIEW_ICON}
                  style={{
                    height: 25,
                    width: 25,
                    marginRight: 4,
                  }}
                />
              )}
            </TouchableOpacity>
          </View>
        );
      }
      case 'Timesheet': {
        return (
          <View
            style={{
              flexDirection: 'row',
              justifyContent: 'center',
              alignItems: 'center',
            }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({discarding: true});
                await this._timesheetTab.reload();
                this.setState({discarding: false});
              }}>
              {discarding ? (
                <Loader />
              ) : (
                <Image source={UNDO_ICON} style={{height: 30, width: 30}} />
              )}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                if (
                  eveluationFlowReducer &&
                  eveluationFlowReducer?.selected_test?.status != 'pending'
                ) {
                  Alert.alert('You cannot edit a completed test');
                  this._timesheetTab.reload();
                  return;
                } else if (
                  userReducer &&
                  userReducer.userProfile.id !==
                    eveluationFlowReducer.instructor_info.id
                ) {
                  // id or instructor id evaulationred id  !=  id
                  Alert.alert('You are not instructor for this test');
                  // you are instructor
                  return;
                }
                this.setState({saving: true});
                await this._timesheetTab.saveInfo();
                this.setState({saving: false});
              }}>
              {saving ? (
                <Loader />
              ) : (
                <Image
                  source={SAVE_ICON}
                  style={{height: 26, width: 26, marginHorizontal: 10}}
                />
              )}
            </TouchableOpacity>

            <TouchableOpacity
              onPress={async () => {
                this._timesheetTab.setState({showPreview: true});
              }}>
              <Image
                source={PREVIEW_ICON}
                style={{height: 25, width: 25, marginRight: 4}}
              />
            </TouchableOpacity>
          </View>
        );
      }

      case 'CK Offsheet': {
        return (
          <View
            style={{
              flexDirection: 'row',
              justifyContent: 'center',
              alignItems: 'center',
            }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({discarding: true});
                await this._ckOfsheetTab.reload();
                this.setState({discarding: false});
              }}>
              {discarding ? (
                <Loader />
              ) : (
                <Image source={UNDO_ICON} style={{height: 30, width: 30}} />
              )}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                if (
                  eveluationFlowReducer &&
                  eveluationFlowReducer.selected_test.status != 'pending'
                ) {
                  Alert.alert('You cannot edit a completed test');
                  this._dayzTruckSchoolTab.reload();
                  return;
                } else if (
                  userReducer &&
                  userReducer.userProfile.id !==
                    eveluationFlowReducer.instructor_info.id
                ) {
                  // id or instructor id evaulationred id  !=  id
                  Alert.alert('You are not instructor for this test');
                  // you are instructor
                  return;
                }
                this.setState({saving: true});
                await this._ckOfsheetTab.saveInfo();
                this.setState({saving: false});
              }}>
              {saving ? (
                <Loader />
              ) : (
                <Image
                  source={SAVE_ICON}
                  style={{height: 26, width: 26, marginHorizontal: 10}}
                />
              )}
            </TouchableOpacity>

            <TouchableOpacity
              onPress={async () => {
                this._ckOfsheetTab.setState({showPreview: true});
              }}>
              <Image
                source={PREVIEW_ICON}
                style={{height: 25, width: 25, marginRight: 4, }}
              />
            </TouchableOpacity>
          </View>
        );
      }

      default:
        break;
    }
  };

  renderTabComponent = () => {
    const {selectedTab, DistractedMounted} = this.state;
    const {tabChangeErrorMessage} = this.props;
    // switch (selectedTab) {
    //   case 'Info Tab': return <InfoTab />
    //   case '6 Days Truck Driving School': return <DaysTruckSchoolTab />
    //   case 'Defensive Driving Quiz': return <DefenseQuizTab />
    //   case 'Distracted Quiz': return <DistractedQuizTab />
    //   default:
    //     break;
    // }
    return (
      <>
        <InfoTab
          ref={(r) => (this._infoTab = r)}
          shown={selectedTab == 'Info Tab'}
        />
        <DaysTruckSchoolTab
          // ref={(r) => {
          //   this.setState({truckDriver: r})
          //   this._dayzTruckSchoolTab = r

          // }}
          ref={this.state.truckDriver}
          shown={selectedTab === 'Truck Driving School'}
        />
        <DefenseQuizTab
          ref={(r) => (this._defenseTab = r)}
          shown={selectedTab == 'Defensive Driving Quiz'}
        />
        <DistractedQuizTab
          ref={(r) => (this._distractedTab = r)}
          shown={selectedTab == 'Distracted Quiz'}
        />
        <TimeSheet
          ref={(r) => (this._timesheetTab = r)}
          shown={selectedTab === 'Timesheet'}
        />
        <CkOffsheet
          ref={(r) => (this._ckOfsheetTab = r)}
          shown={selectedTab === 'CK Offsheet'}
        />
      </>
    );
  };

  onChangeTab = (_tab) => {
    let tab = _tab;
    const {tabChangeErrorMessage} = this.props;
    if (tabChangeErrorMessage == false) {
      requestAnimationFrame(() => {
        if (this.state[`${tab}Mounted`]) {
          requestAnimationFrame(() => {
            this.setState({selectedTab: tab});
          });
        } else {
          this.setState(
            {
              [`${tab}Mounted`]: true,
            },
            () => {
              requestAnimationFrame(() => {
                this.setState({selectedTab: tab});
              });
            },
          );
        }
      });
    } else {
      alert(tabChangeErrorMessage);
    }
  };

  render() {
    const {selectedTab, accessableTabs, truckDriver} = this.state;
    const {tabChangeErrorMessage} = this.props;
    return (
      <View style={{flex: 1, justifyContent: 'space-between'}}>
        <Header>
          <Text onPress={() => NavigationService.navigate('HomeScreen')}>
            Home
          </Text>
          <>
            {IS_TAB ? (
              <View
                horizontal
                style={{flexDirection: 'row', flex: 1, marginHorizontal: 5}}>
                {accessableTabs.map((tab) => (
                  <TouchableWithoutFeedback
                    onPress={() => {
                      if (tabChangeErrorMessage == false) {
                        this.onChangeTab(tab);
                      } else {
                        alert(tabChangeErrorMessage);
                      }
                    }}>
                    <View
                      style={{
                        flex: 1,
                        justifyContent: 'center',
                        alignItems: 'center',
                        marginRight: scale(5),
                        borderWidth: 1,
                        borderRadius: 5,
                        borderColor: colors.APP_BORDER_GRAY_COLOR,
                        padding: scale(5),
                        backgroundColor:
                          selectedTab == tab ? 'white' : colors.APP_GRAY_COLOR,
                      }}>
                      <Text style={{fontSize: 12}}>{tab}</Text>
                    </View>
                  </TouchableWithoutFeedback>
                ))}
              </View>
            ) : (
              <TouchableWithoutFeedback
                onPress={() => {
                  if (tabChangeErrorMessage == false) {
                    this._tabsActionSheet.show();
                  } else {
                    alert(tabChangeErrorMessage);
                  }
                }}>
                <View
                  style={{
                    flex: 1,
                    position: 'absolute',
                    left:
                      SCREEN_WIDTH / 2 -
                      scale(selectedTab.length * 2) -
                      scale(28),
                    bottom: 10,
                  }}>
                  <Text style={{alignSelf: 'center'}}>{selectedTab}</Text>
                </View>
              </TouchableWithoutFeedback>
            )}
          </>
          {this.renderHeaderRight()}
        </Header>
        <ActionSheet
          ref={(o) => (this._tabsActionSheet = o)}
          title={'Options'}
          options={[...accessableTabs, 'Cancel']}
          cancelButtonIndex={10}
          // destructiveButtonIndex={10}
          onPress={(index) => {
            console.log('QuizScreen actionsheet index', index);
            if (index < accessableTabs.length) {
              this.onChangeTab(accessableTabs[index]);
              // requestAnimationFrame(() => {
              //   if (this.state[`${accessableTabs[index]}Mounted`]) {
              //     requestAnimationFrame(() => {
              //       this.setState({ selectedTab: accessableTabs[index] })
              //     });
              //   } else {
              //     this.setState({
              //       [`${accessableTabs[index]}Mounted`]: true
              //     }, () => {
              //       requestAnimationFrame(() => {
              //         this.setState({ selectedTab: accessableTabs[index] })
              //       });
              //     })
              //   }
              // })
              // requestAnimationFrame(() => {
              //   this.setState({ selectedTab: accessableTabs[index] })
              // });
              // this.setState({ selectedTab: accessableTabs[index] })
            }
          }}
        />
        {this.renderTabComponent()}
      </View>
    );
  }
}

const mapStateToProps = (state) => {
  // console.log('state.eveluationFlowReducer QuizScreen: ', state.eveluationFlowReducer);
  return {
    userReducer: state.userReducer,
    tabChangeErrorMessage: state.eveluationFlowReducer.tabChangeErrorMessage,
    selectedTestInfo: state.eveluationFlowReducer.selectedTestInfo,
    student_info: state.eveluationFlowReducer.student_info,
    eveluationFlowReducer: state.eveluationFlowReducer,
  };
};

export default connect(mapStateToProps, {})(QuizScreen);

import React from 'react';
import { View, TouchableOpacity, Image, Modal, Alert } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
import { connect } from 'react-redux';
import { Text, Loader, ScreenWrapper, EvaluationField, Evaluation7OptionField, DateTimePicker, Header, SignaturePicker, EvaluationYesNoOptionField, Footer, Selector } from '../../components';
import { fetchUserProfileAction, hideSelector, showPopup, showSelector, updateTabChangeErrorMessage, errorMessage } from '../../actions';
import { PLATFORM_IOS, RIGHT_ARROW_ICON, CALENDAR_ICON, PLAY_ICON, PAUSE_ICON, EXPORT_ICON, PLUS_ICON, CLOSE_ICON, } from '../../constants';
import { ProdsDataModals, ProdsDataEquipModal } from '../../utils/ProdsDataModals';
import _ from 'lodash';
import * as colors from '../../styles/colors';
import { counterToAlpha, getDataDiff } from '../../utils/function';
import { apiGet, apiPut, apiPatch, apiPost } from '../../utils/http';
import { WebView } from 'react-native-webview';
import { scale } from '../../utils/scale';
import RNHTMLtoPDF from 'react-native-html-to-pdf';
import Share from 'react-native-share';
import moment from 'moment';
import PROD from './preview/PRODPreviewHTML';

class ProdTab extends React.Component {

  state = {
    // ...ProdsDataModals,
    signature: null,
    mounting: true,
    showPreview: false,
    apiData: {},
  }

  async componentDidMount() {
    console.log('ProdsDataModals', ProdsDataModals)
    //set base state
    let state = {}
    Object.keys(ProdsDataModals).forEach(key => {
      state[key] = null;
    })
    this.setState({ ...state, }, this.getData);
  }

  componentDidUpdate(prevProps, prevState) {
    if (this.props.shown && prevProps.tabChangeErrorMessage == this.props.tabChangeErrorMessage) {
      const isDiff = getDataDiff({ ...this.state.apiData }, this.state)
      console.log('isDiff', isDiff)
      if (isDiff) {
        if (this.props.tabChangeErrorMessage == false)
          this.props.updateTabChangeErrorMessage('Please save your changes')
      } else {
        if (this.props.tabChangeErrorMessage !== false)
          this.props.updateTabChangeErrorMessage(false)
      }
    }
  }

  getData = async () => {
    // this.setState({ mounting: false })
    // return false;

    const { company_info, student_info, selected_test } = this.props.eveluationFlowReducer
    let res = await apiGet(`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/prod/`)
    if (res && res.data) {
      console.log('data', res.data)
      let prodItemsRes = await apiGet(`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/prod/items/`)
      console.log('prodItemsRes:', prodItemsRes)

      // let equipmentRes = await apiGet(`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/equips/`)
      // console.log(`equipmentRes: `, equipmentRes);
      // if (equipmentRes && equipmentRes.data && equipmentRes.data.length) {
      //   equipmentRes.data.reverse()
      //   this.setState({ studentEquipInfo: equipmentRes.data });
      // } else {
      //   errorMessage('No Equipment found\nPlease add equipment from equipment tab')
      // }

      this.setState({ ...res.data, apiData: res.data, mounting: false })

    } else {
      this.setState({ mounting: false })
    }
    return true;
  }

  saveProd = async () => {
    const isDiff = getDataDiff({ ...this.state.apiData }, this.state)
    if (!isDiff) {
      return
    }
    //TODO: how to upload signature
    let newState = {}
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

    // let newState = this.state;
    // _.forEach(newState, (value, _state) => {
    //   if (_state.includes('signature'))
    //     delete newState[_state]
    // })
    // newState.prod_items = [
    //   {
    //     title: 'testing title',
    //     trailer: '112233'
    //   }
    // ]
    const { company_info, student_info, selected_test } = this.props.eveluationFlowReducer
    let res = await apiPatch(`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/prod/`, newState, true)
    console.log(`prod put res: `, res)
    if (res && res.data) {
      this.setState({ ...res.data, apiData: res.data })
      // this.props.navigation.goBack()
      // errorMessage('Student Info Updated')
      // this.getData();
    }
    return true;
  }

  previewProd = async () => {
    await this.saveProd();
    await this.getData();
    this.setState({ showPreview: true })
  }

  render() {
    if (this.state.mounting) {
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
    const { company_info, student_info, selected_test } = eveluationFlowReducer
    return (
      <>
        <ScreenWrapper parentStyle={this.props.shown ? show : hide}>
          <KeyboardAwareScrollView enableAutomaticScroll={false}>

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
                      html: PROD(),
                      fileName: `student_${eveluationFlowReducer.student_info?.id}_PROD`,
                      // directory: 'Documents',
                    };
                    this.setState({ showPreview: false })
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
                  source={{ html: PROD() }}
                  ref={ref => { this.WebView = ref; }}
                  javaScriptEnabled={true}
                  domStorageEnabled={true}
                  startInLoadingState={true}
                />
              </View>
            </Modal>

            {_.map(ProdsDataModals, (level1) => {
              // console.log('level1', level1.value)
              ++level1Counter;
              // level2Counter = 0;
              if (level1.value == null) {
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
                      // required
                      rightArrow
                      title={`${level1.title}`}
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
                      key={level1.key}
                      title={`${level1.title}`}
                      value={this.state[level1.key]}
                      onChangeText={value => this.setState({ [level1.key]: value })}
                    />
                  )
                }
              } else if (level1.value === false || level1.value === true) {
                return (
                  <View style={{ backgroundColor: 'white' }}>
                    <EvaluationYesNoOptionField
                      start_time={this.state.start_time}
                      end_time={this.state.end_time}
                      key={level1.key}
                      title={`${level1.title}`}
                      value={this.state[level1.key]}
                      onChange={value => this.setState({ [level1.key]: value })}
                    />
                  </View>
                )
              }
            })}
          </KeyboardAwareScrollView>
        </ScreenWrapper>
        {this.props.shown && <Footer>

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
                          await this.saveProd();
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
          {/* <TouchableOpacity>
            <Image source={CLOSE_ICON} style={{ resizeMode: 'contain', height: 20, width: 20 }} />
          </TouchableOpacity> */}

          <TouchableOpacity onPress={() => {
            Alert.alert("Info", "0 points received from 0 points possible");
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
          <TouchableOpacity onPress={() => {
            showSelector(<Selector
              title={'Equipments'}
              endpoint={`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/equips/`}
              displayKey={'power_unit_number'}
              resultPath={'data'}
              onSelect={async (item) => {
                console.log('item equip: ', item);
                Alert.alert('Adding New Equipment', `Are you sure you want to add entry for equipment\n ${item.power_unit_number}`,
                  [
                    {
                      text: 'No',
                      onPress: () => console.log('No Pressed'),
                      style: 'no',
                    },
                    {
                      text: 'Yes',
                      onPress: async () => {
                        let prodItemData = {
                          trailer: item.power_unit_number
                        }
                        let res = await apiPost(`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/prod/items/`, prodItemData)
                        if(res && res.data){
                          this.getData();
                        }
                      }
                    },
                  ],
                  { cancelable: false })
              }}
            />)
          }}>
            <Image source={PLUS_ICON} style={{ resizeMode: 'contain', height: 20, width: 20, paddingRight: 10 }} />
          </TouchableOpacity>
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

export default connect(mapStateToProps, { fetchUserProfileAction, updateTabChangeErrorMessage }, null, { forwardRef: true })(ProdTab);
import React from 'react';
import { View, ScrollView, TouchableOpacity, TouchableWithoutFeedback, NativeModules, LayoutAnimation, Image, Alert } from 'react-native';
import { connect } from 'react-redux';
import { Loader, Text, Header, Footer } from '../../components';
import SplashScreen from 'react-native-splash-screen'
import { fetchUserProfileAction } from '../../actions';
import { EXPORT_ICON, IS_TAB, SCREEN_WIDTH, PREVIEW_ICON, SAVE_ICON, UNDO_ICON } from '../../constants';
import * as colors from '../../styles/colors';
import NavigationService from '../../navigation/NavigationService';
import ActionSheet from 'react-native-actionsheet'
import InfoTab from './InfoTab';
import EquipTab from './EquipTab';
import EyeTab from './EyeTab';
import NotesTab from './NotesTab';
import ProdTab from './ProdTab';
import PreTripTab from './PreTripTab';
import BTWTab from './BTWTab';
import SWPTab from './SWPTab';
import VRTTab from './VRTTab';
import PASTab from './PASTab';
import { scale } from '../../utils/scale';

const { UIManager } = NativeModules;
UIManager.setLayoutAnimationEnabledExperimental &&
  UIManager.setLayoutAnimationEnabledExperimental(true)

const tabs = [
  'Info',
  'Equip',
  'Eye',
  'Notes',
  'Prod',
  'Pre Trip',
  'BTW',
  'SWP',
  'VRT',
  'PAS',
]
class EvaluationScreen extends React.Component {
  state = {
    selectedTab: 'Info',
    saving: false,
    discarding: false,
    previewing: false,
    EquipMounted: false,
    EyeMounted: false,
    NotesMounted: false,
    ProdMounted: false,
    PreTripMounted: false,
    BTWMounted: false,
    SWPMounted: false,
    VRTMounted: false,
    PASMounted: false,
    accessableTabs: [
      'Info',
    ],
    // [
    //   'Info',
    //   'Prod',
    //   'PreTrip',
    //   'BTW',
    //   'SWP',
    //   'VRT',
    //   'PAS',
    // ]
  }
  async componentDidMount() {

  }

  componentDidUpdate(prevProps, prevState) {
    if (prevProps.student_info != this.props.student_info) {
      this.setState({
        selectedTab: 'Info',
        saving: false,
        previewing: false,
        isSsInProgress: false,
        EquipMounted: false,
        EyeMounted: false,
        NotesMounted: false,
        ProdMounted: false,
        PreTripMounted: false,
        BTWMounted: false,
        SWPMounted: false,
        VRTMounted: false,
        PASMounted: false,
        // accessableTabs: ['Info']
      }, () => {
        if (this.props.student_info == null) {
          this.setState({ accessableTabs: ['Info'] })
        }
        // console.warn('disabling all tabs so they remount, student changed')
      })
    }
    if (this.props.selectedTestInfo && prevProps.selectedTestInfo != this.props.selectedTestInfo) {
      let accessableTabs = [
        'Info',
        'Notes',
      ];
      const {
        equipement,//equip
        eye_movement,//eye
        production, //prod
        pre_post_trip,//pre
        passenger_pre_trip,
        behind_the_wheel, //btw
        safe_work_practice,//swp
        vehicle_road_test, //vrt
        passenger_evacuation, //pas
      } = this.props.selectedTestInfo
      if (equipement) {
        accessableTabs.push('Equip')
      }
      if (eye_movement) {
        accessableTabs.push('Eye')
      }
      if (production) {
        accessableTabs.push('Prod')
      }
      if (pre_post_trip) {
        accessableTabs.push('PreTrip')
      }
      if (behind_the_wheel) {
        accessableTabs.push('BTW')
      }
      if (safe_work_practice) {
        accessableTabs.push('SWP')
      }
      if (vehicle_road_test) {
        accessableTabs.push('VRT')
      }
      // if (passenger_evacuation) {
      //   accessableTabs.push('PAS')
      // }
      this.setState({ accessableTabs })
      // tabs = [
      //   'Info',
      //   'Equip',
      //   'Eye',
      //   'Notes',
      //   'Prod',
      //   'Pre Trip',
      //   'BTW',
      //   'SWP',
      //   'VRT',
      //   'PAS',
      // ]
    }
  }

  renderHeaderRight = () => {
    const { selectedTab, saving, discarding, previewing, EquipMounted, EyeMounted, NotesMounted, ProdMounted, PreTripMounted, BTWMounted, SWPMounted, VRTMounted, PASMounted } = this.state
    const { tabChangeErrorMessage, eveluationFlowReducer, userReducer } = this.props
    switch (selectedTab) {
      case 'Info': {
        return (
          <View style={{ flexDirection: 'row', justifyContent: 'center', alignItems: 'center' }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({ discarding: true })
                await this._infoTab.reload()
                this.setState({ discarding: false })
              }}>
              {discarding ? <Loader /> : <Image source={UNDO_ICON} style={{ height: 30, width: 30 }} />}
            </TouchableOpacity>
            <TouchableOpacity onPress={async () => {
              if (eveluationFlowReducer && eveluationFlowReducer.selected_test.status != 'pending') {
                Alert.alert('You cannot edit a completed test')
                this._infoTab.reload()
                return;
              } else if (userReducer.userProfile.id != eveluationFlowReducer.instructor_info.id) { // id or instructor id evaulationred id  !=  id
                Alert.alert('You are not instructor for this test')
                // you are instructor
                return;
              }
              this.setState({ saving: true })
              await this._infoTab.saveInfo()
              this.setState({ saving: false })
            }}>
              {saving ? <Loader /> : <Image source={SAVE_ICON} style={{ height: 26, width: 26, marginHorizontal: 10 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {

                this.setState({ previewing: true })
                await this._infoTab.previewInfo()
                this.setState({ previewing: false })
              }}>
              {previewing ? <Loader /> : <Image
                source={PREVIEW_ICON}
                style={{height: 25, width: 25, marginRight: 4, marginRight: 4}}
              />
      }
            </TouchableOpacity>
          </View>
        )
      }
      case 'Equip': {
        return (
          <View style={{ flexDirection: 'row', justifyContent: 'center', alignItems: 'center' }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({ discarding: true })
                await this._equipTab.getEquipInfo();
                this.setState({ discarding: false })
              }}>
              {discarding ? <Loader /> : <Image source={UNDO_ICON} style={{ height: 30, width: 30 }} />}
            </TouchableOpacity>
            <TouchableOpacity onPress={async () => {
              if (eveluationFlowReducer && eveluationFlowReducer.selected_test.status != 'pending') {
                Alert.alert('You cannot edit a completed test')
                return;
              } else if (userReducer.userProfile.id != eveluationFlowReducer.instructor_info.id) { // id or instructor id evaulationred id  !=  id
                Alert.alert('You are not instructor for this test')
                // you are instructor
                return;
              }
              this.setState({ saving: true })
              await this._equipTab.saveEquip()
              this.setState({ saving: false })
            }}>
              {saving ? <Loader /> : <Image source={SAVE_ICON} style={{ height: 26, width: 26, marginHorizontal: 10 }} />}
            </TouchableOpacity>
          </View>
        )
      }
      case 'Eye': {
        return (
          <View style={{ flexDirection: 'row', justifyContent: 'center', alignItems: 'center' }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({ discarding: true })
                await this._eyeTab.getEye()
                this.setState({ discarding: false })
              }}>
              {discarding ? <Loader /> : <Image source={UNDO_ICON} style={{ height: 30, width: 30 }} />}
            </TouchableOpacity>
            <TouchableOpacity onPress={async () => {
              if (eveluationFlowReducer && eveluationFlowReducer.selected_test.status != 'pending') {
                Alert.alert('You cannot edit a completed test')
                return;
              } else if (userReducer.userProfile.id != eveluationFlowReducer.instructor_info.id) { // id or instructor id evaulationred id  !=  id
                Alert.alert('You are not instructor for this test')
                // you are instructor
                return;
              }
              this.setState({ saving: true })
              await this._eyeTab.saveEye()
              this.setState({ saving: false })
            }}>
              {saving ? <Loader /> : <Image source={SAVE_ICON} style={{ height: 26, width: 26, marginHorizontal: 10 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                this.setState({ isSsInProgress: true })
                await this._eyeTab.takeScreenShot()
                this.setState({ isSsInProgress: false })
              }}>
              {this.state.isSsInProgress ? <Loader /> : <Image source={EXPORT_ICON} style={{ height: 20, width: 20, marginRight: 4, marginRight: 4 }} />}
            </TouchableOpacity> 
            <TouchableOpacity
              onPress={async () => {
                this.setState({ previewing: true })
                await this._eyeTab.shareImg()
                this.setState({ previewing: false })
              }}>
              {previewing ? <Loader /> : <Image source={EXPORT_ICON} style={{ height: 20, width: 20, marginRight: 4, marginRight: 4 }} />}
            </TouchableOpacity>
          </View>
        )
      }
      case 'Notes': {
        return (
          <View style={{ flexDirection: 'row', justifyContent: 'center', alignItems: 'center' }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({ discarding: true })
                await this._btwTab.getData()
                this.setState({ discarding: false })
              }}>
              {discarding ? <Loader /> : <Image source={UNDO_ICON} style={{ height: 30, width: 30 }} />}
            </TouchableOpacity>
            <TouchableOpacity onPress={async () => {
              if (eveluationFlowReducer && eveluationFlowReducer.selected_test.status != 'pending') {
                Alert.alert('You cannot edit a completed test')
                // you are instructor
                return;
              } else if (userReducer.userProfile.id != eveluationFlowReducer.instructor_info.id) { // id or instructor id evaulationred id  !=  id
                Alert.alert('You are not instructor for this test')
                // you are instructor
                return;
              }
              this.setState({ saving: true })
              await this._notesTab.saveNote()
              this.setState({ saving: false })
            }}>
              {saving ? <Loader /> : <Image source={SAVE_ICON} style={{ height: 26, width: 26, marginHorizontal: 10 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                this.setState({ previewing: true })
                await this._notesTab.saveNote()
                await this._notesTab.previewNotes()
                this.setState({ previewing: false })
              }}>
              {previewing ? <Loader /> : <Image source={PREVIEW_ICON} style={{ height: 25, width: 25, marginRight: 4, marginRight: 4 }} />}
            </TouchableOpacity>
          </View>
        )
      }
      case 'Prod': {
        return (
          <View style={{ flexDirection: 'row', justifyContent: 'center', alignItems: 'center' }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({ discarding: true })
                await this._prodTab.getData()
                this.setState({ discarding: false })
              }}>
              {discarding ? <Loader /> : <Image source={UNDO_ICON} style={{ height: 30, width: 30 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              disabled={saving}
              onPress={async () => {
                if (eveluationFlowReducer && eveluationFlowReducer.selected_test.status != 'pending') {
                  Alert.alert('You cannot edit a completed test')
                  return;
                } else if (userReducer.userProfile.id != eveluationFlowReducer.instructor_info.id) { // id or instructor id evaulationred id  !=  id
                  Alert.alert('You are not instructor for this test')
                  // you are instructor
                  return;
                }
                this.setState({ saving: true })
                await this._prodTab.saveProd()
                this.setState({ saving: false })
              }}>
              {saving ? <Loader /> : <Image source={SAVE_ICON} style={{ height: 26, width: 26, marginHorizontal: 10 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                this.setState({ previewing: true })
                await this._prodTab.saveProd()
                await this._prodTab.previewProd()
                this.setState({ previewing: false })
              }}>
              {previewing ? <Loader /> : <Image source={PREVIEW_ICON} style={{ height: 25, width: 25, marginRight: 4 }} />}
            </TouchableOpacity>
          </View>
        )
      }
      case 'PreTrip': {
        return (
          <View style={{ flexDirection: 'row', justifyContent: 'center', alignItems: 'center' }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({ discarding: true })
                await this._preTripTab.getData()
                this.setState({ discarding: false })
              }}>
              {discarding ? <Loader /> : <Image source={UNDO_ICON} style={{ height: 30, width: 30 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              disabled={saving}
              onPress={async () => {
                if (eveluationFlowReducer && eveluationFlowReducer.selected_test.status != 'pending') {
                  Alert.alert('You cannot edit a completed test')
                  return;
                } else if (userReducer.userProfile.id != eveluationFlowReducer.instructor_info.id) { // id or instructor id evaulationred id  !=  id
                  Alert.alert('You are not instructor for this test')
                  // you are instructor
                  return;
                }
                this.setState({ saving: true })
                await this._preTripTab.savePreTrip()
                this.setState({ saving: false })
              }}>
              {saving ? <Loader /> : <Image source={SAVE_ICON} style={{ height: 26, width: 26, marginHorizontal: 10 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                this.setState({ previewing: true })
                await this._preTripTab.savePreTrip()
                await this._preTripTab.previewPreTrip()
                this.setState({ previewing: false })
              }}>
              {previewing ? <Loader /> : <Image source={PREVIEW_ICON} style={{ height: 25, width: 25, marginRight: 4 }} />}
            </TouchableOpacity>
          </View>
        )
      }
      case 'BTW': {
        return (
          <View style={{ flexDirection: 'row', justifyContent: 'center', alignItems: 'center' }}>
            <TouchableOpacity
              disabled={saving}
              onPress={async () => {
                this.setState({ discarding: true })
                await this._btwTab.getData()
                this.setState({ discarding: false })
              }}>
              {discarding ? <Loader /> : <Image source={UNDO_ICON} style={{ height: 30, width: 30 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              disabled={saving}
              onPress={async () => {
                if (eveluationFlowReducer && eveluationFlowReducer.selected_test.status != 'pending') {
                  Alert.alert('You cannot edit a completed test')
                  this._btwTab.getData()
                  return;
                } else if (userReducer.userProfile.id != eveluationFlowReducer.instructor_info.id) { // id or instructor id evaulationred id  !=  id
                  Alert.alert('You are not instructor for this test')
                  // you are instructor
                  return;
                }
                this.setState({ saving: true })
                await this._btwTab.saveBTW()
                this.setState({ saving: false })
              }}>
              {saving ? <Loader /> : <Image source={SAVE_ICON} style={{ height: 26, width: 26, marginHorizontal: 10 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                this.setState({ previewing: true })
                await this._btwTab.saveBTW()
                await this._btwTab.previewBTW()
                this.setState({ previewing: false })
              }}>
              {previewing ? <Loader /> : <Image source={PREVIEW_ICON} style={{ height: 25, width: 25, marginRight: 4 }} />}
            </TouchableOpacity>
          </View>
        )
      }
      case 'SWP': {
        return (
          <View style={{ flexDirection: 'row', justifyContent: 'center', alignItems: 'center' }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({ discarding: true })
                await this._swpTab.getData()
                this.setState({ discarding: false })
              }}>
              {discarding ? <Loader /> : <Image source={UNDO_ICON} style={{ height: 30, width: 30 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              disabled={saving}
              onPress={async () => {
                if (eveluationFlowReducer && eveluationFlowReducer.selected_test.status != 'pending') {
                  Alert.alert('You cannot edit a completed test')
                  return;
                } else if (userReducer.userProfile.id != eveluationFlowReducer.instructor_info.id) { // id or instructor id evaulationred id  !=  id
                  Alert.alert('You are not instructor for this test')
                  // you are instructor
                  return;
                }
                this.setState({ saving: true })
                await this._swpTab.saveSWP()
                this.setState({ saving: false })
              }}>
              {saving ? <Loader /> : <Image source={SAVE_ICON} style={{ height: 26, width: 26, marginHorizontal: 10 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                this.setState({ previewing: true })
                await this._swpTab.saveSWP()
                await this._swpTab.previewSWP()
                this.setState({ previewing: false })
              }}>
              {previewing ? <Loader /> : <Image source={PREVIEW_ICON} style={{ height: 25, width: 25, marginRight: 4 }} />}
            </TouchableOpacity>
          </View>
        )
      }
      case 'VRT': {
        return (
          <View style={{ flexDirection: 'row', justifyContent: 'center', alignItems: 'center' }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({ discarding: true })
                await this._vrtTab.getData()
                this.setState({ discarding: false })
              }}>
              {discarding ? <Loader /> : <Image source={UNDO_ICON} style={{ height: 30, width: 30 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              disabled={saving}
              onPress={async () => {
                if (eveluationFlowReducer && eveluationFlowReducer.selected_test.status != 'pending') {
                  Alert.alert('You cannot edit a completed test')
                  return;
                } else if (userReducer.userProfile.id != eveluationFlowReducer.instructor_info.id) { // id or instructor id evaulationred id  !=  id
                  Alert.alert('You are not instructor for this test')
                  // you are instructor
                  return;
                }
                this.setState({ saving: true })
                await this._vrtTab.saveVRT()
                this.setState({ saving: false })
              }}>
              {saving ? <Loader /> : <Image source={SAVE_ICON} style={{ height: 26, width: 26, marginHorizontal: 10 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                this.setState({ previewing: true })
                await this._vrtTab.saveVRT()
                await this._vrtTab.previewVRT()
                this.setState({ previewing: false })
              }}>
              {previewing ? <Loader /> : <Image source={PREVIEW_ICON} style={{ height: 25, width: 25, marginRight: 4 }} />}
            </TouchableOpacity>
          </View>
        )
      }
      case 'PAS': {
        return (
          <View style={{ flexDirection: 'row', justifyContent: 'center', alignItems: 'center' }}>
            <TouchableOpacity
              disabled={discarding}
              onPress={async () => {
                this.setState({ discarding: true })
                await this._pasTab.getData()
                this.setState({ discarding: false })
              }}>
              {discarding ? <Loader /> : <Image source={UNDO_ICON} style={{ height: 30, width: 30 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              disabled={saving}
              onPress={async () => {
                if (eveluationFlowReducer && eveluationFlowReducer.selected_test.status != 'pending') {
                  Alert.alert('You cannot edit a completed test')
                  return;
                } else if (userReducer.userProfile.id != eveluationFlowReducer.instructor_info.id) { // id or instructor id evaulationred id  !=  id
                  Alert.alert('You are not instructor for this test')
                  // you are instructor
                  return;
                }
                this.setState({ saving: true })
                await this._pasTab.savePAS()
                this.setState({ saving: false })
              }}>
              {saving ? <Loader /> : <Image source={SAVE_ICON} style={{ height: 26, width: 26, marginHorizontal: 10 }} />}
            </TouchableOpacity>
            <TouchableOpacity
              onPress={async () => {
                this.setState({ previewing: true })
                await this._pasTab.savePAS()
                await this._pasTab.previewPAS()
                this.setState({ previewing: false })
              }}>
              {previewing ? <Loader /> : <Image source={PREVIEW_ICON} style={{ height: 25, width: 25, marginRight: 4 }} />}
            </TouchableOpacity>
          </View>
        )
      }
      default:
        break;
    }
  }

  renderTabComponent = () => {
    const { selectedTab, EquipMounted, EyeMounted, NotesMounted, ProdMounted, PreTripMounted, BTWMounted, SWPMounted, VRTMounted, PASMounted } = this.state
    const { tabChangeErrorMessage, } = this.props
    // switch (selectedTab) {
    //   case 'Info': return <InfoTab />
    //   case 'Equip': return <EquipTab />
    //   case 'Eye': return <EyeTab />
    //   case 'Notes': return <NotesTab />
    //   case 'Prod': return <ProdTab />
    //   case 'PreTrip': return <PreTripTab />
    //   case 'BTW': return <BTWTab />
    //   case 'SWP': return <SWPTab />
    //   case 'VRT': return <VRTTab />
    //   case 'PAS': return <PASTab />
    //   default:
    //     break;
    // }
    return (
      <>
        <InfoTab ref={r => this._infoTab = r} shown={selectedTab == 'Info'} />
        {EquipMounted && <EquipTab ref={r => this._equipTab = r} shown={selectedTab == 'Equip'} />}

        {NotesMounted && <NotesTab ref={r => this._notesTab = r} shown={selectedTab == 'Notes'} />}
        {ProdMounted && <ProdTab ref={r => this._prodTab = r} shown={selectedTab == 'Prod'} />}
        {PreTripMounted && <PreTripTab ref={r => this._preTripTab = r} shown={selectedTab == 'PreTrip'} />}
        {BTWMounted && <BTWTab ref={r => this._btwTab = r} shown={selectedTab == 'BTW'} />}
        {SWPMounted && <SWPTab ref={r => this._swpTab = r} shown={selectedTab == 'SWP'} />}
        {VRTMounted && <VRTTab ref={r => this._vrtTab = r} shown={selectedTab == 'VRT'} />}
        {PASMounted && <PASTab ref={r => this._pasTab = r} shown={selectedTab == 'PAS'} />}
        {EyeMounted && <EyeTab ref={r => this._eyeTab = r} shown={selectedTab == 'Eye'} />}
      </>
    )
  }

  onChangeTab = (_tab) => {
    let tab = _tab;
    if (_tab == 'Pre Trip')
      tab = 'PreTrip'
    const { tabChangeErrorMessage, } = this.props
    if (tabChangeErrorMessage == false) {
      requestAnimationFrame(() => {
        if (this.state[`${tab}Mounted`]) {
          requestAnimationFrame(() => {
            this.setState({ selectedTab: tab })
          });
        } else {
          this.setState({
            [`${tab}Mounted`]: true
          }, () => {
            requestAnimationFrame(() => {
              this.setState({ selectedTab: tab })
            });
          })
        }
      })
    } else {
      alert(tabChangeErrorMessage)
    }
  }

  render() {
    const { selectedTab, accessableTabs, } = this.state
    const { tabChangeErrorMessage, } = this.props
    console.log("check tabs equal: ",  selectedTab, accessableTabs)
    return (
      <View style={{ flex: 1, justifyContent: 'space-between' }}>
        <Header>
          <Text onPress={() => NavigationService.navigate('HomeScreen')}>Home</Text>
          <>
            {IS_TAB ?
              <View horizontal style={{ flexDirection: 'row', flex: 1, marginHorizontal: 5 }}>
                {accessableTabs.map(tab => (
                  <TouchableWithoutFeedback
                    onPress={() => {
                      if (tabChangeErrorMessage == false) {
                        this.onChangeTab(tab)
                      } else {
                        alert(tabChangeErrorMessage)
                      }
                    }}>
                    <View style={{
                      flex: 1,
                      justifyContent: 'center',
                      alignItems: 'center',
                      marginRight: scale(5), borderWidth: 1, borderRadius: 5, borderColor: colors.APP_BORDER_GRAY_COLOR, padding: scale(5),
                      backgroundColor: selectedTab == tab ? 'white' : colors.APP_GRAY_COLOR
                    }}>
                      <Text style={{ fontSize: 12 }}>{tab}</Text>
                    </View>
                  </TouchableWithoutFeedback>
                ))}
              </View> :
              <TouchableWithoutFeedback onPress={() => {
                if (tabChangeErrorMessage == false) {
                  this._tabsActionSheet.show()
                } else {
                  alert(tabChangeErrorMessage)
                }
              }}>
                <View style={{ flex: 1, position: 'absolute', left: (SCREEN_WIDTH / 2) - scale(selectedTab.length * 2) - scale(8), bottom: 10 }}>
                  <Text style={{ alignSelf: 'center' }}>{selectedTab}</Text>
                </View>
              </TouchableWithoutFeedback>
            }
          </>
          {this.renderHeaderRight()}
        </Header>
        <ActionSheet
          ref={o => this._tabsActionSheet = o}
          title={'Options'}
          options={[...accessableTabs, 'Cancel']}
          cancelButtonIndex={10}
          // destructiveButtonIndex={10}
          onPress={(index) => {
            console.log('EvaluationScreen actionsheet index', index);
            if (index < accessableTabs.length) {
              this.onChangeTab(accessableTabs[index])
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
    )
  }
}

const mapStateToProps = state => {
  // console.log('state.eveluationFlowReducer EvaluationScreen: ', state.eveluationFlowReducer);
  return {
    userReducer: state.userReducer,
    tabChangeErrorMessage: state.eveluationFlowReducer.tabChangeErrorMessage,
    selectedTestInfo: state.eveluationFlowReducer.selectedTestInfo,
    student_info: state.eveluationFlowReducer.student_info,
    eveluationFlowReducer: state.eveluationFlowReducer
  };
};

export default connect(mapStateToProps, { fetchUserProfileAction, })(EvaluationScreen);
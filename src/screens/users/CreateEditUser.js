import React from 'react';
import { View, TextInput, Image, Modal, FlatList, RefreshControl, TouchableOpacity, ScrollView } from 'react-native';
import { connect } from 'react-redux';
import { Loader, Text, Header, Footer, Selector, UserField, DateTimePicker } from '../../components';
import { SEARCH_ICON, SCREEN_WIDTH, CALENDAR_ICON, RIGHT_ARROW_ICON, ALL_US_STATES } from '../../constants';
import SplashScreen from 'react-native-splash-screen'
import { fetchUserProfileAction, showSelector, showPopup, hidePopup, errorMessage } from '../../actions';
import { PLATFORM_IOS } from '../../constants';
import NavigationService from '../../navigation/NavigationService';
import { scale } from '../../utils/scale';
import * as colors from '../../styles/colors';
import { apiGet, apiPost, apiPut, showToast, apiPatch } from '../../utils/http';
import ActionSheet from 'react-native-actionsheet'
import ToggleSwitch from 'toggle-switch-react-native'
import moment from 'moment'
import _ from 'lodash'

class CreateEditUser extends React.Component {

  state = {
    selectedCompany: this.props.navigation.getParam('selectedCompany'),
    selectedUserType: this.props.navigation.getParam('selectedUserType'),
    selectedUser: this.props.navigation.getParam('selectedUser', null),
    loading: false,
    studentInfo: null,
    instructorInfo: null,
    //student props
    driver_license_class: null,
    company: this.props.navigation.getParam('selectedCompany').name,
    firstName: '',
    middleName: '',
    lastName: '',
    email: '',
    password: '',
    driver_license_num: '',
    driver_license_state: '',
    driver_license_expire_date: '',
    endorsements: false,
    corrective_lens_require: false,
    dot_expire_date: '',
    user_group: '',
    user_group_id: '',
    employee_id: '',
    // Show date picker props
    show_driver_license_expire_date: false,
    show_dot_expire_date: false,
  }

  async componentDidMount() {
    if (this.state.selectedUser) {
      await this.loadSelectedUserData();
      { this.state.studentInfo && this.studentDataPapulated() }
      { this.state.instructorInfo && this.instructorDataPapulated() }
    }
  }

  studentDataPapulated = () => {
    const { studentInfo } = this.state;
    this.setState({
      firstName: studentInfo?.first_name,
      middleName: studentInfo?.middle_name,
      lastName: studentInfo?.last_name,
      email: studentInfo?.email,
      password: '',
      driver_license_class: studentInfo?.info.driver_license_class,
      driver_license_num: studentInfo?.info.driver_license_number,
      driver_license_state: studentInfo?.info.driver_license_state,
      driver_license_expire_date: studentInfo?.info.driver_license_expire_date,
      endorsements: studentInfo?.info.endorsements,
      corrective_lens_require: studentInfo?.info.corrective_lense_required,
      dot_expire_date: studentInfo?.info.dot_expiration_date,
      user_group: studentInfo?.info?.group?.name,
      user_group_id: studentInfo?.info?.group?.id,
    })
  }

  instructorDataPapulated = () => {
    const { instructorInfo } = this.state;
    this.setState({
      firstName: instructorInfo.first_name,
      middleName: instructorInfo.middle_name,
      lastName: instructorInfo.last_name,
      email: instructorInfo.email,
      password: '',
      driver_license_class: instructorInfo.driver_license_class,
      driver_license_num: instructorInfo.driver_license_number,
      driver_license_state: instructorInfo.driver_license_state,
      driver_license_expire_date: instructorInfo.driver_license_expire_date,
      endorsements: instructorInfo.endorsements,
      corrective_lens_require: instructorInfo.corrective_lense_required,
      dot_expire_date: instructorInfo.dot_expiration_date,
      user_group: instructorInfo.user_group_name
    })
  }

  loadSelectedUserData = async () => {
    const { selectedCompany, selectedUserType, selectedUser } = this.state
    const studentEndpoint = `/api/v1/students/${selectedUser.id}/`
    // const instructorEndpoint = `/api/v1/students/${selectedUser.id}/info/`
    const instructorEndpoint = `/api/v1/users/${selectedUser.id}/`
    // const instructorEndpoint = `/api/v1/instructors/${selectedUser.id}/profile/`
    let endpoint = null;
    if (selectedCompany) {
      if (selectedUserType == 'Student') {
        endpoint = studentEndpoint
      } else {
        endpoint = instructorEndpoint
      }
      let res = await apiGet(endpoint)
      console.log(`loadSelectedUserData res for ${selectedUserType}:`, res.data)
      if (selectedUserType == "Instructor") {
        this.setState({ instructorInfo: res.data });
      } else {
        this.setState({ studentInfo: res.data });

      }
    }
  }

  validateData = () => {
    if (this.state.company == '') {
      showToast('Please enter your Company name.');
      return false;
    } else if (this.state.firstName == '') {
      showToast('Please enter your first name.');
      return false;
    } else if (this.state.lastName == '') {
      showToast('Please enter your last name.');
      return false;
    } else if (this.state.email == '') {
      showToast('Please enter your email.');
      return false;
    } else if (!!!this.state.selectedUser && this.state.password == '') {
      showToast('Please enter your password.');
      return false;
    }
    else if (this.state.user_group_id == '') {
      showToast('Please select a group.');
      return false;
    }
    return true;
  }

  saveButtonTapped = async () => {
    const selectedUser = this.props.navigation.getParam('selectedUser', null)
    if (this.state.selectedUserType == 'Student') {
      if (this.validateData()) {
        if (selectedUser) {
          console.log('edit user');
          this.editUser();
        } else {
          this.createUser();
          console.log('create user');
        }
      }
    } else {
      errorMessage('Please contact a system administrator to update instructor information')
    }
  }

  createUser = async () => {

    let endpoint = null;
    let msg = null;
    let data = null;

    if (this.state.selectedUserType == 'Student') {
      endpoint = '/api/v1/students/register/';
      msg = "Student created";
      data = {
        "first_name": this.state.firstName,
        "middle_name": this.state.middleName,
        "last_name": this.state.lastName,
        "email": this.state.email,
        "password": this.state.password,
        "send_gps_location": true,
        "groups": [
          // this.state.user_group_id
        ],

        "info": {
          "company": this.props.navigation.getParam('selectedCompany').id,
          "group": this.state.user_group_id,
          "driver_license_number": this.state.driver_license_num,
          "driver_license_state": this.state.driver_license_state,
          "driver_license_expire_date": this.state.driver_license_expire_date,
          "dot_expiration_date": this.state.dot_expire_date,
          "endorsements": this.state.endorsements,
          "driver_license_class": this.state.driver_license_class,
          "corrective_lense_required": this.state.corrective_lens_require
        }
      }
      if(this.state.user_group_id){
        data.groups= [
          this.state.user_group_id
        ]
      }
    } else {
      endpoint = `/api/v1/user/instructor/register/`
      msg = "Instructor created";
      data = {
        "first_name": this.state.firstName,
        "middle_name": this.state.middleName,
        "last_name": this.state.lastName,
        "email": this.state.email,
        "password": this.state.password,
        "send_gps_location": true,
        "groups": [
          // this.state.user_group_id
        ],

        "profile": {
          "company": this.props.navigation.getParam('selectedCompany').id,
          "driver_license_number": this.state.driver_license_num,
          "driver_license_state": this.state.driver_license_state,
          "driver_license_expire_date": this.state.driver_license_expire_date,
          "dot_expiration_date": this.state.dot_expire_date,
          "endorsements": this.state.endorsements,
          "driver_license_class": this.state.driver_license_class,
          "corrective_lense_required": this.state.corrective_lens_require
        }
      }
    }
    // console.log('student register data', data)
    // return
    let res = await apiPost(endpoint, data)
    console.log(`createUser res: `, res)
    if (res && res.data) {
      this.props.navigation.goBack()
      errorMessage(msg)
    } else if (res && res.error && res.error.data) {
      let errorString = ''
      _.forEach(res.error.data, (error, errorType) => {
        errorString += errorType + ' : ' + error
      })
      errorMessage(errorString)
    }
    // this.setState({ data: res.data.results })
  }

  editUser = async () => {

    let endpoint = null;
    let msg = null;
    let data = null;

    if (this.state.selectedUserType == 'Student') {
      endpoint = `/api/v1/students/${this.state.selectedUser.id}/`;
      msg = "Student updated";
      data = {
        "first_name": this.state.firstName,
        "middle_name": this.state.middleName,
        "last_name": this.state.lastName,
        "email": this.state.email,
        // "password": this.state.password,
        "send_gps_location": true,
        "groups": [
          this.state.user_group_id
        ],

        "info": {
          // "company": this.props.navigation.getParam('selectedCompany').id,
          'group':this.state.user_group_id,
          "driver_license_number": this.state.driver_license_num,
          "driver_license_state": this.state.driver_license_state,
          "driver_license_expire_date": this.state.driver_license_expire_date,
          "dot_expiration_date": this.state.dot_expire_date,
          "endorsements": this.state.endorsements,
          "driver_license_class": this.state.driver_license_class,
          "corrective_lense_required": this.state.corrective_lens_require
        }
      }
    } else {
      endpoint = `/api/v1/users/${this.state.selectedUser.id}/`
      msg = "Instructor updated";
      data = {
        // "username": this.state.firstName + this.state.lastName,
        "first_name": this.state.firstName,
        "middle_name": this.state.middleName,
        "last_name": this.state.lastName,
        "email": this.state.email,
        // "password": this.state.password,
        "send_gps_location": true,
        "groups": [
          // this.state.user_group_id
        ],
        //  "company": this.props.navigation.getParam('selectedCompany').id,
        //   "driver_license_number": this.state.driver_license_num,
        //   "driver_license_state": this.state.driver_license_state,
        //   "driver_license_expire_date": "2020-09-19",
        //   "dot_expiration_date": "2020-09-30",
        //   "endorsements": this.state.endorsements,
        //   "driver_license_class": this.state.driver_license_class,
        //   "corrective_lense_required": this.state.corrective_lens_require
        "info": {
          "company": this.props.navigation.getParam('selectedCompany').id,
          "driver_license_number": this.state.driver_license_num,
          "driver_license_state": this.state.driver_license_state,
          "driver_license_expire_date": this.state.driver_license_expire_date,
          "dot_expiration_date": this.state.dot_expire_date,
          "endorsements": this.state.endorsements,
          "driver_license_class": this.state.driver_license_class,
          "corrective_lense_required": this.state.corrective_lens_require
        }
      }
    }

    let res = await apiPatch(endpoint, data, true)
    console.log(`UserInfo update res: `, res)
    if (res && res.data) {
      this.props.navigation.goBack()
      errorMessage(msg)
    } else if (res && res.error && res.error.data) {
      let errorString = ''
      _.forEach(res.error.data, (error, errorType) => {
        errorString += errorType + ' : ' + error
      })
      errorMessage(errorString)
    }
  }

  render() {
    const {
      company,
      firstName, lastName,
      middleName, email,
      password,
      driver_license_class,
      driver_license_num,
      driver_license_state,
      driver_license_expire_date,
      endorsements,
      corrective_lens_require,
      dot_expire_date,
      user_group,
      selectedUserType,
      selectedCompany,
      loading } = this.state
    //student data
    // const { driver_license_class, driver_license_expire_date, endorsements, corrective_lens_require, dot_expire_date, user_group, company, driver_license_state } = this.state
    return (
      <View style={{ flex: 1, justifyContent: 'space-between', backgroundColor: colors.FONT_WHITE_COLOR }}>
        {/* Header */}
        <Header>
          <Text onPress={() => NavigationService.goBack()}>Cancel</Text>
          <Text>{selectedUserType}</Text>
          <Text onPress={() => this.saveButtonTapped()}>     Save</Text>
        </Header>

        <ScrollView style={{ flex: 1 }}>
          <UserField
            required
            disabled
            title={'Company'}
            onChangeText={company => this.setState({ company })}
            value={company}
          />
          <UserField
            required
            title={'First Name'}
            onChangeText={firstName => this.setState({ firstName })}
            value={firstName}
          />
          <UserField
            // required
            title={'Middle Name'}
            onChangeText={middleName => this.setState({ middleName })}
            value={middleName}
          />
          <UserField
            required
            title={'Last Name'}
            onChangeText={lastName => this.setState({ lastName })}
            value={lastName}
          />
          <UserField
            required
            title={'Email'}
            onChangeText={email => this.setState({ email })}
            value={email}
          />
          {!!!this.state.selectedUser && <UserField
            required
            title={'Password'}
            onChangeText={password => this.setState({ password })}
            value={password}
            autoCapitalize={'none'}
          />}
          <UserField
            // required
            title={'Class'}
            onPress={() => showSelector(<Selector
              title={'Class'}
              data={[
                { id: 1, name: 'A' },
                { id: 2, name: 'B' },
                { id: 3, name: 'C' },
              ]}
              onSelect={(item) => this.setState({ driver_license_class: item.name })}
            />)}
            component={
              <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                <Text>{driver_license_class}</Text>
                <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} />
              </View>
            }
          />
          <UserField
            // required
            title={'Driver license Number'}
            onChangeText={driver_license_num => this.setState({ driver_license_num })}
            value={driver_license_num}
          />
          <UserField
            // required
            title={'Driver license State'}
            onPress={() => showSelector(<Selector
              title={'State'}
              data={ALL_US_STATES}
              onSelect={(item) => this.setState({ driver_license_state: item.name })}
            />)}
            component={
              <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                <Text>{driver_license_state}</Text>
                <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} />
              </View>
            }
          />
          <UserField
            // required
            title={'Driver license Expiration Date'}
            // onPress={() => this.setState({ show_driver_license_expire_date: true })}
            onPress={() => {
              showPopup(
                <DateTimePicker
                  onConfirm={(date) => {
                    console.log('date driver_license_expire_date', date);
                    this.setState({ driver_license_expire_date: date })
                  }}
                />
              )
            }}
            rightArrow
            component={
              <View style={{ flexDirection: 'row', alignItems: 'center' }}>
                <Image source={CALENDAR_ICON} style={{ height: scale(34), width: scale(34) }} />
                <Text>{driver_license_expire_date}</Text>
              </View>
            }
          />

          <UserField
            // required
            title={'Endorsements'}
            component={
              <View style={{ flexDirection: 'row', justifyContent: 'flex-end', flex: 1 }}>
                <ToggleSwitch
                  isOn={endorsements}
                  onColor="rgb(61,197,94)"
                  offColor="rgb(233,233,235)"
                  onToggle={isOn => this.setState({ endorsements: isOn })}
                />
              </View>
            }
          />
          <UserField
            // required
            title={'Corrective Lens Required'}
            component={
              <View style={{ flexDirection: 'row', justifyContent: 'flex-end', flex: 1 }}>
                <ToggleSwitch
                  isOn={corrective_lens_require}
                  onColor="rgb(61,197,94)"
                  offColor="rgb(233,233,235)"
                  onToggle={isOn => this.setState({ corrective_lens_require: isOn })}
                />
              </View>
            }
          />
          <UserField
            // required
            rightArrow
            title={'DOT Expiration Date'}
            onPress={() => {
              showPopup(
                <DateTimePicker
                  onConfirm={(date) => {
                    console.log('date dot_expire_date', date);
                    this.setState({ dot_expire_date: date })
                  }}
                />
              )
            }}
            component={
              <View style={{ flexDirection: 'row', alignItems: 'center' }}>
                <Image source={CALENDAR_ICON} style={{ height: scale(34), width: scale(34) }} />
                <Text>{dot_expire_date}</Text>
              </View>
            }
          />
          <UserField
            required
            title={'User Group'}
            onPress={() => showSelector(<Selector
              title={'Groups'}
              // data={[
              //   { id: 1, name: 'A' },
              //   { id: 2, name: 'B' },
              //   { id: 3, name: 'C' },
              // ]}
              endpoint={'/api/v1/student-groups/'}
              // onSelect={(item) => console.log('item', item)}
              onSelect={(item) => this.setState({ user_group: item.name, user_group_id: item.id })}
            />)}
            component={
              <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                <Text>{user_group}</Text>
                {/* <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} /> */}
              </View>
            }
          />
        </ScrollView>

        {/* Footer */}
        <Footer>
          <Text
            numberOfLines={1}
            style={{ width: (SCREEN_WIDTH / 3) - 10 }}
            onPress={() => {
              // showSelector(
              //   <Selector
              //     title={'Companies'}
              //     endpoint={'/api/v1/companies/'}
              //     onSelect={(item) => this.setState({ selectedCompany: item }, this.loadCompanyData)}
              //   />
              // )
            }} >
            Info
          </Text>
          {/* <Text style={{ textAlign: 'center', width: (SCREEN_WIDTH / 3) - scale(50), marginLeft: -15 }} onPress={() => this._userTypeActionSheet.show()}>UserType</Text> */}
          <Text style={{ textAlign: 'right', width: (SCREEN_WIDTH / 3) - 10 }}>Delete</Text>
        </Footer>

      </View>
    )
  }
}

const mapStateToProps = state => {
  return {
    userReducer: state.userReducer,
  };
};

export default connect(mapStateToProps, { fetchUserProfileAction, })(CreateEditUser);


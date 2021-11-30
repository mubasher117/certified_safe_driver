import React from 'react';
import { StatusBar, Image, Text, View, ScrollView, TouchableOpacity, Alert } from 'react-native';
import { connect } from 'react-redux';
import { EvaluationField, Loader, ScreenWrapper, Selector, Footer } from '../../components';
import SplashScreen from 'react-native-splash-screen'
import { fetchUserProfileAction, showSelector } from '../../actions';
import { RIGHT_ARROW_ICON, INFO_ICON, BACKWARD_ICON, FORWARD_ICON, PLUS_ICON } from '../../constants';
import * as colors from '../../styles/colors';
import { scale } from '../../utils/scale';
import { apiPut, apiGet, apiPatch, apiPost } from '../../utils/http';
import { updateCompanyInfo, updateStudentInfo } from '../../actions'
import FooterBtns from '../../components/FooterBtns';
import { UPDATE_SELECTED_TEST } from '../../actions/types';

class EquipTab extends React.Component {

  state = {
    start_time: true,
    end_time: false,
    type: false,
    studentEquipInfo: [],
    selectedEquipIndex: 0,
    selectedEquipId: null,
    date: '',
    power_unit_number: '',
    transmission_type: '',
    transmission_type_other: '',
    vehicle_type: '',
    vehicle_type_other: '',
    vehicle_manufacturer: '',
    vehicle_manufacturer_other: '',
    single_trailer_length: '',
    single_trailer_length_other: '',
    combination_vehicles: '',
    combinations_vehicles_other: '',
    combination_vehicles_length: '',
    combination_vehicles_length_other: '',
    dolly_or_gear_type: '',
    dolly_or_gear_type_other: '',
    trailer_1: '',
    trailer_2: '',
    trailer_3: '',
    dolly_1: '',
    dolly_2: ''
  }

  async componentDidMount() {
    if (this.props.eveluationFlowReducer.student_info) {
      this.getEquipInfo();
    }
  }

  FieldClears = () => {
    this.setState({
      selectedEquipId: null,
      power_unit_number: "",
      transmission_type: "",
      transmission_type_other: "",
      vehicle_type: "",
      vehicle_type_other: "",
      vehicle_manufacturer: "",
      vehicle_manufacturer_other: "",
      single_trailer_length: "",
      single_trailer_length_other: "",
      combination_vehicles: "",
      combinations_vehicles_other: "",
      combination_vehicles_length: "",
      combination_vehicles_length_other: "",
      dolly_or_gear_type: "",
      dolly_or_gear_type_other: "",
      trailer_1: "",
      trailer_2: "",
      trailer_3: "",
      dolly_1: "",
      dolly_2: "",

      transmisionType: "",
      transmisionTypeNotes: "",
      vehicleType: "",
      vehicleTypeNotes: "",
      vehicleManufacturer: "",
      vehicleManufacturerNotes: "",
      singleTrailerLength: "",
      singleTrailerLengthNotes: "",
      combinationVehicles: "",
      combinationVehiclesNotes: "",
      combinationVehiclesLength: "",
      combinationVehiclesLengthNotes: "",
      dollyGearType: "",
      dollyGearTypeNotes: ""
    });
  }

  PopulateData = (item) => {
    console.log('item', item)
    this.setState({
      power_unit_number: item.power_unit_number,
      transmission_type: item.transmission_type,
      // transmission_type_other: item.,
      vehicle_type: item.vehicle_type,
      vehicle_type_other: item.vehicle_type_other,
      vehicle_manufacturer: item.vehicle_manufacturer,
      vehicle_manufacturer_other: item.vehicle_manufacturer_other,
      single_trailer_length: item.single_trailer_length,
      single_trailer_length_other: item.single_trailer_length_other,
      combination_vehicles: item.combination_vehicles,
      combinations_vehicles_other: item.combinations_vehicles_other,
      combination_vehicles_length: item.combination_vehicles_length,
      combination_vehicles_length_other: item.combination_vehicles_length_other,
      dolly_or_gear_type: item.dolly_or_gear_type,
      dolly_or_gear_type_other: item.dolly_or_gear_type_other,
      trailer_1: item.trailer_1,
      trailer_2: item.trailer_2,
      trailer_3: item.trailer_3,
      dolly_1: item.dolly_1,
      dolly_2: item.dolly_2,
      selectedEquipId: item.id
    });
  }

  getEquipInfo = async () => {
    const { company_info, student_info, selected_test } = this.props.eveluationFlowReducer
    let res = await apiGet(`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/equips/`)
    console.log(`getEquipInfo res: `, res);
    if (res && res.data && res.data.length) {
      res.data.reverse()
      this.setState({ studentEquipInfo: res.data });
      this.PopulateData(res.data[res.data.length - 1]);
      // this.props.navigation.goBack()
      // errorMessage('Student Info Fetch')
    }
    return true
  }

  saveEquip = async () => {
    const { company_info, student_info, selected_test } = this.props.eveluationFlowReducer
    let data = {
      "power_unit_number": this.state.power_unit_number,
      "transmission_type": this.state.transmission_type,
      "vehicle_type": this.state.vehicle_type,
      "vehicle_type_other": this.state.vehicle_type_other,
      "vehicle_manufacturer": this.state.vehicle_manufacturer,
      "vehicle_manufacturer_other": this.state.vehicle_manufacturer_other,
      "single_trailer_length": this.state.single_trailer_length,
      "single_trailer_length_other": this.state.single_trailer_length_other,
      "combination_vehicles": this.state.combination_vehicles,
      "combinations_vehicles_other": this.state.combinations_vehicles_other,
      "combination_vehicles_length": this.state.combination_vehicles_length,
      "combination_vehicles_length_other": this.state.combination_vehicles_length_other,
      "dolly_or_gear_type": this.state.dolly_or_gear_type,
      "dolly_or_gear_type_other": this.state.dolly_or_gear_type_other,
      "trailer_1": this.state.trailer_1,
      "trailer_2": this.state.trailer_2,
      "trailer_3": this.state.trailer_3,
      "dolly_1": this.state.dolly_1,
      "dolly_2": this.state.dolly_2
    }

    let res = null
    if (this.state.selectedEquipId) {
      //create equip POST
      res = await apiPatch(`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/equips/${this.state.selectedEquipId}`, data, true);
    } else {
      //EDIT equip with id PATCH
      res = await apiPost(`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/equips/`, data, true);
      console.log(`createEquip res: `, res);
    }
    
    if (res && res.data) {
      this.getEquipInfo();
      // this.props.navigation.goBack()
      // errorMessage('Student Equip Updated')
    }
    return true;
  }

  render() {

    const {
      studentEquipInfo,
      selectedEquipIndex,

      power_unit_number,
      transmission_type,
      transmission_type_other,
      vehicle_type,
      vehicle_type_other,
      vehicle_manufacturer,
      vehicle_manufacturer_other,
      single_trailer_length,
      single_trailer_length_other,
      combination_vehicles,
      combinations_vehicles_other,
      combination_vehicles_length,
      combination_vehicles_length_other,
      dolly_or_gear_type,
      dolly_or_gear_type_other,
      trailer_1,
      trailer_2,
      trailer_3,
      dolly_1,
      dolly_2,

      transmisionType,
      transmisionTypeNotes,
      vehicleType,
      vehicleTypeNotes,
      vehicleManufacturer,
      vehicleManufacturerNotes,
      singleTrailerLength,
      singleTrailerLengthNotes,
      combinationVehicles,
      combinationVehiclesNotes,
      combinationVehiclesLength,
      combinationVehiclesLengthNotes,
      dollyGearType,
      dollyGearTypeNotes
    } = this.state;
    const { company_info, student_info, instructor_info } = this.props.eveluationFlowReducer;
    const show = { flex: 1, height: undefined }
    const hide = { flex: 0, height: 0 }
    return (
      <>
        <ScreenWrapper parentStyle={this.props.shown ? show : hide}>
          <ScrollView style={{ flex: 1 }}>

            <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
              // required
              disabled
              backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
              title={'Company'}
              component={
                <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                  <Text>{company_info && company_info?.name}</Text>
                  {/* <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} /> */}
                </View>
              }
            />

            <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
              // required
              disabled
              backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
              title={'Instructor'}
              component={
                <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                  <Text>{instructor_info && `${instructor_info.first_name} ${instructor_info.last_name}`}</Text>
                  {/* <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} /> */}
                </View>
              }
            />

            <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
              disabled
              // required
              backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
              title={'Student'}
              component={
                <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                  <Text>{student_info && `${student_info?.first_name} ${student_info?.last_name}`}</Text>
                  {/* <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} /> */}
                </View>
              }
            />

            {!this.state.type ? <>
              <View style={{ backgroundColor: 'yellow' }}>
                <Text style={{ marginHorizontal: 10, marginVertical: 5, fontSize: 14 }}>{`Power Unit`}</Text>
              </View>

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                required
                title={'Power Unit Number'}
                // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                onChangeText={power_unit_number => this.setState({ power_unit_number })}
                value={power_unit_number}
              />

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                // required
                title={'Transmission Type'}
                onPress={() => {
                  showSelector(<Selector
                    title={'Transmission Type'}
                    data={[
                      { id: 1, name: 'Automatic' },
                      { id: 2, name: 'Manual' },
                      { id: 3, name: 'Other' },
                    ]}
                    onSelect={(transmission_type) => this.setState({ transmission_type: transmission_type.name })}
                  />)
                }}
                component={
                  <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                    <Text>{transmission_type}</Text>
                    <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} />
                  </View>
                }
              />

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                //required
                title={'Transmission Type Other'}
                // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                onChangeText={transmission_type_other => this.setState({ transmission_type_other })}
                value={transmission_type_other}
              />

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                // required
                title={'Vehicle Type'}
                onPress={() => {
                  showSelector(<Selector
                    title={'Vehicle Type'}
                    data={[
                      { id: 1, name: 'Pick-up Truck' },
                      { id: 2, name: 'Cargo Van' },
                      { id: 3, name: 'Passenger Van' },
                      { id: 4, name: 'Utility Truck' },
                      { id: 5, name: 'Passenger Bus' },
                      { id: 6, name: 'Stright Truck' },
                      { id: 8, name: 'Tractor (Day Cab)' },
                      { id: 9, name: 'Tractor Sleeper' },
                      { id: 10, name: 'Yard shifter' },
                      { id: 11, name: 'Other' },
                    ]}
                    onSelect={(vehicle_type) => this.setState({ vehicle_type: vehicle_type.name })}
                  />)
                }}
                component={
                  <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                    <Text>{vehicle_type}</Text>
                    <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} />
                  </View>
                }
              />

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                //required
                title={'Vehicle Type Other'}
                // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                onChangeText={vehicle_type_other => this.setState({ vehicle_type_other })}
                value={vehicle_type_other}
              />

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                // required
                title={'Vehicle Manufacturer'}
                onPress={() => {
                  showSelector(<Selector
                    title={'Vehicle Manufacturer'}
                    data={[
                      { id: 1, name: 'Freightliner' },
                      { id: 2, name: 'International' },
                      { id: 3, name: 'Mack' },
                      { id: 4, name: 'Ottowa' },
                      { id: 5, name: 'Sterling' },
                      { id: 6, name: 'Other' },
                    ]}
                    onSelect={(vehicle_manufacturer) => this.setState({ vehicle_manufacturer: vehicle_manufacturer.name })}
                  />)
                }}
                component={
                  <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                    <Text>{vehicle_manufacturer}</Text>
                    <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} />
                  </View>
                }
              />

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                //required
                title={'Vehicle Manufacturer Other'}
                // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                onChangeText={vehicle_manufacturer_other => this.setState({ vehicle_manufacturer_other })}
                value={vehicle_manufacturer_other}
              />

              <View style={{ backgroundColor: 'yellow' }}>
                <Text style={{ marginHorizontal: 10, marginVertical: 5, fontSize: 14 }}>{`Combination Vehicle - Train or Chain`}</Text>
              </View>

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                // required
                title={'Single Trailer Length'}
                onPress={() => {
                  showSelector(<Selector
                    title={'Single Trailer Length'}
                    data={[
                      { id: 1, name: '28' },
                      { id: 2, name: '40' },
                      { id: 3, name: '45' },
                      { id: 4, name: '48' },
                      { id: 5, name: '53' },
                      { id: 6, name: 'Other' },
                    ]}
                    onSelect={(single_trailer_length) => this.setState({ single_trailer_length: single_trailer_length.name })}
                  />)
                }}
                component={
                  <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                    <Text>{single_trailer_length}</Text>
                    <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} />
                  </View>
                }
              />

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                //required
                title={'Single Trailer Length Other'}
                // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                onChangeText={single_trailer_length_other => this.setState({ single_trailer_length_other })}
                value={single_trailer_length_other}
              />

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                // required
                title={'Combination Vehicles'}
                onPress={() => {
                  showSelector(<Selector
                    title={'Combination Vehicles'}
                    data={[
                      { id: 1, name: 'Doubles' },
                      { id: 2, name: 'Thriples' },
                      { id: 3, name: 'Rockey Mountain' },
                      { id: 4, name: 'Other' },
                    ]}
                    onSelect={(combination_vehicles) => this.setState({ combination_vehicles: combination_vehicles.name })}
                  />)
                }}
                component={
                  <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                    <Text>{combination_vehicles}</Text>
                    <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} />
                  </View>
                }
              />

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                //required
                title={'Combination Vehicles Other'}
                // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                onChangeText={combinations_vehicles_other => this.setState({ combinations_vehicles_other })}
                value={combinations_vehicles_other}
              />

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                // required
                title={'Combination Vehicles Length'}
                onPress={() => {
                  showSelector(<Selector
                    title={'Combination Vehicles Length'}
                    data={[
                      { id: 1, name: '28' },
                      { id: 2, name: '40' },
                      { id: 3, name: '45' },
                      { id: 4, name: 'Other' },
                    ]}
                    onSelect={(combination_vehicles_length) => this.setState({ combination_vehicles_length: combination_vehicles_length.name })}
                  />)
                }}
                component={
                  <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                    <Text>{combination_vehicles_length}</Text>
                    <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} />
                  </View>
                }
              />

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                //required
                title={'Combination Vehicles Length Other'}
                // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                onChangeText={combination_vehicles_length_other => this.setState({ combination_vehicles_length_other })}
                value={combination_vehicles_length_other}
              />

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                // required
                title={'Dholly/Gear Type'}
                onPress={() => {
                  showSelector(<Selector
                    title={'Dholly/Gear Type'}
                    data={[
                      { id: 1, name: 'Converter' },
                      { id: 2, name: 'Low-Loader' },
                      { id: 3, name: 'Expending/Contracting' },
                      { id: 4, name: 'Other' }, 
                    ]}
                    onSelect={(dolly_or_gear_type) => this.setState({ dolly_or_gear_type: dolly_or_gear_type.name })}
                  />)
                }}
                component={
                  <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                    <Text>{dolly_or_gear_type}</Text>
                    <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} />
                  </View>
                }
              />

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                //required
                title={'Dholly/Gear Type Other'}
                // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                onChangeText={dolly_or_gear_type_other => this.setState({ dolly_or_gear_type_other })}
                value={dolly_or_gear_type_other}
              />

              <View style={{ backgroundColor: 'yellow' }}>
                <Text style={{ marginHorizontal: 10, marginVertical: 5, fontSize: 14 }}>{`Vehicle Numbers`}</Text>
              </View>

              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                //required
                title={'Trailer 1'}
                // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                onChangeText={trailer_1 => this.setState({ trailer_1 })}
                value={trailer_1}
              />
              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                //required
                title={'Dholly 1'}
                // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                onChangeText={dolly_1 => this.setState({ dolly_1 })}
                value={dolly_1}
              />
              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                //required
                title={'Trailer 2'}
                // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                onChangeText={trailer_2 => this.setState({ trailer_2 })}
                value={trailer_2}
              />
              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                //required
                title={'Dholly 2'}
                // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                onChangeText={dolly_2 => this.setState({ dolly_2 })}
                value={dolly_2}
              />
              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                //required
                title={'Trailer 3'}
                // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                onChangeText={trailer_3 => this.setState({ trailer_3 })}
                value={trailer_3}
              />
            </> :
              <>
                <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                  //required
                  title={'Transmission Type'}
                  // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                  onChangeText={transmisionType => this.setState({ transmisionType })}
                  value={transmisionType}
                />
                <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                  //required
                  title={'Notes'}
                  // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                  onChangeText={transmisionTypeNotes => this.setState({ transmisionTypeNotes })}
                  value={transmisionTypeNotes}
                />
                <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                  //required
                  title={'Vehicle Type'}
                  // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                  onChangeText={vehicleType => this.setState({ vehicleType })}
                  value={vehicleType}
                />
                <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                  //required
                  title={'Notes'}
                  // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                  onChangeText={vehicleTypeNotes => this.setState({ vehicleTypeNotes })}
                  value={vehicleTypeNotes}
                />
                <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                  //required
                  title={'Vehicle Manufacturer'}
                  // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                  onChangeText={vehicleManufacturer => this.setState({ vehicleManufacturer })}
                  value={vehicleManufacturer}
                />
                <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                  //required
                  title={'Notes'}
                  // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                  onChangeText={vehicleManufacturerNotes => this.setState({ vehicleManufacturerNotes })}
                  value={vehicleManufacturerNotes}
                />
                <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                  //required
                  title={'Single trailer Length'}
                  // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                  onChangeText={singleTrailerLength => this.setState({ singleTrailerLength })}
                  value={singleTrailerLength}
                />
                <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                  //required
                  title={'Notes'}
                  // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                  onChangeText={singleTrailerLengthNotes => this.setState({ singleTrailerLengthNotes })}
                  value={singleTrailerLengthNotes}
                />
                <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                  //required
                  title={'Combination Vehicles'}
                  // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                  onChangeText={combinationVehicles => this.setState({ combinationVehicles })}
                  value={combinationVehicles}
                />
                <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                  //required
                  title={'Notes'}
                  // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                  onChangeText={combinationVehiclesNotes => this.setState({ combinationVehiclesNotes })}
                  value={combinationVehiclesNotes}
                />
                <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                  //required
                  title={'Combination Vehicles Length'}
                  // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                  onChangeText={combinationVehiclesLength => this.setState({ combinationVehiclesLength })}
                  value={combinationVehiclesLength}
                />
                <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                  //required
                  title={'Notes'}
                  // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                  onChangeText={combinationVehiclesLengthNotes => this.setState({ combinationVehiclesLengthNotes })}
                  value={combinationVehiclesLengthNotes}
                />
                <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                  //required
                  title={'Dholly Gear Type'}
                  // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                  onChangeText={dollyGearType => this.setState({ dollyGearType })}
                  value={dollyGearType}
                />
                <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                  //required
                  title={'Notes'}
                  // backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
                  onChangeText={dollyGearTypeNotes => this.setState({ dollyGearTypeNotes })}
                  value={dollyGearTypeNotes}
                />
              </>
            }
          </ScrollView>
        </ScreenWrapper>
        {
          this.props.shown && <Footer>

            {/* <FooterBtns onChange={(type) => this.setState({ type })} initialValue={this.state.type} /> */}

            <TouchableOpacity
              disabled={studentEquipInfo.length < 2 || selectedEquipIndex == 0}
              onPress={() => {
                this.setState({
                  selectedEquipIndex: this.state.selectedEquipIndex - 1
                }, () => {
                  this.PopulateData(studentEquipInfo[selectedEquipIndex])
                })
              }}
            >
              <Image source={BACKWARD_ICON} style={{ resizeMode: 'contain', height: 25, width: 25 }} />
            </TouchableOpacity>

            <TouchableOpacity>
              <Text style={{}}>{selectedEquipIndex + (studentEquipInfo.length ? 1 : 0)}/{studentEquipInfo.length}</Text>
            </TouchableOpacity>

            <TouchableOpacity
              disabled={studentEquipInfo.length < 2 || selectedEquipIndex >= studentEquipInfo.length - 1}
              onPress={() => {
                this.setState({
                  selectedEquipIndex: this.state.selectedEquipIndex + 1
                }, () => {
                  this.PopulateData(studentEquipInfo[selectedEquipIndex])
                })
              }}
            >
              <Image source={FORWARD_ICON} style={{ resizeMode: 'contain', height: 20, width: 20 }} />
            </TouchableOpacity>

            <TouchableOpacity onPress={() => Alert.alert('Notification', `1. To add a new Equipment please tap on the Add button from bottom toolbar. \n \n 2. To navigate through Equipments please use '<<' and '>>' buttons`)}>
              <Image source={INFO_ICON} style={{ resizeMode: 'contain', height: 20, width: 20, paddingLeft: 10 }} />
            </TouchableOpacity>

            <TouchableOpacity
              onPress={() => Alert.alert(
                'Add new Equipment?',
                `Fill data for new equipment and save`,
                [
                  {
                    text: 'No',
                    onPress: () => {

                    },
                    style: 'no',
                  },
                  {
                    text: 'Yes',
                    onPress: () => {
                      this.FieldClears();
                      this.setState({ selectedEquipIndex: studentEquipInfo.length })
                    }
                  },
                ],
                { cancelable: false },
              )}>
              <Image source={PLUS_ICON} style={{ resizeMode: 'contain', height: 20, width: 20, paddingRight: 10 }} />
            </TouchableOpacity>
          </Footer>
        }
      </>
    )
  }
}

const mapStateToProps = state => {
  return {
    userReducer: state.userReducer,
    eveluationFlowReducer: state.eveluationFlowReducer,
  };
};

export default connect(mapStateToProps, { fetchUserProfileAction, updateCompanyInfo, updateStudentInfo }, null, { forwardRef: true })(EquipTab);
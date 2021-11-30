import React from 'react';
import { View, Image, TouchableOpacity, StyleSheet, PixelRatio, PermissionsAndroid } from 'react-native';
import { connect } from 'react-redux';
import { Loader, ScreenWrapper, Header, Text, Footer } from '../../components';
import SplashScreen from 'react-native-splash-screen'
import { setMapData } from '../../actions';
import { PLATFORM_IOS, IS_TAB, SCREEN_WIDTH } from '../../constants';
import MapView, { Marker, PROVIDER_GOOGLE } from 'react-native-maps';
import NavigationService from '../../navigation/NavigationService';
import Geolocation from 'react-native-geolocation-service';
import { scale } from '../../utils/scale';
import ViewShot from "react-native-view-shot";
import AsyncStorage from '@react-native-community/async-storage';


const LEFT_WIDE_IMG = require('../../assets/icons/left-wide.png')
const LEFT_OK_IMG = require('../../assets/icons/left-ok.png')
const LEFT_SHORT_IMG = require('../../assets/icons/left-short.png')
const RIGHT_WIDE_IMG = require('../../assets/icons/right-wide.png')
const RIGHT_OK_IMG = require('../../assets/icons/right-ok.png')
const RIGHT_SHORT_IMG = require('../../assets/icons/right-short.png')
// const USER_LOCATION_IMAGE=
let locationWatcher = null;

const INITIAL_REGION = {
  latitude: 36.1986623,
  longitude: -113.7990099,
  latitudeDelta: 0.0143,
  longitudeDelta: 0.0134,
}
const Camera = {
  center: {
    latitude: 36.1986623,
    longitude: -113.7990099,
  },
  pitch: 1,
  heading: 1,
  // Only when using Google Maps.
  zoom: 4
}
const MapButton = ({ title, onPress }) =>
  <TouchableOpacity
    style={{ padding: IS_TAB ? scale(8) : scale(3), marginRight: IS_TAB ? 5 : 1, borderRadius: 50, borderWidth: 0.5, borderColor: 'black' }}
    onPress={onPress}>
    <Text style={{ fontSize: IS_TAB ? scale(16) : scale(8) }} >{title}</Text>
  </TouchableOpacity>

class MapScreen extends React.Component {
  state = {
    leftWides: [],
    leftOks: [],
    leftShorts: [],
    rightWides: [],
    rightOks: [],
    rightShorts: [],
    userLocation: null,
    focusUserLocation: true,
    map_screenshot_url: ''
  }
  async componentDidMount() {
    if (Platform.OS === 'android') {
      await this.requestLocationPermission();
    } else {
      await Geolocation.requestAuthorization("always")
    }
    if (this.props.eveluationFlowReducer.mapData) {
      this.setState({ ...this.state, ...this.props.eveluationFlowReducer.mapData }, () => {
        // console.log('mounted state', this.state)
        // this.refMapView.fitToElements(false);
      })
    }
    setTimeout(() => {
      this.getAndUpdateLocation()
    }, 750);
    setTimeout(() => {
      this.refMapView.fitToElements(false);
    }, 2000);
    this.watchDriverLocation()
  }

  componentWillUnmount() {
    clearInterval(locationWatcher)
  }

  requestLocationPermission = async () => {
    try {
      const granted = await PermissionsAndroid.request(
        PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION,
        {
          title: 'Location Permission',
          message: 'HooleyHopper App needs access to your GPS',
        },
      );
      if (granted === PermissionsAndroid.RESULTS.GRANTED) {
        console.log('You can use the GPS');
      } else {
        console.log('GPS permission denied');
      }
    } catch (err) {
      console.warn(err);
    }
  };

  watchDriverLocation = () => {
    clearInterval(locationWatcher);
    locationWatcher = setInterval(() => {
      this.getAndUpdateLocation();
    }, 10 * 1000);
  }

  getAndUpdateLocation = async () => {
    return await Geolocation.getCurrentPosition(async ({ coords: { latitude, longitude } }) => {
      // success
      // console.warn('3')

      console.log('got COORDS latitude', latitude, ' longitude', longitude)
      this.setState({
        userLocation: {
          latitude,
          longitude,
          latitudeDelta: 0.0143,
          longitudeDelta: 0.0134,
        }
      })
    },
      error => {
        // error
        console.log('Error -->', error);
        clearInterval(locationWatcher);
        // Alert.alert('count not get location', JSON.stringify(error))
      },
      {
        timeout: 9000,
        enableHighAccuracy: false,// (Platform.OS === 'android' ? false : true),
        maximumAge: 9000,
        distanceFilter: 100
      })
  }

  processClick = async (key) => {
    console.log('processClick key', key)
    const { leftWides, leftOks, leftShorts, rightWides, rightOks, rightShorts } = this.state
    if (__DEV__ && key == 'leftOks') {
      await this.setState({ [key]: [...this.state[key], { latitude: this.state.userLocation.latitude + 0.01, longitude: this.state.userLocation.longitude }] })
      // return
    }
    if (__DEV__ && key == 'leftShorts') {
      await this.setState({ [key]: [...this.state[key], { latitude: this.state.userLocation.latitude, longitude: this.state.userLocation.longitude + 0.01 }] })
      // return
    }
    if (__DEV__ && key == 'leftWides') {
      await this.setState({ [key]: [...this.state[key], { latitude: this.state.userLocation.latitude, longitude: this.state.userLocation.longitude - 0.01 }] })
      // return
    }
    if (__DEV__ && key == 'rightWides') {
      await this.setState({ [key]: [...this.state[key], { latitude: this.state.userLocation.latitude-0.01, longitude: this.state.userLocation.longitude - 0.01 }] })
      // return
    }
    this.setState({ focusUserLocation: false, [key]: [...this.state[key], { ...this.state.userLocation }] }, async () => {
      await this.refMapView.fitToElements(false);
      setTimeout(() => {
        this.takeSnapshot()
      }, 1000);
    })
  }

  takeSnapshot = async () => {
    // 'takeSnapshot' takes a config object with the
    // following options
    try {
      console.warn('wid:', PixelRatio.getPixelSizeForLayoutSize(SCREEN_WIDTH), 'rat', PixelRatio.get())
      const uri = await this.refMapView.takeSnapshot({
        width: 750,// PixelRatio.getPixelSizeForLayoutSize(SCREEN_WIDTH),      // optional, when omitted the view-width is used
        height: 750,     // optional, when omitted the view-height is used
        // region: {..},    // iOS only, optional region to render
        format: 'jpg',   // image formats: 'png', 'jpg' (default: 'png')
        quality: 0.8,    // image quality: 0..1 (only relevant for jpg, default: 1)
        result: 'base64'   // result types: 'file', 'base64' (default: 'file')
      });
      // console.log('uri', uri)
      if (uri) {
        this.setState({ map_screenshot_url: '' + 'data:image/png;base64,' + uri }, () => {
          // console.log('this.state',JSON.stringify( this.state))
          this.props.setMapData(this.state)
        });
      }
    } catch (err) {
      alert('Could not record co-ordinates')
    }
  }
  takeScreenShot = () => {
    alert("Screenshot Captured");
    this.refs.viewShotMap.capture().then(async (data) => {
      AsyncStorage.setItem('mapScreenshot', data).then((val) => {
        console.log('saving:  ', val);
      });
    });
  };
  render() {
    const { focusUserLocation, userLocation, leftWides, leftOks, leftShorts, rightWides, rightOks, rightShorts } = this.state
    return (
      <View style={{flex: 1, justifyContent: 'space-between'}}>
        <Header>
          <Text onPress={() => NavigationService.goBack()}>Close</Text>
          <Text>Turns</Text>
          <Text onPress={() => this.setState({focusUserLocation: true})}>
            Sync
          </Text>
          <Text onPress={this.takeScreenShot}>
            Capture
          </Text>
        </Header>
        <ViewShot
          style={{flex: 1}}
          ref="viewShotMap"
          // options={{format: 'png', quality: 0.9}}
          options={{result: 'base64'}}>
          <MapView
            provider={PROVIDER_GOOGLE} // remove if not using Google Maps
            // style={[{ position:'absolute', top:scale(30), bottom:scale(30), left:0, right:0 }]}
            style={{flex: 1}}
            // initialRegion={INITIAL_REGION}
            region={userLocation && focusUserLocation ? userLocation : null}
            camera={Camera}
            showsUserLocation
            // showMyLocationButton
            loadingEnabled
            ref={(r) => (this.refMapView = r)}>
            {leftWides.map((location) => (
              <Marker
                coordinate={location} // with origin and destination values
                anchor={{x: 0, y: 0}} // controls the position of the marking image on the map
                image={LEFT_WIDE_IMG}
              />
            ))}
            {leftOks.map((location) => (
              <Marker
                coordinate={location} // with origin and destination values
                anchor={{x: 0, y: 0}} // controls the position of the marking image on the map
                image={LEFT_OK_IMG}
              />
            ))}
            {leftShorts.map((location) => (
              <Marker
                coordinate={location} // with origin and destination values
                anchor={{x: 0, y: 0}} // controls the position of the marking image on the map
                image={LEFT_SHORT_IMG}
              />
            ))}
            {rightWides.map((location) => (
              <Marker
                coordinate={location} // with origin and destination values
                anchor={{x: 0, y: 0}} // controls the position of the marking image on the map
                image={RIGHT_WIDE_IMG}
              />
            ))}
            {rightOks.map((location) => (
              <Marker
                coordinate={location} // with origin and destination values
                anchor={{x: 0, y: 0}} // controls the position of the marking image on the map
                image={RIGHT_OK_IMG}
              />
            ))}
            {rightShorts.map((location) => (
              <Marker
                coordinate={location} // with origin and destination values
                anchor={{x: 0, y: 0}} // controls the position of the marking image on the map
                image={RIGHT_SHORT_IMG}
              />
            ))}
          </MapView>
        </ViewShot>

        <Footer>
          <MapButton
            title={`Left Wide (${leftWides.length})`}
            onPress={() => this.processClick('leftWides')}
          />
          <MapButton
            title={`Left Ok (${leftOks.length})`}
            onPress={() => this.processClick('leftOks')}
          />
          <MapButton
            title={`Left Short (${leftShorts.length})`}
            onPress={() => this.processClick('leftShorts')}
          />
          <MapButton
            title={`Right Wide (${rightWides.length})`}
            onPress={() => this.processClick('rightWides')}
          />
          <MapButton
            title={`Right Ok (${rightOks.length})`}
            onPress={() => this.processClick('rightOks')}
          />
          <MapButton
            title={`Right Short (${rightShorts.length})`}
            onPress={() => this.processClick('rightShorts')}
          />
        </Footer>
      </View>
    );
  }
}

const mapStateToProps = state => {
  return {
    userReducer: state.userReducer,
    eveluationFlowReducer: state.eveluationFlowReducer,
  };
};

export default connect(mapStateToProps, { setMapData, })(MapScreen);
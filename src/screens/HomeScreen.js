import React from 'react';
import { StatusBar, Image, View, TouchableOpacity } from 'react-native';
import { connect } from 'react-redux';
import { Loader, ScreenWrapper } from '../components';
import SplashScreen from 'react-native-splash-screen'
import { fetchUserProfileAction, signOutAction } from '../actions';
import { HOME_BG, HOME_TEST_WHEEL, HOME_TEST_WHEELS, HOME_USERS, LOGO, SCREEN_WIDTH, TRUCK_ICON } from '../constants';
import * as colors from '../styles/colors';
import { scale } from '../utils/scale';

class AuthLoadingScreen extends React.Component {
  async componentDidMount() {

  }


  render() {
    return (
      <ScreenWrapper backgroundImage={HOME_BG}>
        <Text onPress={() => this.props.signOutAction()}>Logout</Text>
        <View style={{ marginHorizontal: scale(30), flexDirection: 'row', justifyContent: 'space-around', }}>
          <TouchableOpacity onPress={() => this.props.navigation.navigate('testStack')}>
            <View style={{ justifyContent: 'center', alignItems: 'center' }}>
              <Image source={HOME_TEST_WHEELS} style={{ margin: scale(20), height: scale(130), width: scale(130) }} />
              <Text style={{ color: colors.FONT_WHITE_COLOR, fontWeight: '700' }}>EVALUATION</Text>
            </View>
          </TouchableOpacity>
          <TouchableOpacity onPress={() => this.props.navigation.navigate('usersStack')}>
            <View style={{ justifyContent: 'center', alignItems: 'center' }}>
              <Image source={HOME_USERS} style={{ height: scale(170), width: scale(170) }} />
              <Text style={{ color: colors.FONT_WHITE_COLOR, fontWeight: '700' }}>USERS</Text>
            </View>
          </TouchableOpacity>
        </View>

        <View style={{ marginHorizontal: scale(30), alignSelf: 'flex-start' }}>
          <TouchableOpacity onPress={() => this.props.navigation.navigate('quizStack')}>
            <View style={{ justifyContent: 'center', alignItems: 'center', marginLeft: scale(-10) }}>
              <Image source={TRUCK_ICON} style={{ margin: scale(20), height: scale(170), width: scale(170), resizeMode: 'contain' }} />
              <Text style={{ color: colors.FONT_WHITE_COLOR, fontWeight: '700', textAlign: 'center', marginTop: scale(-55) }}>{`ENTRY LEVEL\n DRIVING SCHOOL`}</Text>
            </View>
          </TouchableOpacity>
        </View>
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', }}>
          <Image
            source={LOGO}
            style={{ width: SCREEN_WIDTH }}
            resizeMode='contain'
          />
        </View>
      </ScreenWrapper>
    )
  }
}

const mapStateToProps = state => {
  return {
    userReducer: state.userReducer,
  };
};

export default connect(mapStateToProps, { fetchUserProfileAction, signOutAction })(AuthLoadingScreen);
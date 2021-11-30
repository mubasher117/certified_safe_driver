import React from 'react';
import { StatusBar } from 'react-native';
import { connect } from 'react-redux';
import { Loader, ScreenWrapper } from '../../components';
import SplashScreen from 'react-native-splash-screen'
import { fetchUserProfileAction } from '../../actions';
import { PLATFORM_IOS, AUTH_BG } from '../../constants';

class AuthLoadingScreen extends React.Component {
  async componentDidMount() {
    StatusBar.setBarStyle('light-content')
    SplashScreen.hide();

    // if (__DEV__ && this.props.userReducer.token) {
    //   // this.props.navigation.navigate('ProfileScreen');
    //   // this.props.navigation.navigate('tabNavigator')
    //   return;
    // }

    // const { userProfile, token } = this.props.userReducer
    if (this.props.userReducer.token) {
      this.props.navigation.navigate('HomeScreen');
    } else {
      this.props.navigation.navigate('authStack');
    }
  }

  // componentWillUnmount() {
  //   StatusBar.setBarStyle('dark-content')
  // }

  render() {
    return (
      <ScreenWrapper backgroundImage={AUTH_BG} contentContainerStyle={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        <Loader color={'white'} />
      </ScreenWrapper>
    )
  }
}

const mapStateToProps = state => {
  return {
    userReducer: state.userReducer,
  };
};

export default connect(mapStateToProps, { fetchUserProfileAction, })(AuthLoadingScreen);
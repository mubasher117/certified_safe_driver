import React, { PureComponent } from 'react';
import { TouchableOpacity, TextInput as RNTextInput, View, Image, StatusBar, Alert } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
import { connect } from 'react-redux';
import { signInWithEmailAndPasswordAction, fetchUserProfileAction, signOutAction, errorMessage, hidePopup, } from '../../actions';
import { ScreenWrapper, Text, LoadingButton } from '../../components';
import * as colors from '../../styles/colors';
import { SCREEN_HEIGHT, emailValidationRegex, SCREEN_WIDTH, AUTH_BG, DEFAULT_FONT_SIZE } from '../../constants';
import { scale } from '../../utils/scale';

const TextInput = (props) => {
  let finalFontSize = DEFAULT_FONT_SIZE;
  if (props.style && props.style.forceFontSize)
    finalFontSize = props.style.forceFontSize;
  else if (props.style && props.style.fontSize)
    finalFontSize = scale(props.style.fontSize);
  return (
    <View style={{ alignItems: 'center', justifyContent: 'space-between', flexDirection: 'row', borderColor: 'white', borderWidth: 2, borderRadius: 5, width: SCREEN_WIDTH * 0.8, backgroundColor: 'rgba(255,255,255,0.7)', height: scale(44), paddingRight: 10, ...props.style, }}>
      <View style={{ height: '100%', backgroundColor: 'white', width: scale(100), paddingLeft: scale(10), justifyContent: 'center', }}>
        <Text>{props.lable}</Text>
      </View>
      <RNTextInput
        ref={props.setRef}
        spellCheck={false}
        autoCorrect={false}
        placeholderTextColor={props.placeholderTextColor ? props.placeholderTextColor : colors.PLACEHOLDER_COLOR}
        underlineColorAndroid={'transparent'}
        {...props} //props aboove this will act like default, position is important
        style={{ color: colors.FONT_BLACK_COLOR, width: '95%', borderWidth: 0, padding: 0, paddingLeft: scale(20), ...props.textInputStyle, fontSize: finalFontSize, }}
      />
    </View>
  );
}


class SigninScreen extends PureComponent {
  state = { loading: false, email: '', password: '', }

  async componentDidMount() {
    // StatusBar.setBarStyle('light-content')
    if (__DEV__) {
      this.setState({ email: 'borhan', password: 'cbcsd123', });
    }
  }

  // componentWillUnmount() {
  //   StatusBar.setBarStyle('dark-content')
  // }

  _signInWithEmailAndPassword = async (_email, _password) => {
    // const { loading, email, password, } = this.state
    let email = this.state.email;
    let password = this.state.password;
    if (_email && _password) {
      email = _email;
      password = _password;
    }
    // signInWithEmailAndPassword
    if (email != '') {
      if (password != '') {
        this.setState({ loading: true });
        hidePopup();
        this._signinButton.showLoading()
        let res = await this.props.signInWithEmailAndPasswordAction({ email, password });
        if (res) {
          res = await this.props.fetchUserProfileAction();
          console.log('fetchUserProfileAction: res: ', res);
          // return;
          if (res.is_instructor === true) {
            this._signinButton.hideLoading();
            this.setState({ loading: false })
            this.props.navigation.navigate('HomeScreen')
          } else if (res.is_instructor === false) {
            Alert.alert('You are not instructor. You need to be a instructor.')
            this.props.signOutAction();
            this._signinButton.hideLoading();
            this.setState({ loading: false });
          } else {
            this._signinButton.hideLoading();
            this.setState({ loading: false })
          }

        } else {
          this._signinButton.hideLoading();
          this.setState({ loading: false })
        }
      } else {
        errorMessage('Password cannot be empty')
      }
    } else {
      errorMessage('Enter a valid login')
    }
  }


  render() {
    const { loading, email, password, } = this.state
    return (
      <ScreenWrapper backgroundImage={AUTH_BG} >
        <KeyboardAwareScrollView
          style={{ flex: 1, paddingTop: scale(50) }}
          contentContainerStyle={{ alignItems: 'center', }}
          keyboardShouldPersistTaps='handled'
        // behavior="height"
        >
          <TextInput
            lable={'Login'}
            placeholder='Email'
            autoCapitalize={'none'}
            style={{ marginBottom: 15, }}
            onChangeText={email => this.setState({ email })}
            value={email}
            onSubmitEditing={() => this.passwordField.focus()}
          />
          <TextInput
            lable={'Password'}
            secureTextEntry
            setRef={(passwordField) => this.passwordField = passwordField}
            placeholder='Password'
            autoCapitalize={'none'}
            onChangeText={password => this.setState({ password })}
            value={password}
            // textInputStyle={{ width: '80%' }}
            onSubmitEditing={this._signInWithEmailAndPassword}
          />

          <LoadingButton
            ref={r => this._signinButton = r}
            disabled={loading}
            style={{ marginTop: scale(30), borderRadius: 5 }}
            onPress={this._signInWithEmailAndPassword}
            title={'Connect'}
            titleStyle={{ fontWeight: '500', fontSize: 21 }}
          />
        </KeyboardAwareScrollView>
      </ScreenWrapper>
    );
  }
}



const mapStateToProps = state => {
  return {
    userReducer: state.userReducer
  };
};
export default connect(mapStateToProps, { signInWithEmailAndPasswordAction, fetchUserProfileAction, signOutAction })(SigninScreen);
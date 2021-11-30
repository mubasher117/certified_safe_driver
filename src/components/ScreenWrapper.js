import React from 'react';
import { SafeAreaView, ImageBackground, View } from 'react-native';
import { PLATFORM_IOS, isIPhoneX } from '../constants';

class ScreenWrapper extends React.Component {
  render() {
    if (this.props.backgroundImage) {
      return (
        <ImageBackground source={this.props.backgroundImage} style={{ flex: 1, width: '100%', height: '100%', ...this.props.parentStyle }}>
          <SafeAreaView style={{ flex: 1, paddingTop: PLATFORM_IOS ? isIPhoneX ? 3 : 10 : 24, ...this.props.contentContainerStyle, }}>
            {this.props.children}
          </SafeAreaView>
        </ImageBackground>
      )
    }
    return (
      <View style={{ flex: 1, ...this.props.parentStyle }}>
        <SafeAreaView
          style={{
            flex: 1,
            paddingTop: (!!this.props.parentStyle) ? 0 : PLATFORM_IOS ? isIPhoneX ? 3 : 10 : 24,
            ...this.props.contentContainerStyle,
          }}>
          {this.props.children}
        </SafeAreaView>
      </View>
    )
  }
}

export default ScreenWrapper;

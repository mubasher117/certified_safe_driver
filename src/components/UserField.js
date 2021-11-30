import React, { Component, PureComponent } from 'react';
import { ActivityIndicator, View, Image, TouchableWithoutFeedback } from 'react-native';
import Text from './Text';
import TextInput from './TextInput';
import * as colors from '../styles/colors';
import { scale } from '../utils/scale';
import { RIGHT_ARROW_ICON } from '../constants';

export default class UserField extends PureComponent {
  state = {
    changeColor: false,
  }

  blink() {
    this.blinkInterval = setInterval(() => {
      this.setState({ changeColor: !this.state.changeColor })
    }, 100);

    setTimeout(() => {
      clearInterval(this.blinkInterval)
      this.setState({ changeColor: false })
    }, 1000);
  }

  render() {
    const { title, required, rightArrow, component, onPress, disabled, backgroundColor } = this.props
    return (
      <View>
        <View style={{ backgroundColor: backgroundColor ? backgroundColor : colors.APP_LIGHT_GRAY_COLOR }}>
          <Text style={{ fontWeight: '600', paddingHorizontal: scale(15) }}>{title}</Text>
        </View>
        <TouchableWithoutFeedback disabled={disabled} onPress={onPress}>
          <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', height: scale(38), paddingHorizontal: scale(20), paddingVertical: scale(5) }}>
            {!!component ? component :
              <TextInput
                editable={!disabled}
                {...this.props}
              />}
            {/* TODO: replace with a better image of * */}
            {required && <Text style={{ fontSize: 30, fontWeight: 'bold', color: 'red' }}>*</Text>}
            {rightArrow && <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} />}
          </View>
        </TouchableWithoutFeedback>
      </View>
    )
  }

}

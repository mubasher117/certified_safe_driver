import React, { Component, PureComponent } from 'react';
import { ActivityIndicator, View, Image, TouchableWithoutFeedback, Text } from 'react-native';
// import Text from './Text';
import TextInput from './TextInput';
import * as colors from '../styles/colors';
import { scale } from '../utils/scale';
import { RIGHT_ARROW_ICON } from '../constants';
import YesNoButton from './YesNoButton';

export default class EvaluationTrueFalseOptionField extends PureComponent {

  render() {
    const { title, onPress, onChange, start_time, end_time, value } = this.props
    return (
      <View style={{ borderTopWidth: 0.5, borderColor: colors.APP_BORDER_GRAY_COLOR, justifyContent: 'space-between', paddingVertical: scale(5) }}>
        <View style={{ backgroundColor: colors.APP_LIGHT_GRAY_COLOR }}>
          <Text style={{ marginVertical: 5, fontWeight: '600', paddingHorizontal: scale(14) }}>{title}</Text>
        </View>
        <View style={{ paddingHorizontal: scale(15), backgroundColor: colors.APP_LIGHT_GRAY_COLOR, alignItems: 'flex-end' }}>
          <YesNoButton boolean={true} onChange={onChange} onPress={onPress} initialValue={value} start_time={start_time} end_time={end_time} />
        </View>
      </View>
    )
  }

}

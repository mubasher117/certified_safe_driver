import React, { Component, PureComponent } from 'react';
import { ActivityIndicator, View, Image, TouchableWithoutFeedback } from 'react-native';
import Text from './Text';
import TextInput from './TextInput';
import * as colors from '../styles/colors';
import { scale } from '../utils/scale';
import { RIGHT_ARROW_ICON } from '../constants';
import YesNoButton from './YesNoButton';

export default class EvaluationYesNoOptionField extends PureComponent {

  render() {
    const { title, onPress, onChange,start_time,end_time, value } = this.props
    return (
      <View style={{ borderTopWidth: 0.5, borderColor: colors.APP_BORDER_GRAY_COLOR, flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', height: scale(38), paddingHorizontal: scale(20), paddingVertical: scale(5) }}>
        <Text>{title}</Text>
        <YesNoButton onChange={onChange} onPress={onPress} initialValue={value} start_time={start_time}  end_time={end_time} />
      </View>
    )
  }

}

import React, { Component, PureComponent } from 'react';
import { ActivityIndicator, View, Image, TouchableWithoutFeedback } from 'react-native';
import Text from './Text';
import TextInput from './TextInput';
import * as colors from '../styles/colors';
import { scale } from '../utils/scale';
import { RIGHT_ARROW_ICON } from '../constants';
import { Option4Buttons } from '.';

export default class Evaluation4OptionField extends PureComponent {

  render() {
    const { title, value, onChange, start_time,end_time } = this.props
    return (
      <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', height: scale(38), paddingHorizontal: scale(20), paddingVertical: scale(5) }}>
        <Text>{title}</Text>
        <Option4Buttons initialValue={value} onChange={onChange} start_time={start_time}  end_time={end_time} />
      </View>
    )
  }

}

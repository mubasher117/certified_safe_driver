import React, { Component, PureComponent } from 'react';
import { ActivityIndicator, View, Image, TouchableWithoutFeedback } from 'react-native';
import Text from './Text';
import TextInput from './TextInput';
import * as colors from '../styles/colors';
import { scale } from '../utils/scale';
import { RIGHT_ARROW_ICON } from '../constants';
import ImpButton from './ImpButton';

export default class EvaluationImpOptionField extends PureComponent {

  render() {
    const { title, value, onPress, onChange, start_time,end_time } = this.props
    return (
      <View style={{ borderTopWidth: 0.5, borderColor: colors.APP_BORDER_GRAY_COLOR, flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', height: scale(38), paddingHorizontal: scale(20), paddingVertical: scale(5) }}>
        <Text>{title}</Text>
        <ImpButton initialValue={value} onChange={onChange} start_time={start_time}  end_time={end_time} />
      </View>
    )
  }

}

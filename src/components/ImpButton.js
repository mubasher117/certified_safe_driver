import React, { Component, PureComponent } from 'react';
import { ActivityIndicator, View, NativeModules,Alert, LayoutAnimation, Image, TouchableWithoutFeedback } from 'react-native';
import Text from './Text';
import TextInput from './TextInput';
import * as colors from '../styles/colors';
import { scale } from '../utils/scale';
import { RIGHT_ARROW_ICON, IS_TAB } from '../constants';
import ActionSheet from 'react-native-actionsheet'
import { TouchableOpacity } from 'react-native-gesture-handler';

const { UIManager } = NativeModules;
UIManager.setLayoutAnimationEnabledExperimental &&
  UIManager.setLayoutAnimationEnabledExperimental(true)

const _width = scale(36);
const _height = scale(28);
const _rad = 5

//HINT: on tab, width is _width*7
//on phone width is _width
//hight is always _width

export default class ImpButton extends PureComponent {
  state = {
    value: 0,
    left: 2 * _width,
  }

  componentDidMount() {
    if (this.props.initialValue != undefined && this.props.initialValue != 0 && this.props.initialValue != null) {
      this.onChange(this.props.initialValue)
      // if (IS_TAB)
      //   this.onChange(this.props.initialValue)
      // else
      //   this.setState({ value: this.props.initialValue })
    }
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevProps.initialValue != this.props.initialValue && this.props.initialValue != this.state.value) {
      this.onChange(this.props.initialValue)
    }
  }

  onChange = (value) => {
    LayoutAnimation.configureNext(
      LayoutAnimation.create(200, 'easeInEaseOut', 'opacity')
    );
    console.log('impButton value', value)
    this.setState({ value, left: value == 0 ? 2 * _width : (value - 1) * _width })
    if (this.props.onChange && typeof (this.props.onChange) == 'function')
      this.props.onChange(value)
  }

  onButtonPress = (value) => {
    if (!!!this.props.start_time) {
      Alert.alert('Please start the test to make changes')
      return
    } else if (this.props.start_time && this.props.end_time) {
      Alert.alert('this test is marked completed')
      return;
    } else {
      this.onChange(value)
    }
  }

  render() {
    const { disabled } = this.props
    const { left, value } = this.state
    const absoluteStyle = { borderRadius: 5, height: _height, width: _width, position: 'absolute', left: left, backgroundColor: 'white' }

    return (
      <View style={{ flexDirection: 'row', backgroundColor: colors.APP_LIGHT_GRAY_COLOR }}>
        <View style={absoluteStyle} />
        <TouchableWithoutFeedback disabled={disabled} onPress={() => this.onButtonPress(1)}>
          <View style={[styles.buttonView, { borderTopLeftRadius: _rad, borderBottomLeftRadius: _rad }]}>
            <Text style={styles.buttonText}>Ok</Text>
          </View>
        </TouchableWithoutFeedback>
        <TouchableWithoutFeedback disabled={disabled} onPress={() => this.onButtonPress(2)}>
          <View style={[styles.buttonView, { borderRightWidth: 0.5, borderTopRightRadius: _rad, borderBottomRightRadius: _rad }]}>
            <Text style={styles.buttonText}>Imp</Text>
          </View>
        </TouchableWithoutFeedback>
        <TouchableWithoutFeedback disabled={disabled} onPress={() => this.onButtonPress(0)}>
          <View style={[styles.buttonView, { borderRightWidth: 0.5, borderTopRightRadius: _rad, borderBottomRightRadius: _rad }]}>
            <Text style={styles.buttonText}>N/A</Text>
          </View>
        </TouchableWithoutFeedback>
      </View>
    )
  }
}

const styles = {
  buttonView: { overFlow: 'hidden', width: _width, height: _height, borderWidth: 0.5, borderRightWidth: 0, borderColor: colors.APP_BORDER_GRAY_COLOR, justifyContent: 'center', alignItems: 'center' },
  buttonText: { color: 'black', fontSize: 14 }
}
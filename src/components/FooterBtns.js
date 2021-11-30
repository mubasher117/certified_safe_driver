import React, { Component, PureComponent } from 'react';
import { ActivityIndicator, View, NativeModules, LayoutAnimation, Image, TouchableWithoutFeedback } from 'react-native';
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

const _width = scale(64);
const _height = scale(28);
const _rad = 5

//HINT: on tab, width is _width*7
//on phone width is _width
//hight is always _width

export default class FooterBtns extends PureComponent {
  state = {
    value: false,
    left: 0,
  }

  componentDidMount() {
    if (this.props.initialValue != undefined || this.props.initialValue != null) {
      this.onChange(this.props.initialValue)
    }
  }

  componentDidUpdate(prevProps, prevState){
    if(prevProps.initialValue != this.props.initialValue && this.props.initialValue!=this.state.value){
      this.onChange(this.props.initialValue)
    }
  }

  onChange = (value) => {
    LayoutAnimation.configureNext(
      LayoutAnimation.create(200, 'easeInEaseOut', 'opacity')
    );
    console.log('footerBtns value', value)
    this.setState({ value, left: value ? _width : 0 })
    if (this.props.onChange && typeof (this.props.onChange) == 'function')
      this.props.onChange(value)
  }

  render() {
    const { disabled } = this.props
    const { left, value } = this.state
    const absoluteStyle = { borderRadius: 5, height: _height, width: _width, position: 'absolute', left: left, backgroundColor: 'white' }

    return (
      <View style={{ flexDirection: 'row', backgroundColor: colors.APP_LIGHT_GRAY_COLOR, borderRadius: 4 }}>
        <View style={absoluteStyle} />
        <TouchableWithoutFeedback disabled={disabled} onPress={() => this.onChange(false)}>
          <View style={[styles.buttonView, { borderTopLeftRadius: _rad, borderBottomLeftRadius: _rad }]}>
            <Text style={styles.buttonText}>Used</Text>
          </View>
        </TouchableWithoutFeedback>
        <TouchableWithoutFeedback disabled={disabled} onPress={() => this.onChange(true)}>
          <View style={[styles.buttonView, { borderRightWidth: 0.5, borderTopRightRadius: _rad, borderBottomRightRadius: _rad }]}>
            <Text style={styles.buttonText}>Reviewed</Text>
          </View>
        </TouchableWithoutFeedback>
      </View>
    )
  }
}

const styles = {
  buttonView: { overFlow: 'hidden', width: _width, height: _height, borderRightWidth: 0, borderTopLeftRadius: 4, borderBottomLeftRadius: 4, borderColor: colors.APP_BORDER_GRAY_COLOR, borderWidth: 0.5, justifyContent: 'center', alignItems: 'center' },
  buttonText: { color: 'black', fontSize: 12 }
}
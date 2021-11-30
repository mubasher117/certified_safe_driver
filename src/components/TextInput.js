import React from 'react';
import { TextInput as RNTextInput, View, StyleSheet } from 'react-native';
import { DEFAULT_FONT_SIZE, SCREEN_WIDTH } from '../constants';
import * as colors from '../styles/colors';
import { scale } from '../utils/scale';

export default TextInput = (props) => {
  let finalFontSize = DEFAULT_FONT_SIZE;
  if (props.style && props.style.forceFontSize)
    finalFontSize = props.style.forceFontSize;
  else if (props.style && props.style.fontSize)
    finalFontSize = scale(props.style.fontSize);
  return (
    <RNTextInput
      ref={props.setRef}
      spellCheck={false}
      autoCorrect={false}
      placeholderTextColor={props.placeholderTextColor ? props.placeholderTextColor : colors.PLACEHOLDER_COLOR}
      underlineColorAndroid={'transparent'}
      {...props} //props aboove this will act like default, position is important
      style={{ color: colors.FONT_BLACK_COLOR, width: '95%', padding: 0, paddingRight: scale(10), height: scale(38), ...props.style, fontSize: finalFontSize, }}
    />
  );
}
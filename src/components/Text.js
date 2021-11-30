import React from 'react';
import { Text as RNText, Platform } from 'react-native';
import { FONT_BLACK_COLOR } from '../styles/colors';
import { DEFAULT_FONT_SIZE } from '../constants';
import { scale } from '../utils/scale';

export default Text = (props) => {
  let finalFontSize = DEFAULT_FONT_SIZE;

  if (props.style && props.style.forceFontSize) {
    finalFontSize = props.style.forceFontSize;
    delete props.style.forceFontSize
  } else if (props.style && props.style.fontSize) {
    finalFontSize = scale(props.style.fontSize);
  }



  return (<RNText
    {...props}
    style={{
      color: FONT_BLACK_COLOR,
      ...props.style,
      fontSize: finalFontSize,
    }}
  >
    {props.children}
  </RNText>);
};


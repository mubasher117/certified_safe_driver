import React, { Component, PureComponent } from 'react';
import { ActivityIndicator } from 'react-native';
import * as colors from '../styles/colors';

export default Loader = (props) =>
  <ActivityIndicator
    size={props.size || 'small'}
    style={[{ padding: 1 }, props.style]}
    color={props.color || colors.APP_LOADER_COLOR}
  />

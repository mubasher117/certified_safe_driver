import React, { Component, PureComponent } from 'react';
import { Image, View, TouchableOpacity } from 'react-native';
import Text from './Text';
import { scale } from '../utils/scale';
import { SCREEN_HEIGHT, CROSS_ICON, DEFAULT_BORDER_RADIUS } from '../constants';
import { hidePopup } from '../actions';
import { APP_FRONT_COLOR } from '../styles/colors';
export default PopupBase = (props) => {
  const { onClose } = props;
  return (
    <View style={{borderColor: APP_FRONT_COLOR, borderRadius: 10, borderWidth: 2, width: '85%', alignItems: 'center', padding: 10, }}>
      <TouchableOpacity
        onPress={() => {
          if (onClose && typeof (onClose) == 'function') {
            onClose();
          }
          hidePopup()
        }}
        // style={{ position: 'absolute', right: 0 }}
        style={{ alignSelf: 'flex-end' }}
      >
        <Image source={CROSS_ICON} style={{ height: 40, width: 40, marginRight: -10, marginTop: -10 }} />
      </TouchableOpacity>
      {props.children}
    </View>
  )
}
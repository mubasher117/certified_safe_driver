import React from 'react';
import {TouchableOpacity, Text, StyleSheet, Image, View} from 'react-native';
import {CHECK_ICON} from '../constants';
import * as colors from '../styles/colors';

const CheckBoxGroup = ({
  selected,
  onPress,
  style,
  textStyle,
  size = 30,
  color = colors.APP_COLOR,
  text = '',
  tintColor,
  ...props
}) => (
  <TouchableOpacity
    style={[styles.checkBox, style]}
    onPress={onPress}
    {...props}>
    {selected ? (
      <View
        style={{
          height: 20,
          width: 20,
          borderRadius: 5,
          borderColor: colors.APP_GRAY_COLOR,
        }}>
        <Image
          source={CHECK_ICON}
          style={{height: 19, width: 19, tintColor: tintColor}}
        />
      </View>
    ) : (
      <View
        style={{
          height: 20,
          width: 20,
          borderRadius: 5,
          borderColor: colors.APP_GRAY_COLOR,
          borderWidth: 1,
        }}
      />
    )}

    <Text style={textStyle}> {text} </Text>
  </TouchableOpacity>
);

export default CheckBoxGroup;

const styles = StyleSheet.create({
  checkBox: {
    flexDirection: 'row',
    // alignItems: 'center'
  },
});

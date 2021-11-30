import React, { Component, PureComponent } from 'react';
import { SafeAreaView, View } from 'react-native';
import * as colors from '../styles/colors';
import { PLATFORM_IOS, isIPhoneX } from '../constants';

export default Footer = (props) =>
  <SafeAreaView style={{ backgroundColor: colors.APP_GRAY_COLOR }}>
    <View style={{ paddingHorizontal: 10, paddingTop: 10, paddingBottom: PLATFORM_IOS ? isIPhoneX ? 0 : 20 : 24, backgroundColor: colors.APP_GRAY_COLOR, flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', }}>
      {props.children}
    </View>
  </SafeAreaView>

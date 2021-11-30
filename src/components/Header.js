import React, { Component, PureComponent } from 'react';
import { SafeAreaView, Text, View, Platform } from 'react-native';
import * as colors from '../styles/colors';
import { PLATFORM_IOS, isIPhoneX } from '../constants';

export default Header = (props) =>
  <SafeAreaView style={{ backgroundColor: colors.APP_GRAY_COLOR, }}>
    <View style={{ paddingHorizontal: 10, paddingBottom: 10, paddingTop: PLATFORM_IOS ? isIPhoneX ? 0 : 20 : Platform.OS == 'ios' || PLATFORM_IOS ? 24 : 40, backgroundColor: colors.APP_GRAY_COLOR, flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', ...props.style }}>
      {props.children}
      {/* <View style={{ justifyContent: 'flex-start', ...colors.VISUAL }}>
        <Text >Home</Text>
      </View>
      <View style={{ flex: 1, alignItems: 'center', ...colors.VISUAL2 }}>
        <Text >STUDENT</Text>
      </View>
      <View style={{ alignItems: 'flex-end', justifyContent: 'flex-end', ...colors.VISUAL3 }}>
        <Text >+</Text>
      </View> */}
    </View>
  </SafeAreaView>

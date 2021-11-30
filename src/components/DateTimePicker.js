import React, { Component, PureComponent } from 'react';
import { SafeAreaView, View } from 'react-native';
import * as colors from '../styles/colors';
import { PLATFORM_IOS, isIPhoneX } from '../constants';
import DateTimePickerModal from "react-native-modal-datetime-picker";
import { hidePopup } from '../actions';
import moment from 'moment';

export default DateTimePicker = (props) =>
  {
    console.log("DATETIME DATE IS:  ", props.date)
  return <DateTimePickerModal
    isVisible={true}
    mode={props.mode ? props.mode : "date"}
    date={props.date ? props.date : new Date()}
    onConfirm={(date) => {
      if (props.onConfirm && typeof (props.onConfirm) == 'function') {
        if (props.unformated) {
          props.onConfirm(date)
        } else {
          props.onConfirm(moment(date).format('YYYY-MM-DD'))
        }
      }
      hidePopup()
    }}
    onCancel={() => {
      if (props.onCancel && typeof (props.onCancel) == 'function') {
        props.onCancel()
      }
      hidePopup()
    }}
  />
}
import React, {Component, PureComponent} from 'react';
import {
  ActivityIndicator,
  View,
  Image,
  TouchableWithoutFeedback,
  Alert,
  TouchableOpacity,
} from 'react-native';
import Text from './Text';
import TextInput from './TextInput';
import * as colors from '../styles/colors';
import {scale} from '../utils/scale';
import {
  RIGHT_ARROW_ICON,
  COLORED_PHOTO_ICON,
  GRAY_PHOTO_ICON,
} from '../constants';
import {pickFromGallery, pickFromCamera} from './camera';
import ActionSheet from 'react-native-actionsheet';

export default class EvaluationField extends PureComponent {
  state = {
    changeColor: false,
  };

  blink() {
    this.blinkInterval = setInterval(() => {
      this.setState({changeColor: !this.state.changeColor});
    }, 100);

    setTimeout(() => {
      clearInterval(this.blinkInterval);
      this.setState({changeColor: false});
    }, 1000);
  }

  _imagePickerSheet = () => {
    const ImagePickerOptions = [
      // '', 
      'Choose from Gallery', 'Cancel'
    ];

    return (
      <ActionSheet
        ref={(ImagePickerSheet) => (this.ImagePickerSheet = ImagePickerSheet)}
        title={'Select Image'}
        options={ImagePickerOptions}
        cancelButtonIndex={2}
        // destructiveButtonIndex={1}
        onPress={async (index) => {
          if (index != 2) {
            // if (index == 0) {
            //   let res = await pickFromCamera();
            //   console.log(
            //     'pickFromCamera res',
            //     `${res.mime},base64.${res.data}`,
            //   );
            //   if (res && !res.cancelled && res.uri)
            //     this.props.notesImg(`${res.mime};base64,${res.data}`);
            // } else 
            if (index === 0) {
              let res = await pickFromGallery();
              // console.log('_pickFromGallery res', res);
              console.log(
                '_pickFromGallery res',
                `${res.mime};base64,${res.data}`,
              );
              if (res && !res.cancelled && res.uri);
              this.props.notesImg(`${res.mime};base64,${res.data}`);
            }
          }
        }}
      />
    );
  };

  render() {
    const {
      title,
      required,
      rightArrow,
      component,
      onPress,
      disabled,
      oneliner,
      imageBox,
    } = this.props;
    if (oneliner) {
      return (
        <View
          style={{
            flexDirection: 'row',
            justifyContent: 'space-between',
            alignItems: 'center',
            height: scale(38),
            paddingHorizontal: scale(20),
            paddingVertical: scale(5),
          }}>
          {!!component ? (
            component
          ) : (
            <TextInput
              setRef={(r) => (this._textInput = r)}
              editable={!disabled}
              placeholder={title}
              onFocus={() => {
                if (!!!this.props.start_time) {
                  Alert.alert('Please start the test to make changes');
                  this._textInput.blur();
                  return;
                } else if (this.props.start_time && this.props.end_time) {
                  Alert.alert('this test is marked completed');
                  this._textInput.blur();
                  return;
                }
              }}
              {...this.props}
            />
          )}
          {/* TODO: replace with a better image of * */}
          {required && (
            <Text style={{fontSize: 30, fontWeight: 'bold', color: 'red'}}>
              *
            </Text>
          )}
          {rightArrow && (
            <Image
              source={RIGHT_ARROW_ICON}
              style={{height: scale(12), width: scale(12)}}
            />
          )}
          {imageBox && (
            <TouchableOpacity
              onPress={() => {
                this.ImagePickerSheet.show();
              }}>
              <Image
                source={GRAY_PHOTO_ICON}
                style={{
                  height: scale(40),
                  width: scale(38),
                  marginRight: scale(12),
                }}
              />
            </TouchableOpacity>
          )}
          {this._imagePickerSheet()}
        </View>
      );
    }
    return (
      <View>
        <View style={{backgroundColor: colors.APP_LIGHT_GRAY_COLOR}}>
          <Text style={{fontWeight: '600', paddingHorizontal: scale(15)}}>
            {title}
          </Text>
        </View>

        {!this.props.hideInputField && (
          <TouchableWithoutFeedback
            disabled={disabled}
            onPress={() => {
              console.log('this.props.start_time', this.props.start_time);
              console.log('this.props.end_time', this.props.end_time);
              if (!!!this.props.start_time) {
                Alert.alert('Please start the test to make changes');
                return;
              } else if (this.props.start_time && this.props.end_time) {
                Alert.alert('this test is marked completed');
              } else {
                onPress();
              }
            }}>
            <View
              style={{
                flexDirection: 'row',
                justifyContent: 'space-between',
                alignItems: 'center',
                height: this.props.isSignature ? scale(100) : scale(38),
                paddingHorizontal: scale(20),
                paddingVertical: scale(5),
              }}>
              {!!component ? (
                component
              ) : (
                <TextInput
                  setRef={(r) => (this._textInput = r)}
                  editable={!disabled}
                  onFocus={() => {
                    if (!!!this.props.start_time) {
                      Alert.alert('Please start the test to make changes');
                      this._textInput.blur();
                      return;
                    } else if (this.props.start_time && this.props.end_time) {
                      Alert.alert('this test is marked completed');
                      this._textInput.blur();
                      return;
                    }
                  }}
                  {...this.props}
                />
              )}
              {/* TODO: replace with a better image of * */}
              {required && (
                <Text style={{fontSize: 30, fontWeight: 'bold', color: 'red'}}>
                  *
                </Text>
              )}
              {rightArrow && (
                <Image
                  source={RIGHT_ARROW_ICON}
                  style={{height: scale(12), width: scale(12)}}
                />
              )}
              {imageBox && (
                <TouchableOpacity
                  onPress={async () => {
                    this.ImagePickerSheet.show();
                  }}>
                  <Image
                    source={GRAY_PHOTO_ICON}
                    style={{
                      height: scale(40),
                      width: scale(38),
                      marginRight: scale(12),
                    }}
                  />
                </TouchableOpacity>
              )}
            </View>
          </TouchableWithoutFeedback>
        )}
        {this._imagePickerSheet()}
      </View>
    );
  }
}
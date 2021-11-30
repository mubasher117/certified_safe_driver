import React, { PureComponent } from 'react';
import { TouchableOpacity, TouchableWithoutFeedback, ActivityIndicator, Dimensions, View } from 'react-native';
import Text from './Text';
import * as colors from '../styles/colors';
import { DEFAULT_FONT_SIZE, SCREEN_WIDTH } from '../constants';
import { scale } from '../utils/scale';


export default class LoadingButton extends PureComponent {
  state = {
    isLoading: false,
  };

  showLoading() {
    this.setState({ isLoading: true });
  }

  hideLoading() {
    this.setState({ isLoading: false });
  }

  render() {
    return (
      <TouchableOpacity disabled={this.props.disabled} style={{ ...styles.button, ...this.props.style }} activeOpacity={0.7} onPress={!this.state.isLoading ? this.props.onPress : null} >
        <>
          {
            this.state.isLoading
              ? <ActivityIndicator size="small" color={this.props.loadingColor || colors.APP_LOADER_COLOR} />
              : <>
                {this.props.leftComponent ?
                  <View
                    style={{ flexDirection: 'row', ...this.props.leftComponentContainerStyle }}
                  >
                    {this.props.leftComponent}
                    <Text style={{ ...styles.title, ...this.props.titleStyle }} >{this.props.title}</Text>
                  </View>
                  :
                  <Text style={{ ...styles.title, ...this.props.titleStyle }} >{this.props.title}</Text>
                }
              </>
          }
        </>
      </TouchableOpacity>
    );
  }
}

const styles = {
  button: {
    width: SCREEN_WIDTH * 0.8,
    justifyContent: 'center',
    alignItems: 'center',
    alignSelf: 'center',
    height:scale( 44),
    borderRadius: 22,
    backgroundColor: 'white',
    marginBottom: scale(20)
  },
  title: {
    fontSize: 21,
    fontWeight: '500',
    color: colors.FONT_BLACK_COLOR,
    // fontWeight:'bold',
  },
};

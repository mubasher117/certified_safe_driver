import React from 'react';
import { StatusBar, StyleSheet, Image, View, } from 'react-native';
import { Loader, ScreenWrapper } from '../components';
import Signature from 'react-native-signature-canvas';
import { IS_TAB, SCREEN_HEIGHT, SCREEN_WIDTH, STATUSBAR_HEIGHT } from '../constants';
import { hideSelector } from '../actions';
import { scale } from '../utils/scale';

export default class SignaturePicker extends React.Component {

    async componentDidMount() {

    }

    handleEmpty = () => {
        console.log('Empty');
    }

    handleClear = () => {
        console.log('clear success!');
    }

    // handleEnd = () => {
    //     // ref.current.readSignature();
    //     this.refs["sign"].readSignature();
    // }
    style = `.m-signature-pad--footer
    .button {
      background-color: 'rgb(175,175,175)';
      color: #FFF;
    }
    .m-signature-pad {
        position: absolute;
        font-size: 10px;
        flex: 1,
        top: 50%;
        left: 50%;
        margin-left: -350px;
        margin-top: -200px;
        border: 1px solid #e8e8e8;
        background-color: #fff;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.27), 0 0 40px rgba(0, 0, 0, 0.08) inset;
      }
    `;

    style = IS_TAB ? `.m-signature-pad--footer
    .button {
      background-color: 'rgb(175,175,175)';
      color: #FFF;
    }
    .m-signature-pad {
        position: absolute;
        font-size: 10px;
        flex: 1,
        top: 50%;
        left: 50%;
        margin-left: -320px;
        margin-top: -190px;
        border: 1px solid #e8e8e8;
        background-color: #fff;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.27), 0 0 40px rgba(0, 0, 0, 0.08) inset;
      }
    ` : `.m-signature-pad--footer
    .button {
      background-color: 'rgb(175,175,175)';
      color: #FFF;
    }`

    render() {
        return (
            <View style={{ flex: 1 }}>
                <Header style={{ justifyContent: 'center', backgroundColor: '#fff' }}>
                    <Text onPress={hideSelector}>Close</Text>
                </Header>

                {/* <View style={{ height: SCREEN_HEIGHT * 0.80, width: IS_TAB ? SCREEN_WIDTH - 90 : SCREEN_WIDTH - 32, marginTop: scale(8) }}> */}
                <View style={{ flex: 1, marginTop: scale(8), borderTopWidth: IS_TAB ? 1 : 0 }}>
                    <Signature
                        onOK={this.props?.handleSignature}
                        onEmpty={this.handleEmpty}
                        descriptionText="Signature"
                        clearText="Clear"
                        confirmText="Save"
                        webStyle={this.style}
                        penColor={'blue'}
                    />
                </View>
            </View>
        )
    }
}

const styles = StyleSheet.create({
    preview: {
        width: 335,
        height: 114,
        backgroundColor: "#F8F8F8",
        justifyContent: "center",
        alignItems: "center",
        marginTop: 15
    },
    previewText: {
        color: "#FFF",
        fontSize: 14,
        height: 40,
        lineHeight: 40,
        paddingLeft: 10,
        paddingRight: 10,
        backgroundColor: "#69B2FF",
        width: 120,
        textAlign: "center",
        marginTop: 10
    }
});
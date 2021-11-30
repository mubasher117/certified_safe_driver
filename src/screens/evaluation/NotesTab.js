import React from 'react';
import { StatusBar, View, Image, ScrollView, Modal, TouchableOpacity, Alert } from 'react-native';
import { connect } from 'react-redux';
import SplashScreen from 'react-native-splash-screen'
import { errorMessage, fetchUserProfileAction, showSelector } from '../../actions';
import { PLATFORM_IOS } from '../../constants';
import * as colors from '../../styles/colors';
import { Text, Selector, Header, ScreenWrapper, EvaluationField, Footer } from '../../components';
import { RIGHT_ARROW_ICON, PLUS_ICON, INFO_ICON, EXPORT_ICON } from '../../constants';
import { scale } from '../../utils/scale';
import { WebView } from 'react-native-webview';
import _ from 'lodash';
import { apiGet, apiPatch, apiPost } from '../../utils/http';
import NOTES from './preview/NOTESPreviewHTML'
import RNHTMLtoPDF from 'react-native-html-to-pdf';
import Share from 'react-native-share';
import moment from 'moment';

class NotesTab extends React.Component {

  state = {
    company: null,
    instructor: null,
    student: null,
    showPreview: false,
    studentNotes: [],
    note: null,
    notesImage: '',
    updatedNotes: {},
    notesCount: 0
  }

  async componentDidMount() {
    // if (this.props.eveluationFlowReducer.student_info) {
    this.getNotesInfo();
    // }
  }

  getNotesInfo = async () => {
    const { company_info, student_info, selected_test } = this.props.eveluationFlowReducer
    let res = await apiGet(`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/notes/`)
    console.log(`getInfoUser res: `, res);
    if (res && res.data && res.data.results) {
      this.setState({ studentNotes: res.data.results });
      // this.DataPapulate(res.data);
      // this.props.navigation.goBack()
      // errorMessage('Student Info Fetch')
    }
  }

  previewNotes = async () => {
    this.setState({ showPreview: true })
  }

  saveNote = async () => {
    console.log('this.state', this.state)
    const { company_info, student_info, selected_test } = this.props.eveluationFlowReducer;
    let apiInput = {
      note: this.state.note,
    };
    if (this.state.notesImage)
    {apiInput['image'] = this.state.notesImage}
    
    if (_.size(this.state.updatedNotes)) {
      let updates = await Promise.all(_.map(this.state.updatedNotes, async (note, id) => {
         await apiPatch(`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/notes/${id}`,  apiInput , true)
         
        this.setState({note: null})
        return
      }))
      // console.log('updates', updates)
    }

    if (this.state.note) {
      let data = {
        note: this.state.note,
        image: this.state.notesImage
      }
      let res = await apiPost(`/api/v1/students/${student_info?.id}/tests/${selected_test?.id}/notes/`, apiInput, true)
      console.log(`notes post res: `, res)
      if (res && res.data) {
        // this.props.navigation.goBack()
        // errorMessage('Student Info Updated')
        // this.getNotesInfo();
        this.setState({note: null})
      }
    }

    this.getNotesInfo();
    this.setState({note: ''})

    return false;
  }

  render() {
    // const { company_name, instructor_name, student_name } = this.state;
    const show = { flex: 1, height: undefined }
    const hide = { flex: 0, height: 0 }
    const { company_info, student_info, instructor_info, selectedTestInfo } = this.props.eveluationFlowReducer;
    console.log('Notes Tabs: ', this.state.updatedNotes, this.state.studentNotes);
    return (
      <>
        <ScreenWrapper parentStyle={this.props.shown ? show : hide} >
          <ScrollView>

            <Modal
              animationType="slide"
              visible={this.state.showPreview}
              onRequestClose={() => { }}>
              <View style={{ flex: 1 }}>
                <Header>
                  <TouchableOpacity onPress={() => this.setState({ showPreview: false })}>
                    <Text style={{ marginLeft: 20, fontSize: 16 }}>{'Close'}</Text>
                  </TouchableOpacity>

                  <Text style={{ marginRight: scale(23) }}>Preview</Text>
                  {/* <Text>Email</Text> */}

                  <TouchableOpacity onPress={async () => {

                    let options = {
                      html: NOTES(this.state.studentNotes, this.state, student_info, company_info, instructor_info, INFO_ICON),
                      fileName: `student_${student_info?.id}_NOTES`,
                      // directory: 'Documents',
                    };
                    this.setState({ showPreview: false })
                    let file = await RNHTMLtoPDF.convert(options)
                    console.log('RNHTMLtoPDF file', file);
                    console.log('RNHTMLtoPDF file path', `${PLATFORM_IOS ? '' : 'file://'}${file.filePath}`);
                    await Share.open({
                      url: `${PLATFORM_IOS ? '' : 'file://'}${file.filePath}`,
                      title: 'Share PDF'
                    })
                  }}>
                    {/* <Text style={{ marginRight: 20, fontSize: 16 }}>Share</Text> */}
                    <Image source={EXPORT_ICON} style={{ resizeMode: 'contain', height: 20, width: 20, paddingRight: 10 }} />
                  </TouchableOpacity>

                </Header>

                <WebView
                  // source={require('./preview/notes.html')}
                  source={{ html: NOTES(this.state.studentNotes, this.state, student_info, company_info, instructor_info, INFO_ICON) }}
                  ref={ref => { this.WebView = ref; }}
                  javaScriptEnabled={true}
                  domStorageEnabled={true}
                  startInLoadingState={true}
                />
              </View>
            </Modal>

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              disabled
              backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
              title={'Company'}
              component={
                <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                  <Text>{company_info && company_info?.name}</Text>
                  {/* <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} /> */}
                </View>
              }
            />

            <EvaluationField
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              disabled
              backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
              title={'Instructor'}
              component={
                <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                  <Text>{instructor_info && `${instructor_info.first_name} ${instructor_info.last_name}`}</Text>
                  {/* <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} /> */}
                </View>
              }
            />

            <EvaluationField
              disabled
              start_time={this.state.start_time}
              end_time={this.state.end_time}
              // required
              backgroundColor={colors.APP_LIGHT_BLUE_COLOR}
              title={'Student'}
              component={
                <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', flex: 1 }}>
                  <Text>{student_info && `${student_info?.first_name} ${student_info?.last_name}`}</Text>
                  {/* <Image source={RIGHT_ARROW_ICON} style={{ height: scale(12), width: scale(12) }} /> */}
                </View>
              }
            />
            {this.state.studentNotes.map((note, index) =>
              <EvaluationField
                start_time={this.state.start_time}
                end_time={this.state.end_time}
                title={`${moment(note.updated).format('YYYY-MM-DD hh:mm:ss')}`}
                defaultValue={note.note}
                onChangeText={_note => this.setState({ updatedNotes: { ...this.state.updatedNotes, [note.id]: _note } })}
              />
            )}

            {this.state?.studentNotes?.length <= 20 ? <EvaluationField
              // rightArrow
              start_time={true}
              end_time={this.state.end_time}
              title={'New Note'}
              onChangeText={note => this.setState({ note })}
              imageBox={true}
              notesImg={(notesImage) => { this.setState({ notesImage }) }}
            />: 
            <Text style={{color: "red"}}>Notes Limit Reached</Text>}
          </ScrollView>
        </ScreenWrapper>
        {this.props.shown && <Footer>

          <TouchableOpacity onPress={() => {
            if (this.state?.studentNotes?.length <= 20){
            this.saveNote()
            }
            else{
              Alert.alert('Notes limit reached')
            }
          }}>
            <Image source={PLUS_ICON} style={{ resizeMode: 'contain', height: 20, width: 20, paddingLeft: 20 }} />
          </TouchableOpacity>

          <TouchableOpacity
            onPress={() => Alert.alert('Notifications', `1. To Add a new Note please tap on the Add button from bottom toolbar \n \n 2. To Add a Photo to a note please Save first (tap on the Save button) and after that tap on the 'Photo' button correponding to that Note.`)}>
            <Image source={INFO_ICON} style={{ resizeMode: 'contain', height: 20, width: 20, paddingRight: 20 }} />
          </TouchableOpacity>

        </Footer>}
      </>
    )
  }
}

const mapStateToProps = state => {
  return {
    userReducer: state.userReducer,
    eveluationFlowReducer: state.eveluationFlowReducer,
  };
};

export default connect(mapStateToProps, { fetchUserProfileAction, }, null, { forwardRef: true })(NotesTab);
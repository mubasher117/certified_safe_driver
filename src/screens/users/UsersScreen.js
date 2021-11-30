import React from 'react';
import { View, Image, Modal, FlatList, RefreshControl, TouchableOpacity } from 'react-native';
import { connect } from 'react-redux';
import { Loader, Text, Header, Footer, Selector, TextInput } from '../../components';
import { SEARCH_ICON, SCREEN_WIDTH } from '../../constants';
import SplashScreen from 'react-native-splash-screen'
import { fetchUserProfileAction, showSelector, errorMessage } from '../../actions';
import { PLATFORM_IOS } from '../../constants';
import NavigationService from '../../navigation/NavigationService';
import { scale } from '../../utils/scale';
import * as colors from '../../styles/colors';
import { apiGet } from '../../utils/http';
import ActionSheet from 'react-native-actionsheet'

let searchQueryTimeout = null;
class UsersScreen extends React.Component {

  state = {
    selectedCompany: null,
    selectedUserType: 'Student',
    loading: false,
    data: []
  }
  componentDidMount() {
    const { navigation } = this.props;
    this.focusListener = navigation.addListener('didFocus', () => {
      if (this.state.selectedCompany)
        this.loadCompanyData()
    });
  }

  componentWillUnmount() {
    // Remove the event listener
    this.focusListener.remove();
  }

  _handleRefresh = () => {

  }

  loadCompanyData = async () => {

    let endpoint = null;
    const { selectedCompany, selectedUserType, searchValue } = this.state
    if (selectedCompany) {
      const studentEndpoint = `/api/v1/students/?company_id=${selectedCompany.id}`
      // const studentEndpoint = '/api/v1/students/'
      const instructorEndpoint = `/api/v1/instructors/?company_id=${selectedCompany.id}`
      if (selectedUserType == 'Student') {
        endpoint = studentEndpoint
      } else {
        endpoint = instructorEndpoint
      }
      if (searchValue) {
        endpoint = endpoint + `&search=${searchValue}`
      }
      this.setState({ loading: true })
      let res = await apiGet(endpoint)
      console.log(`loadCompanyData res for ${selectedUserType}:`, res.data)
      res.data.results.forEach(element => {
        if (element.info && element.info.company)
          console.log('element', element.info.company.id)
        else
          console.log('no company')
      });
      if (res && res.data)
        this.setState({ data: res.data.results, loading: false })
      else
        this.setState({ loading: false })
    } else {
      //select company
    }
  }


  render() {
    const { selectedUserType, selectedCompany, loading, data } = this.state
    return (
      <View style={{ flex: 1, justifyContent: 'space-between', backgroundColor: colors.FONT_WHITE_COLOR }}>
        {/* Header */}
        <Header>
          <Text onPress={() => NavigationService.navigate('HomeScreen')}>Home</Text>
          <Text>{selectedUserType}</Text>
          <Text onPress={() => {
            if (selectedUserType == 'Student') {
              if (selectedCompany) {
                this.props.navigation.navigate('CreateEditUser', { selectedUserType, selectedCompany })
              } else {
                errorMessage('Please select a company')
              }
            } else {
              errorMessage('Please contact system administrator to add a new instructor')
            }
          }}
            style={{ fontSize: 22 }}>      +</Text>
        </Header>

        <View style={{ flex: 1 }}>
          {/* Search Header */}
          <View style={{ flexDirection: 'row', alignItems: 'center', borderBottomWidth: 0.4, borderColor: colors.APP_BORDER_GRAY_COLOR, padding: scale(12) }}>
            <View style={{ flex: 0.85, alignItems: 'center', borderRadius: 10, flexDirection: 'row', backgroundColor: 'rgb(239,239,240)', marginEnd: scale(10) }}>
              <Image style={{ height: 15, width: 20, marginHorizontal: scale(8) }} source={SEARCH_ICON} />
              <TextInput style={styles.textInputStyle}
                keyboardType='default'
                autoCapitalize='none'
                onChangeText={(text) => this.setState({ searchValue: text }, () => {
                  clearTimeout(searchQueryTimeout)
                  searchQueryTimeout = setTimeout(() => {
                    this.loadCompanyData()
                  }, 1000);
                })}
                value={this.state.searchValue} />
            </View>
            <Text numberOfLines={1} style={{ flex: 0.15, textAlign: 'right', color: 'rgb(35,137,251)' }}>Cancel</Text>
          </View>
          <FlatList
            data={data}
            keyExtractor={item => item.id}
            renderItem={({ item }) => {
              const { first_name, last_name, username } = item
              return (
                <TouchableOpacity onPress={() => {
                  this.props.navigation.navigate('CreateEditUser', { selectedUserType, selectedCompany, selectedUser: item })
                }}>
                  <View style={{ height: 40, borderBottomWidth: 0.4, borderColor: colors.APP_BORDER_GRAY_COLOR, justifyContent: 'center' }}>
                    <Text>{(first_name && last_name) ?
                      first_name + ' ' + last_name
                      : last_name ? last_name
                        : first_name ? first_name
                          : username}</Text>
                  </View>
                </TouchableOpacity>
              )
            }}
            contentContainerStyle={{ flexGrow: 1, paddingHorizontal: scale(16) }}
            ListEmptyComponent={!!!loading && <Text style={{ textAlign: 'center', color: colors.APP_GRAY_COLOR, marginTop: scale(20) }}>No Records</Text>}
            refreshControl={<RefreshControl refreshing={this.state.loading} onRefresh={this._handleRefresh} />}
          />
        </View>

        {/* Footer */}
        <Footer>
          <Text
            numberOfLines={1}
            style={{ width: (SCREEN_WIDTH / 3) - 10 }}
            onPress={() => {
              showSelector(
                <Selector
                  title={'Companies'}
                  endpoint={'/api/v1/companies/'}
                  onSelect={(item) => { console.log('items', item); this.setState({ selectedCompany: item }, this.loadCompanyData) }}
                />
              )
            }} >
            {(selectedCompany && selectedCompany.name) ? selectedCompany.name : 'Company'}
          </Text>
          <Text style={{ textAlign: 'center', width: (SCREEN_WIDTH / 3) - scale(50), marginLeft: -15 }} onPress={() => this._userTypeActionSheet.show()}>UserType</Text>
          <Text style={{ textAlign: 'right', width: (SCREEN_WIDTH / 3) - 10 }}>Add Group</Text>
        </Footer>

        <ActionSheet
          ref={o => this._userTypeActionSheet = o}
          title={'Select user type'}
          options={['Student', 'Instructor', 'Cancel']}
          cancelButtonIndex={2}
          //destructiveButtonIndex={1}
          onPress={(index) => {
            console.log('UserScreen ActionSheet user type index', index);
            switch (index) {
              case 0:
                this.setState({ selectedUserType: 'Student' }, this.loadCompanyData)
                break;
              case 1:
                this.setState({ selectedUserType: 'Instructor' }, this.loadCompanyData)
                break;
              default:
                break;
            }
          }}
        />
      </View>
    )
  }
}

const mapStateToProps = state => {
  return {
    userReducer: state.userReducer,
  };
};

export default connect(mapStateToProps, { fetchUserProfileAction, })(UsersScreen);

const styles = {
  textInputStyle: {
    flex: 1,
    height: 38,
    padding: scale(5),
    fontSize: 15,
    color: 'black',
  }
}

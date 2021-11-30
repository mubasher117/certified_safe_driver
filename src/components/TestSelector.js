import React, { PureComponent } from 'react';
import { FlatList, View, TouchableOpacity, Image, RefreshControl } from 'react-native';
import * as colors from '../styles/colors';
import { DEFAULT_FONT_SIZE, SEARCH_ICON, CROSS_ICON } from '../constants';
import { scale } from '../utils/scale';
import Text from './Text';
import Header from './Header';
import TextInput from './TextInput';
import Loader from './Loader';
import { hideSelector } from '../actions';
import { apiGet } from '../utils/http';

let searchQueryTimeout = null;

export default class TestSelector extends PureComponent {
  state = {
    data: [],
    loading: false,
    canAddNew: false,
    creatingNewTest: false,
  }

  componentDidMount() {
    this._handleRefresh()
  }

  _handleRefresh = async () => {
    this.setState({ loading: true, searchValue: '' })
    let res = await apiGet(`/api/v1/students/${this.props.studentId}/tests/`)
    console.log('test selector res ', res);
    let canAddNew = true;
    if (res && res.data) {
      res.data.results.forEach(test => {
        if (test.status == 'pending')
          canAddNew = false
      })
      this.setState({ data: res.data.results, canAddNew, loading: false });
    } else {
      hideSelector();
    }
  }

  onSearch = async () => {
    this.setState({ data: this.props.data.filter(item => item.name.toLowerCase().includes(this.state.searchValue.toLowerCase())) })
  }

  render() {
    const { topComponent, onSelect, title, flatlistProps, displayKey = 'name', displayComponent } = this.props;
    const { data, loading, searchValue, canAddNew } = this.state;
    return (
      <View style={{ flex: 1 }}>
        {/*Top header */}
        <Header>
          <Text onPress={hideSelector}>Cancel</Text>
          <Text>{title}</Text>
          <Text style={{ color: colors.APP_GRAY_COLOR }}>{title}</Text>
        </Header>

        {/* Search header */}
        <View style={{ flexDirection: 'row', alignItems: 'center', borderBottomWidth: 0.4, borderColor: colors.APP_BORDER_GRAY_COLOR, padding: scale(12) }}>
          <View style={{ flex: 1, alignItems: 'center', borderRadius: 10, flexDirection: 'row', backgroundColor: 'rgb(239,239,240)' }}>
            <Image style={{ height: 15, width: 20, marginHorizontal: scale(8) }} source={SEARCH_ICON} />
            <TextInput
              ref={r => this.searchInput = r}
              style={styles.textInputStyle}
              keyboardType='default'
              autoCapitalize='none'
              onChangeText={(searchValue) => this.setState({ searchValue }, this.onSearch)}
              value={searchValue} />
            <TouchableOpacity onPress={this._handleRefresh}>
              <Image style={{ height: 25, width: 25, marginHorizontal: scale(8) }} source={CROSS_ICON} />
            </TouchableOpacity>
          </View>
        </View>

        {/* list of companies */}
        <FlatList
          data={data}
          keyExtractor={item => item.id}
          renderItem={({ item }) => {
            return (
              <TouchableOpacity onPress={() => {
                onSelect(item)
                hideSelector();
              }}>
                <View style={{ height: 40, borderBottomWidth: 0.4, borderColor: colors.APP_BORDER_GRAY_COLOR, justifyContent: 'center' }}>
                  <View style={{ flexDirection: 'row', justifyContent: 'space-between' }}>
                    <Text>{item.name}</Text>
                    <Text>{item.status}</Text>
                  </View>
                </View>
              </TouchableOpacity>
            )
          }}
          contentContainerStyle={{ flexGrow: 1, paddingHorizontal: scale(16) }}
          ListFooterComponent={this.state.canAddNew &&
            <TouchableOpacity
              onPress={async () => {
                this.setState({ creatingNewTest: true })
                await this.props.createNewTest()
                this.setState({ creatingNewTest: false })
                hideSelector()
              }}
              style={{ marginVertical: 20, justifyContent: 'center', alignItems: 'center', width: '100%', borderRadius: 30, backgroundColor: colors.APP_GRAY_COLOR }}>
              {this.state.creatingNewTest ? <Loader /> : <Text style={{ color: 'white', padding: 7, fontWeight: '700' }}>Start New Test</Text>}
            </TouchableOpacity>
          }
          ListEmptyComponent={!!!loading && <Text style={{ textAlign: 'center', color: colors.APP_GRAY_COLOR, marginTop: scale(20) }}>No Records</Text>}
          refreshControl={<RefreshControl refreshing={this.state.loading} onRefresh={this._handleRefresh} />}
          {...flatlistProps}
        />

      </View>
    );
  }
};

const styles = {
  textInputStyle: {
    flex: 1,
    height: 38,
    padding: scale(5),
    fontSize: 15,
    color: 'black',
  }
}
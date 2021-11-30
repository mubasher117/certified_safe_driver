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

export default class Selector extends PureComponent {
  state = {
    data: [],
    loading: false,
    searchValue: '',
  }

  componentDidMount() {
    this._handleRefresh()
  }

  _handleRefresh = async () => {
    if (this.props.endpoint) {
      this.setState({ loading: true, searchValue: '' })
      let res = await apiGet(this.props.endpoint)
      console.log('selector res ', res);
      if (res && res.data) {
        if (this.props.resultPath) {
          this.setState({ data: res[this.props.resultPath], });
        } else {
          this.setState({ data: res.data.results, });
        }
        this.setState({ loading: false })
      } else {
        hideSelector();
      }
    } else if (this.props.data) {
      this.setState({ data: this.props.data })
    } else {
      console.warn('either endpoint or data is required')
    }

  }

  onSearch = async () => {

    if (this.props.endpoint) {
      clearTimeout(searchQueryTimeout)
      searchQueryTimeout = setTimeout(async () => {
        const endpoint = `${this.props.endpoint}?search=${this.state.searchValue}`
        this.setState({ loading: true })
        let res = await apiGet(endpoint)
        console.log('selector search res ', res);
        this.setState({ data: res.data.results, });
        this.setState({ loading: false })
        this.searchInput.blur()
      }, 1000);
    } else {
      //for hard coded data, filter locally
      this.setState({ data: this.props.data.filter(item => item.name.toLowerCase().includes(this.state.searchValue.toLowerCase())) })
    }
  }

  render() {
    const { noSearch, topComponent, onSelect, title, flatlistProps, displayKey = 'name', displayComponent } = this.props;
    const { data, loading, searchValue } = this.state;
    return (
      <View style={{ flex: 1 }}>
        {/*Top header */}
        <Header>
          <Text onPress={hideSelector}>Cancel</Text>
          <Text style={{ textAlign: 'left' }}>{title}</Text>
          <Text style={{ color: colors.APP_GRAY_COLOR }}>    </Text>
        </Header>

        {/* Search header */}
        {!!!noSearch && <View style={{ flexDirection: 'row', alignItems: 'center', borderBottomWidth: 0.4, borderColor: colors.APP_BORDER_GRAY_COLOR, padding: scale(12) }}>
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
        </View>}
        {topComponent && topComponent()}
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
                  {displayComponent ? displayComponent(item) : <Text>{item[displayKey]}</Text>}
                </View>
              </TouchableOpacity>
            )
          }}
          contentContainerStyle={{ flexGrow: 1, paddingHorizontal: scale(16) }}
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
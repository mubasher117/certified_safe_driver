import { Platform, Dimensions, StatusBar } from 'react-native';
import store from '../store'
import { scale } from '../utils/scale';

const { width, height } = Dimensions.get('window')

const X_WIDTH = 375;
const X_HEIGHT = 812;

const XSMAX_WIDTH = 414;
const XSMAX_HEIGHT = 896;

const { height: W_HEIGHT, width: W_WIDTH } = Dimensions.get('window');

export let isIPhoneX = false;

if (Platform.OS === 'ios' && !Platform.isPad && !Platform.isTVOS) {
  isIPhoneX = W_WIDTH === X_WIDTH && W_HEIGHT === X_HEIGHT || W_WIDTH === XSMAX_WIDTH && W_HEIGHT === XSMAX_HEIGHT;
}

export const SCREEN_WIDTH = width > height ? height : width;
export const SCREEN_HEIGHT = width > height ? width : height;
export const ASPECT_RATIO = SCREEN_HEIGHT / SCREEN_WIDTH;
export const PLATFORM_IOS = (Platform.isPad || width > 600) ? true : false;
export const IS_TAB = ((Platform.OS === 'ios' && Platform.isPad) || (width > 750)) ? true : false;
export const STATUSBAR_HEIGHT = PLATFORM_IOS ? 0 : StatusBar.currentHeight
export const DEFAULT_FONT_SIZE = scale(16);
export const IMAGE_CACHE = 'force-cache';
export const DEFAULT_SOURCE = require('../assets/images/DefaultSource.png')
export const emailValidationRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
export const REDUX_STORE_VERSION = '10';

export const AUTH_BG = require('../assets/images/authBackground.png')
export const HOME_BG = require('../assets/images/homeBackground.png')
export const HOME_TEST_WHEEL = require('../assets/images/testWheel.png')
export const HOME_TEST_WHEELS = require('../assets/images/test_wheel.png')
export const HOME_USERS = require('../assets/images/users.png')
export const SEARCH_ICON = require('../assets/icons/search.png')
export const CROSS_ICON = require('../assets/icons/cross_icon.png')
export const CALENDAR_ICON = require('../assets/icons/calendar.png')
export const RIGHT_ARROW_ICON = require('../assets/icons/right_arrow.png')
export const LOGO = require('../assets/images/Logo.png')

export const CLOSE_ICON = require('../assets/icons/close.png')
export const INFO_ICON = require('../assets/icons/info.png')
export const PLAY_ICON = require('../assets/icons/play.png')
export const PAUSE_ICON = require('../assets/icons/pause.png')
export const BACKWARD_ICON = require('../assets/icons/backward.png')
export const FORWARD_ICON = require('../assets/icons/forward.png')
export const PLUS_ICON = require('../assets/icons/plus.png')
export const EXPORT_ICON = require('../assets/icons/export.png')
export const INFO_BLUE_ICON = require('../assets/icons/info_blue.png')

export const PREVIEW_ICON = require('../assets/icons/preview.png')
export const SAVE_ICON = require('../assets/icons/save.png')
export const UNDO_ICON = require('../assets/icons/undo.png')

export const COLORED_PHOTO_ICON = require('../assets/icons/colored_photo.png')
export const GRAY_PHOTO_ICON = require('../assets/icons/gray_photo.png')

export const TRUCK_ICON = require('../assets/icons/truck.png')
export const CHECK_ICON = require('../assets/icons/check.png');

export const ALL_US_STATES = [{ "name": "Alabama, AL", "id": "AL" }, { "name": "Alaska, AK", "id": "AK" }, { "name": "American Samoa, AS", "id": "AS" }, { "name": "Arizona, AZ", "id": "AZ" }, { "name": "Arkansas, AR", "id": "AR" }, { "name": "California, CA", "id": "CA" }, { "name": "Colorado, CO", "id": "CO" }, { "name": "Connecticut, CT", "id": "CT" }, { "name": "Delaware, DE", "id": "DE" }, { "name": "District Of Columbia, DC", "id": "DC" }, { "name": "Federated States Of Micronesia, FM", "id": "FM" }, { "name": "Florida, FL", "id": "FL" }, { "name": "Georgia, GA", "id": "GA" }, { "name": "Guam, GU", "id": "GU" }, { "name": "Hawaii, HI", "id": "HI" }, { "name": "Idaho, ID", "id": "ID" }, { "name": "Illinois, IL", "id": "IL" }, { "name": "Indiana, IN", "id": "IN" }, { "name": "Iowa, IA", "id": "IA" }, { "name": "Kansas, KS", "id": "KS" }, { "name": "Kentucky, KY", "id": "KY" }, { "name": "Louisiana, LA", "id": "LA" }, { "name": "Maine, ME", "id": "ME" }, { "name": "Marshall Islands, MH", "id": "MH" }, { "name": "Maryland, MD", "id": "MD" }, { "name": "Massachusetts, MA", "id": "MA" }, { "name": "Michigan, MI", "id": "MI" }, { "name": "Minnesota, MN", "id": "MN" }, { "name": "Mississippi, MS", "id": "MS" }, { "name": "Missouri, MO", "id": "MO" }, { "name": "Montana, MT", "id": "MT" }, { "name": "Nebraska, NE", "id": "NE" }, { "name": "Nevada, NV", "id": "NV" }, { "name": "New Hampshire, NH", "id": "NH" }, { "name": "New Jersey, NJ", "id": "NJ" }, { "name": "New Mexico, NM", "id": "NM" }, { "name": "New York, NY", "id": "NY" }, { "name": "North Carolina, NC", "id": "NC" }, { "name": "North Dakota, ND", "id": "ND" }, { "name": "Northern Mariana Islands, MP", "id": "MP" }, { "name": "Ohio, OH", "id": "OH" }, { "name": "Oklahoma, OK", "id": "OK" }, { "name": "Oregon, OR", "id": "OR" }, { "name": "Palau, PW", "id": "PW" }, { "name": "Pennsylvania, PA", "id": "PA" }, { "name": "Puerto Rico, PR", "id": "PR" }, { "name": "Rhode Island, RI", "id": "RI" }, { "name": "South Carolina, SC", "id": "SC" }, { "name": "South Dakota, SD", "id": "SD" }, { "name": "Tennessee, TN", "id": "TN" }, { "name": "Texas, TX", "id": "TX" }, { "name": "Utah, UT", "id": "UT" }, { "name": "Vermont, VT", "id": "VT" }, { "name": "Virgin Islands, VI", "id": "VI" }, { "name": "Virginia, VA", "id": "VA" }, { "name": "Washington, WA", "id": "WA" }, { "name": "West Virginia, WV", "id": "WV" }, { "name": "Wisconsin, WI", "id": "WI" }, { "name": "Wyoming, WY", "id": "WY" }]
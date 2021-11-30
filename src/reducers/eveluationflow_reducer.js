import {
    UPDATE_STUDENT_INFO,
    UPDATE_COMPANY_INFO,
    UPDATE_INSTRUCTOR_INFO,
    UPDATE_GROUPMODE_INFO,
    UPDATE_GROUP_INFO,
    UPDATE_SELECTED_TEST,
    UPDATE_TAB_CHANGE_ERROR_MESSAGE,
    UPDATE_SELECTED_TEST_INFO,
    SET_MAP_DATA
} from '../actions/types';

const INITIAL_STATE = {
    student_info: null,
    company_info: null,
    instructor_info: null,
    group_info:null,
    groupMode:false,
    selected_test: null,
    tabChangeErrorMessage: false,
    selectedTestInfo: null,
    mapData: null,
};

export default function (state = INITIAL_STATE, action) {
    switch (action.type) {
        case UPDATE_STUDENT_INFO: {
            return { ...state, student_info: action.payload };
        }
        case UPDATE_COMPANY_INFO: {
            return { ...state, company_info: action.payload };
        }
        case UPDATE_INSTRUCTOR_INFO: {
            return { ...state, instructor_info: action.payload };
        }
        case UPDATE_GROUPMODE_INFO: {
            return { ...state, groupMode: action.payload };
        }
        case UPDATE_GROUP_INFO: {
            return { ...state, group_info: action.payload };
        }
        case UPDATE_SELECTED_TEST: {
            return { ...state, selected_test: action.payload };
        }
        case UPDATE_TAB_CHANGE_ERROR_MESSAGE: {
            return { ...state, tabChangeErrorMessage: action.payload };
        }
        case UPDATE_SELECTED_TEST_INFO: {
            return { ...state, selectedTestInfo: action.payload };
        }
        case SET_MAP_DATA: {
            return { ...state, mapData: action.payload };
        }
        default:
            return state;
    }
}
import {
    UPDATE_STUDENT_INFO,
    UPDATE_COMPANY_INFO,
    UPDATE_INSTRUCTOR_INFO,
    UPDATE_GROUPMODE_INFO,
    UPDATE_GROUP_INFO,
    UPDATE_SELECTED_TEST,
    UPDATE_TAB_CHANGE_ERROR_MESSAGE,
    UPDATE_SELECTED_TEST_INFO,
    SET_MAP_DATA,
    SET_MAP_IMAGE_URL
} from './types';

export const updateCompanyInfo = (company) => async (dispatch, getState) => {
    dispatch({ type: UPDATE_COMPANY_INFO, payload: company });
    return true;
};

export const updateInstructorInfo = (instructor) => async (dispatch, getState) => {
    dispatch({ type: UPDATE_INSTRUCTOR_INFO, payload: instructor });
    return true;
};

export const updateStudentInfo = (student) => async (dispatch, getState) => {
    dispatch({ type: UPDATE_STUDENT_INFO, payload: student });
    return true;
}
export const updateGroupModeInfo = (groupMode) => async (dispatch, getState) => {
    dispatch({ type: UPDATE_GROUPMODE_INFO, payload: groupMode });
    return true;
}
export const updateGroupInfo = (group) => async (dispatch, getState) => {
    dispatch({ type: UPDATE_GROUP_INFO, payload: group });
    return true;
}

export const updateSelectedTest = (test) => async (dispatch, getState) => {
    dispatch({ type: UPDATE_SELECTED_TEST, payload: test });
    return true;
};

export const updateTabChangeErrorMessage = (tabChangeErrorMessage) => async (dispatch, getState) => {
    dispatch({
        type: UPDATE_TAB_CHANGE_ERROR_MESSAGE,
        payload: tabChangeErrorMessage
        // payload:false
    });
    return true;
};

export const updateSelectedTestInfo = (selectedTestInfo) => async (dispatch, getState) => {
    dispatch({ type: UPDATE_SELECTED_TEST_INFO, payload: selectedTestInfo });
    return true;
};

export const setMapData = (data) => async (dispatch, getState) => {
    dispatch({ type: SET_MAP_DATA, payload: data });
};

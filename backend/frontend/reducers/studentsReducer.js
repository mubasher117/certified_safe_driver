import { STUDENTS } from '../actions/studentsActions';

const initialState = {
  studentsListing: {},
  studentReport: {},
  isLoading: false,
  error: '',
};

const StudentsReducer = (state = initialState, action) => {
  switch (action.type) {
    case STUDENTS.GET_STUDENTS:
      return {
        ...state,
        isLoading: true,
        error: '',
      };
    case STUDENTS.GET_STUDENTS_SUCCESS:
      return {
        ...state,
        isLoading: false,
        studentsListing: action.response,
      };
    case STUDENTS.GET_STUDENTS_ERROR:
      return {
        ...state,
        isLoading: false,
        error: action.error,
      };
    case STUDENTS.UPDATE_STUDENT:
      return {
        ...state,
        isLoading: true,
      };
    case STUDENTS.UPDATE_STUDENT_SUCCESS:
      return {
        ...state,
        isLoading: false,
      };
    case STUDENTS.UPDATE_STUDENT_ERROR:
      return {
        ...state,
        isLoading: false,
        error: action.error,
      };

    case STUDENTS.GET_STUDENT_REPORT:
      return {
        ...state,
        isLoading: true,
      };
    case STUDENTS.GET_STUDENT_REPORT_SUCCESS:
      return {
        ...state,
        isLoading: false,
        studentReport: action.response,
      };
    case STUDENTS.GET_STUDENT_REPORT_ERROR:
      return {
        ...state,
        isLoading: false,
        error: action.error,
      };

    case STUDENTS.ADD_STUDENT:
      return {
        ...state,
        isLoading: true,
      };
    case STUDENTS.ADD_STUDENT_SUCCESS:
      return {
        ...state,
        isLoading: false,
      };
    case STUDENTS.ADD_STUDENT_ERROR:
      return {
        ...state,
        isLoading: false,
        error: action.error,
      };

    default:
      return state;
  }
};

export default StudentsReducer;

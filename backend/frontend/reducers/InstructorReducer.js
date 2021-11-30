import { INSTRUCTOR } from '../actions/instructorActions';

const initialState = {
  instructorListing: {},
  isLoading: false,
  error: '',
};

const InstructorReducer = (state = initialState, action) => {
  switch (action.type) {
    case INSTRUCTOR.GET_INSTRUCTOR:
      return {
        ...state,
        isLoading: true,
        error: '',
      };
    case INSTRUCTOR.GET_INSTRUCTOR_SUCCESS:
      return {
        ...state,
        isLoading: false,
        instructorListing: action.response,
      };
    case INSTRUCTOR.GET_INSTRUCTOR_ERROR:
      return {
        ...state,
        isLoading: false,
        error: action.error,
      };
    case INSTRUCTOR.UPDATE_INSTRUCTOR:
      return {
        ...state,
        isLoading: true,
      };
    case INSTRUCTOR.UPDATE_INSTRUCTOR_SUCCESS:
      return {
        ...state,
        isLoading: false,
      };
    case INSTRUCTOR.UPDATE_INSTRUCTOR_ERROR:
      return {
        ...state,
        isLoading: false,
        error: action.error,
      };

    case INSTRUCTOR.ADD_INSTRUCTOR:
      return {
        ...state,
        isLoading: true,
      };
    case INSTRUCTOR.ADD_INSTRUCTOR_SUCCESS:
      return {
        ...state,
        isLoading: false,
      };
    case INSTRUCTOR.ADD_INSTRUCTOR_ERROR:
      return {
        ...state,
        isLoading: false,
        error: action.error,
      };

    default:
      return state;
  }
};

export default InstructorReducer;

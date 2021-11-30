import { COMPANIES } from '../actions/companiesActions';

const initialState = {
  companiesListing: {},
  isLoading: false,
  error: '',
};

const CompaniesReducer = (state = initialState, action) => {
  switch (action.type) {
    case COMPANIES.GET_COMPANIES:
      return {
        ...state,
        isLoading: true,
        error: '',
      };
    case COMPANIES.GET_COMPANIES_SUCCESS:
      return {
        ...state,
        isLoading: false,
        companiesListing: action.response,
      };
    case COMPANIES.GET_COMPANIES_ERROR:
      return {
        ...state,
        isLoading: false,
        error: action.error,
      };

    case COMPANIES.UPDATE_COMPANY:
      return {
        ...state,
        isLoading: true,
      };
    case COMPANIES.UPDATE_COMPANY_SUCCESS:
      return {
        ...state,
        isLoading: false,
      };
    case COMPANIES.UPDATE_COMPANY_ERROR:
      return {
        ...state,
        isLoading: false,
        error: action.error,
      };

    case COMPANIES.ADD_COMPANY:
      return {
        ...state,
        isLoading: true,
      };
    case COMPANIES.ADD_COMPANY_SUCCESS:
      return {
        ...state,
        isLoading: false,
      };
    case COMPANIES.ADD_COMPANY_ERROR:
      return {
        ...state,
        isLoading: false,
        error: action.error,
      };

    default:
      return state;
  }
};

export default CompaniesReducer;

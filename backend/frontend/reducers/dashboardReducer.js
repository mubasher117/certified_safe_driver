import { REVIEWS, TRIP } from '../actions/dashboardActions';

const initialState = {
  onGoingTrips: {
    isLoading: true,
    data: null,
    error: null
  },
  reviews: {
    isLoading: true,
    data: null,
    error: null
  },
  isLoading: false,
  error: null
};

const DashboardReducer = (state = initialState, action) => {
  switch (action.type) {
    case TRIP.GET_ON_GOING:
      return {
        ...state,
        onGoingTrips: {
          isLoading: true,
          data: null,
          error: null
        }
      };
    case TRIP.GET_ON_GOING_SUCCESS:
      return {
        ...state,
        onGoingTrips: {
          isLoading: false,
          data: action.res,
          error: null
        }
      };
    case TRIP.GET_ON_GOING_ERROR:
      return {
        ...state,
        onGoingTrips: {
          isLoading: true,
          data: null,
          error: action.error
        }
      };

    case REVIEWS.GET_REVIEWS_STATS:
      return {
        ...state,
        reviews: {
          isLoading: true,
          data: null,
          error: null
        }
      };
    case REVIEWS.GET_REVIEWS_STATS_SUCCESS:
      return {
        ...state,
        reviews: {
          isLoading: false,
          data: action.res,
          error: null
        }
      };
    case REVIEWS.GET_REVIEWS_STATS_ERROR:
      return {
        ...state,
        reviews: {
          isLoading: true,
          data: null,
          error: action.error
        }
      };

    default:
      return state;
  }
};

export default DashboardReducer;

export const TRIP = {
  GET_ON_GOING: 'GET_ON_GOING_TRIP',
  GET_ON_GOING_SUCCESS: 'GET_ON_GOING_TRIP_SUCCESS',
  GET_ON_GOING_ERROR: 'GET_ON_GOING_TRIP_ERROR'
};

export const REVIEWS = {
  GET_REVIEWS_STATS: 'GET_REVIEWS_STATS',
  GET_REVIEWS_STATS_SUCCESS: 'GET_REVIEWS_STATS_SUCCESS',
  GET_REVIEWS_STATS_ERROR: 'GET_REVIEWS_STATS_ERROR'
};
const getOnGoingTrips = () => ({
  type: TRIP.GET_ON_GOING
});

const setOnGoingTripsDetail = res => ({
  type: TRIP.GET_ON_GOING_SUCCESS,
  res: res
});

const setOnGoingError = error => ({
  type: TRIP.GET_ON_GOING_ERROR,
  error: error
});

const getReviewsStats = () => ({
  type: REVIEWS.GET_REVIEWS_STATS
});

const setReviewsStats = res => ({
  type: REVIEWS.GET_REVIEWS_STATS_SUCCESS,
  res: res
});

const setReviewsErrors = error => ({
  type: REVIEWS.GET_REVIEWS_STATS_ERROR,
  error: error
});

export { getOnGoingTrips, setOnGoingTripsDetail, setOnGoingError, getReviewsStats, setReviewsErrors, setReviewsStats };

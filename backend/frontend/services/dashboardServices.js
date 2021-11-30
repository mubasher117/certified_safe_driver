import axiosInstance from '../helpers/axios-instance';
import {baseUrl} from "../config/constants";

const getOnGoingTrips = async () => {
  try {
    const url = `${baseUrl}/ongoingtrips/`;
    const response = await axiosInstance.get(url);
    return { response };
  } catch (error) {
    return { error };
  }
};

const overAllReviews = async () => {
  try {
    const url = `${baseUrl}/reviews/`;
    const response = await axiosInstance.get(url);
    return { response };
  } catch (error) {
    return { error };
  }
};

export { getOnGoingTrips, overAllReviews };

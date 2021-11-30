import { baseUrl } from '../config/constants';
import axiosInstance from '../helpers/axios-instance';

const doLoginAPI = async payload => {
  try {
    const url = `${baseUrl}/admin/login/token/`;
    const response = await axiosInstance.post(url, payload);
    return { response };
  } catch (error) {
    return { error };
  }
};

const logoutAPI = async () => {
  try {
    const url = `${baseUrl}/auth/logout/`;
    const response = await axiosInstance.get(url);
    return { response };
  } catch (error) {
    return { error };
  }
};

const doGetUser = async () => {
  try {
    const url = `${baseUrl}/account/profile/`;
    const response = await axiosInstance.get(url);
    return { response };
  } catch (error) {
    return { error };
  }
};

export { doLoginAPI, logoutAPI, doGetUser };

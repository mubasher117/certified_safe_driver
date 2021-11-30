import axios from 'axios';
import { baseUrl } from '../config/constants';
import { logoutUser } from '../actions/authActions';
import store from '../store';

const defaultOptions = {
  baseURL: baseUrl,
};
// Create instance
const Instance = axios.create(defaultOptions);
// Set the AUTH token for any request
Instance.interceptors.request.use(async config => {
  const { access } = JSON.parse(localStorage.getItem('user')) || {};
  config.headers.Authorization = access ? `Bearer ${access}` : '';
  return config;
});

Instance.interceptors.response.use(
  response => {
    console.log('in success :: ', response);
    return response;
  },
  error => {
    if (error.response.status === 401 || error.response.status === 403) {
      // store(logoutUser());
    }
    return Promise.reject(error);
  },
);

export default Instance;

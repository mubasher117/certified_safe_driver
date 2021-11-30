import axiosInstance from '../helpers/axios-instance';

const doGetInstructor = async () => {
  try {
    const url = `/users/?is_instructor=true`;
    const response = await axiosInstance.get(url);
    return { response };
  } catch (error) {
    return { error };
  }
};

const doPatchInstructor = async ({ id, ...payload }) => {
  try {
    console.log('payload', payload, id);
    const url = `/users/${id}/`;
    const response = await axiosInstance.patch(url, payload);
    return { response };
  } catch (error) {
    return { error };
  }
};

const doAddInstructor = async payload => {
  try {
    const url = `/user/add/`;
    const response = await axiosInstance.post(url, payload);
    return { response };
  } catch (error) {
    return { error };
  }
};

export { doGetInstructor, doPatchInstructor, doAddInstructor };

import axiosInstance from '../helpers/axios-instance';

const doGetCompanies = async () => {
  try {
    const url = `/companies/`;
    const response = await axiosInstance.get(url);
    return { response };
  } catch (error) {
    return { error };
  }
};

const doPatchCompany = async ({ id, ...payload }) => {
  try {
    // console.log('companies', payload, id);
    const url = `/companies/${id}/`;
    const response = await axiosInstance.patch(url, payload);
    return { response };
  } catch (error) {
    return { error };
  }
};

const doPostCompany = async ({ id, ...payload }) => {
  try {
    const url = `/companies/`;
    const response = await axiosInstance.post(url, payload);
    return { response };
  } catch (error) {
    return { error };
  }
};

export { doGetCompanies, doPatchCompany, doPostCompany };

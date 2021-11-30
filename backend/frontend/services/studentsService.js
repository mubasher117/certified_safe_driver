import axiosInstance from '../helpers/axios-instance';

const doGetStudents = async () => {
  try {
    const url = `/students/`;
    const response = await axiosInstance.get(url);
    return { response };
  } catch (error) {
    return { error };
  }
};

const doPatchStudent = async ({ id, ...payload }) => {
  try {
    console.log('payload', payload, id);
    const url = `/students/${id}/`;
    const response = await axiosInstance.patch(url, payload);
    return { response };
  } catch (error) {
    return { error };
  }
};

const doGetStudentReport = async id => {
  try {
    const url = `/students/${id}/report`;
    const response = await axiosInstance.get(url);
    return { response };
  } catch (error) {
    return { error };
  }
};

const doPostStudent = async payload => {
  try {
    console.log('postStudentSerivce', payload);
    console.log(payload);
    const url = `/user/add/`;
    const response = await axiosInstance.post(url, payload);
    return { response };
  } catch (error) {
    return { error };
  }
};

export { doGetStudents, doPatchStudent, doGetStudentReport, doPostStudent };

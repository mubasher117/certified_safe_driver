import * as Yup from 'yup';

export const loginInitialValues = { username: '', first_name: '', last_name: '', email: '', company: '' };
export const validationSchema = Yup.object().shape({
  username: Yup.string()
    .required('Username is required.')
    .min(2, 'username is should be at least 2 character.'),
  first_name: Yup.string()
    .required('First Name is required.')
    .min(2, 'First Name should be at least 2 character.'),
  last_name: Yup.string()
    .required('Last Name is required.')
    .min(2, 'Last Name should be at least 2 character.'),
  company: Yup.string(),
  email: Yup.string()
    .required('Email is required.')
    .email('Email is not valid'),
});

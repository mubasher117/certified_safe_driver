import * as Yup from 'yup';

export const loginInitialValues = { username: '', password: '' };
export const validationSchema = Yup.object().shape({
  username: Yup.string()
    .email('Email address should be valid.')
    .required('Email address is required.'),
  password: Yup.string()
    .min(6, 'Password must be at least 6 characters')
    .required('Password is required.'),
});

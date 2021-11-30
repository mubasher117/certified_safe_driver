import * as Yup from 'yup';

export const loginInitialValues = { name: '' };
export const validationSchema = Yup.object().shape({
  name: Yup.string()
    .required('Company is required.')
    .min(2, 'Company name should be at least 2 character.'),
});

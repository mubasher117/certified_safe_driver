import React, { useEffect } from 'react';
import { Form, Formik } from 'formik';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';

import { validationSchema } from './validations';
import styles from './styles';

const EditForm = ({ onSubmit, editCompany }) => {
  const classes = styles();
  useEffect(() => {}, [editCompany]);
  return (
    <Container maxWidth="sm">
      <Formik initialValues={editCompany} onSubmit={onSubmit} validationSchema={validationSchema}>
        {props => {
          const { values, touched, errors, handleChange, handleBlur } = props;
          return (
            <Form className={classes.form}>
              <TextField
                error={errors.name && touched.name}
                value={values.name}
                onChange={handleChange}
                onBlur={handleBlur}
                helperText={errors.name && touched.name && errors.name}
                variant="outlined"
                margin="normal"
                fullWidth
                id="name"
                placeholder={'name'}
                name="name"
                autoComplete="name"
                autoFocus
                InputLabelProps={{
                  shrink: true,
                }}
                InputProps={{
                  classes: { input: classes.inputText },
                }}
              />

              <div className={classes.btnContainer}>
                <Button
                  fullWidth={true}
                  size={'large'}
                  type="submit"
                  variant="contained"
                  color="primary"
                  className={classes.submit}
                >
                  Update
                </Button>
              </div>
            </Form>
          );
        }}
      </Formik>
    </Container>
  );
};
export default EditForm;

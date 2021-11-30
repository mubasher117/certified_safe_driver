import React, { useEffect } from 'react';
import { Form, Formik } from 'formik';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import Select from '@material-ui/core/Select';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';

import { validationSchema } from './validations';
import styles from './styles';

const EditForm = ({ onSubmit, editInstructor, companies }) => {
  const classes = styles();

  return (
    <Container maxWidth="sm">
      <Formik initialValues={editInstructor} onSubmit={onSubmit} validationSchema={validationSchema}>
        {props => {
          const { values, touched, errors, handleChange, handleBlur } = props;
          return (
            <Form className={classes.form}>
              <TextField
                error={errors.username && touched.username}
                value={values.username}
                onChange={handleChange}
                onBlur={handleBlur}
                helperText={errors.username && touched.username && errors.username}
                variant="outlined"
                margin="normal"
                fullWidth
                id="username"
                placeholder={'username'}
                name="username"
                autoComplete="username"
                autoFocus
                InputLabelProps={{
                  shrink: true,
                }}
                InputProps={{
                  classes: { input: classes.inputText },
                }}
              />
              <TextField
                error={errors.first_name && touched.first_name}
                value={values.first_name}
                onChange={handleChange}
                onBlur={handleBlur}
                helperText={errors.first_name && touched.first_name && errors.first_name}
                variant="outlined"
                margin="normal"
                fullWidth
                name="first_name"
                placeholder={'First Name'}
                type="first_name"
                id="first_name"
                autoComplete="first_name"
                InputLabelProps={{
                  shrink: true,
                }}
                InputProps={{
                  classes: { input: classes.inputText },
                }}
              />
              <TextField
                error={errors.last_name && touched.last_name}
                value={values.last_name}
                onChange={handleChange}
                onBlur={handleBlur}
                helperText={errors.last_name && touched.last_name && errors.last_name}
                variant="outlined"
                margin="normal"
                fullWidth
                name="last_name"
                placeholder={'Last Name'}
                type="last_name"
                id="last_name"
                autoComplete="last_name"
                InputLabelProps={{
                  shrink: true,
                }}
                InputProps={{
                  classes: { input: classes.inputText },
                }}
              />
              <TextField
                error={errors.email && touched.email}
                value={values.email}
                onChange={handleChange}
                onBlur={handleBlur}
                helperText={errors.email && touched.email && errors.email}
                variant="outlined"
                margin="normal"
                fullWidth
                name="email"
                placeholder={'Email'}
                type="email"
                id="email"
                autoComplete="email"
                InputLabelProps={{
                  shrink: true,
                }}
                InputProps={{
                  classes: { input: classes.inputText },
                }}
              />
              {!editInstructor.id && (
                <TextField
                  error={errors.password && touched.password}
                  value={values.password}
                  onChange={handleChange}
                  onBlur={handleBlur}
                  helperText={errors.password && touched.password && errors.password}
                  variant="outlined"
                  margin="normal"
                  fullWidth
                  name="password"
                  placeholder={'Password'}
                  type="password"
                  id="password"
                  autoComplete="password"
                  InputLabelProps={{
                    shrink: true,
                  }}
                  InputProps={{
                    classes: { input: classes.inputText },
                  }}
                />
              )}
              <TextField
                error={errors.phone && touched.phone}
                value={values.phone}
                onChange={handleChange}
                onBlur={handleBlur}
                helperText={errors.phone && touched.phone && errors.phone}
                variant="outlined"
                margin="normal"
                fullWidth
                name="phone"
                placeholder={'Phone'}
                type="phone"
                id="phone"
                autoComplete="phone"
                InputLabelProps={{
                  shrink: true,
                }}
                InputProps={{
                  classes: { input: classes.inputText },
                }}
              />
              <FormControl variant="outlined" className={classes.formControl}>
                <InputLabel id="company">Company</InputLabel>
                <Select
                  labelId="company"
                  id="company"
                  name="company"
                  value={values.company}
                  onChange={handleChange('company')}
                  label="Company"
                  error={errors.company && touched.company}
                >
                  <MenuItem value="">
                    <em>None</em>
                  </MenuItem>
                  {companies.map(({ id, name }) => (
                    <MenuItem value={id}>{name}</MenuItem>
                  ))}
                </Select>
              </FormControl>

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

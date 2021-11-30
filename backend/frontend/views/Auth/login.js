import React, { useEffect } from 'react';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import InputAdornment from '@material-ui/core/InputAdornment';
import { LockOutlined } from '@material-ui/icons';
import MailOutlineIcon from '@material-ui/icons/MailOutline';
import Grid from '@material-ui/core/Grid';
import { Form, Formik } from 'formik';
import { loginInitialValues, validationSchema } from './validations';
import { loginStyles } from './style';
import { useDispatch, useSelector } from 'react-redux';
import { projectName } from '../../config/constants';
import { doLogin } from '../../actions/authActions';
import logo from '../../assets/images/csd-logo.png';
import Alert from '@material-ui/lab/Alert';
import Paper from '@material-ui/core/Paper';
export default function Login({ history }) {
  const classes = loginStyles();
  const dispatch = useDispatch();
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated);
  const error = useSelector(state => state.auth.error);

  const title = useSelector(state => state.auth.title);

  useEffect(() => {
    document.title = title + `- ${projectName}`;
  }, [title]);

  useEffect(() => {
    if (isAuthenticated) {
      history.push('/app');
    }
  }, [isAuthenticated, history]);

  const onSubmit = (values, { setSubmitting }) => {
    console.log(values);
    dispatch(doLogin(values));
    setTimeout(() => {
      setSubmitting(false);
    }, 4000);
  };

  const loginAlert = error ? (
    <Alert className={classes.alert} severity="error">
      {error}
    </Alert>
  ) : null;

  return (
    <Grid id={'gridContainer'} className={classes.gridContainer} container>
      <Grid item xs={8} sm={5} md={4} lg={3}>
        <Paper className={classes.paper}>
          <img className={classes.logo} src={logo} alt={'logo'} />
          <Formik initialValues={loginInitialValues} onSubmit={onSubmit} validationSchema={validationSchema}>
            {props => {
              const { values, touched, errors, isSubmitting, handleChange, handleBlur } = props;
              return (
                <Form className={classes.form}>
                  {loginAlert}
                  <TextField
                    error={errors.email && touched.email}
                    value={values.email}
                    onChange={handleChange}
                    onBlur={handleBlur}
                    helperText={errors.email && touched.email && errors.email}
                    variant="outlined"
                    margin="normal"
                    fullWidth
                    id="username"
                    placeholder={'Email Address'}
                    name="username"
                    autoComplete="email"
                    autoFocus
                    InputLabelProps={{
                      shrink: true,
                    }}
                    InputProps={{
                      classes: { input: classes.inputText },
                      startAdornment: (
                        <InputAdornment position="start">
                          <MailOutlineIcon className={classes.inputIcon} />
                        </InputAdornment>
                      ),
                    }}
                  />
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
                    autoComplete="current-password"
                    InputLabelProps={{
                      shrink: true,
                    }}
                    InputProps={{
                      classes: { input: classes.inputText },
                      startAdornment: (
                        <InputAdornment position="start">
                          <LockOutlined className={classes.inputIcon} />
                        </InputAdornment>
                      ),
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
                      disabled={isSubmitting}
                    >
                      Login
                    </Button>
                  </div>
                </Form>
              );
            }}
          </Formik>
        </Paper>
      </Grid>
    </Grid>
  );
}

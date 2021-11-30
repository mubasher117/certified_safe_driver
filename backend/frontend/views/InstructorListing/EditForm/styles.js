import { makeStyles } from '@material-ui/core/styles';

export default makeStyles(theme => ({
  formControl: {
    margin: theme.spacing(1),
    minWidth: '100%',
  },
  gridContainer: {
    background: 'linear-gradient(326.5deg, #965BD1 7%, #4D3EC1 75%)',
    display: 'flex',
    justifyContent: 'center',
    height: '100vh',
    minHeight: '100vh',
    maxHeight: '150vh',
    // paddingBottom: theme.spacing(10)
  },
  paper: {
    marginTop: theme.spacing(10),
    background: 'white',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    paddingRight: theme.spacing(3),
    paddingLeft: theme.spacing(3),
    paddingTop: theme.spacing(4),
    paddingBottom: theme.spacing(4),
  },
  logo: {
    height: 56,
  },
  form: {
    width: '100%',
    marginTop: theme.spacing(3),
  },
  submit: {
    margin: theme.spacing(3, 6, 2),
    background: 'linear-gradient(326.5deg, #00C8E6 7%, #00E6BA 75%)',
  },
  inputText: {
    '&::placeholder': {
      textAlign: 'center',
    },
  },
  signUpPageTxt: {
    color: '#b9b6b6',
    marginTop: theme.spacing(1),
  },
  link: {
    color: 'black',
  },
  inputIcon: {
    width: 16,
    height: 16,
    color: '#b9b6b6',
  },
  btnContainer: {
    marginTop: theme.spacing(1),
    marginBottom: theme.spacing(1),
    display: 'flex',
    justifyContent: 'center',
  },
  alert: {
    marginTop: '10px',
  },
}));

import { red } from '@material-ui/core/colors';
import { createMuiTheme } from '@material-ui/core/styles';

// A custom theme for this app
const theme = createMuiTheme({
  typography: {
    fontFamily: 'Avenir-Medium',
    button: {
      textTransform: 'none'
    }
  },
  palette: {
    primary: {
      main: '#965bd1',
    },
    secondary: {
      main: '#19857b',
    },
    error: {
      main: red.A400,
    },
    background: {
      default: '#FCFCFC',
    },
  },
});

export default theme;

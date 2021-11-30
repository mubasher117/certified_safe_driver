import React from 'react';
import { hot } from 'react-hot-loader/root';
import { HashRouter as Router, Route } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { ThemeProvider } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import { Provider } from 'react-redux';
import { createBrowserHistory } from 'history';

import theme from './config/theme';
import configureStore from './store';
import { logoutUser, setAuthenticatedUser, getCurrentUser } from './actions/authActions';
import Login from './views/Auth/login';
import Admin from './layouts/Admin.js';

const store = configureStore();
const hist = createBrowserHistory();
const App = () => {
  if (localStorage.getItem('user')) {
    const localUser = localStorage.getItem('user');
    const user = JSON.parse(localUser);
    store.dispatch(getCurrentUser());
    store.dispatch(setAuthenticatedUser(user));

    console.log('take the user to dashboard');
  } else {
    if (window.location.hash !== '#/') {
      window.location.href = '#/';
    }
    console.log('logout the user');
    localStorage.removeItem('user');
    document.cookie = 'csrftoken=; Max-Age=0';
    document.cookie = 'arp_scroll_position=; Max-Age=0';
    document.cookie = 'sessionid=; Max-Age=0';
  }

  return (
    <Provider store={store}>
      <ToastContainer
        position="top-right"
        autoClose={5000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
      />
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Router history={hist}>
          <Route exact path={'/'} component={Login} />
          <Route exact path={'/login'} component={Login} />
          <Route path="/app" component={Admin} />
        </Router>
      </ThemeProvider>

      {/* Same as */}
      <ToastContainer />
    </Provider>
  );
};
export default hot(App);

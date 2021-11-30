import React from 'react';
import { Redirect, Switch } from 'react-router-dom';
// creates a beautiful scrollbar
import PerfectScrollbar from 'perfect-scrollbar';
import 'perfect-scrollbar/css/perfect-scrollbar.css';
// @material-ui/core components
import { makeStyles } from '@material-ui/core/styles';
// core components
import Navbar from '../components/Navbars/Navbar.js';
import Sidebar from '../components/Sidebar/Sidebar.js';

import routes from '../routes/routes';
import styles from '../assets/jss/material-dashboard-react/layouts/adminStyle.js';
import logo from '../assets/img/reactlogo.png';
import PrivateRoute from '../components/common/private-routes';
import { Hidden } from '@material-ui/core';
import StudentReport from '../views/StudentReport';
import StudentDetailedReport from '../views/StudentDetailedReport';

let ps;

const useStyles = makeStyles(styles);

export default function Admin({ ...rest }) {
  const switchRoutes = (
    <Switch>
      {routes.map((prop, key) => {
        return <PrivateRoute path={'/app' + prop.path} component={prop.component} key={key} />;
      })}
      <PrivateRoute path={'/app/student-report/:id'} component={StudentReport} />
      <PrivateRoute path={'/app/student-detailed-report/:id'} component={StudentDetailedReport} />

      <Redirect from="/app" to="/app/dashboard" />
    </Switch>
  );
  const classes = useStyles();
  const mainPanel = React.createRef();
  const [mobileOpen, setMobileOpen] = React.useState(false);
  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };
  const resizeFunction = () => {
    if (window.innerWidth >= 960) {
      setMobileOpen(false);
    }
  };
  // initialize and destroy the PerfectScrollbar plugin
  React.useEffect(() => {
    if (navigator.platform.indexOf('Win') > -1) {
      ps = new PerfectScrollbar(mainPanel.current, {
        suppressScrollX: true,
        suppressScrollY: false,
      });
      document.body.style.overflow = 'hidden';
    }
    window.addEventListener('resize', resizeFunction);
    // Specify how to clean up after this effect:
    return function cleanup() {
      if (navigator.platform.indexOf('Win') > -1) {
        ps.destroy();
      }
      window.removeEventListener('resize', resizeFunction);
    };
  }, [mainPanel]);
  return (
    <div className={classes.wrapper}>
      <Sidebar
        routes={routes}
        logoText={''}
        logo={logo}
        handleDrawerToggle={handleDrawerToggle}
        open={mobileOpen}
        color={'blue'}
        {...rest}
      />
      <div className={classes.mainPanel} ref={mainPanel}>
        <Hidden mdUp>
          <Navbar routes={routes} handleDrawerToggle={handleDrawerToggle} {...rest} />
        </Hidden>
        <div className={classes.content}>
          <div className={classes.container}>{switchRoutes}</div>
        </div>
      </div>
    </div>
  );
}

/*eslint-disable*/
import React from 'react';
import classNames from 'classnames';
import PropTypes from 'prop-types';
import { NavLink } from 'react-router-dom';
// @material-ui/core components
import { makeStyles, withStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import Hidden from '@material-ui/core/Hidden';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';

import styles from '../../assets/jss/material-dashboard-react/components/sidebarStyle.js';
import LinearProgress from '@material-ui/core/LinearProgress';
import Typography from '@material-ui/core/Typography';
import { useDispatch, useSelector } from 'react-redux';
import { logoutAPI } from '../../services/authServices';
import { logoutUser } from '../../actions/authActions';

const useStyles = makeStyles(styles);

const BorderLinearProgress = withStyles(() => ({
  root: {
    height: 7,
    borderRadius: 5,
  },
  colorPrimary: {
    backgroundColor: 'black',
    width: '85%',
  },
  bar: {
    borderRadius: 5,
    backgroundColor: '#fff',
  },
}))(LinearProgress);

export default function Sidebar(props) {
  const classes = useStyles();
  const dispatch = useDispatch();

  const userDetails = useSelector(state => state.auth.userDetails);
  function activeRoute(routeName) {
    return window.location.href.indexOf(routeName) > -1;
  }

  const logout = async () => {
    await logoutAPI();
    dispatch(logoutUser());
  };

  const { color, routes } = props;
  const logoutListItem = (
    <ListItem button onClick={logout}>
      <ListItemText primary={'Logout'} className={classes.itemText} />
    </ListItem>
  );

  const links = (
    <List className={classes.list}>
      {routes.map((prop, key) => {
        let activePro = ' ';
        let listItemClasses;
        listItemClasses = classNames({
          [' ' + classes[color]]: activeRoute('/app' + prop.path),
        });
        return (
          <NavLink to={'/app' + prop.path} className={activePro + classes.item} activeClassName="active" key={key}>
            <ListItem button className={listItemClasses}>
              <ListItemText primary={prop.name} className={classes.itemText} />
              {prop.path === '/messages' ? (
                <span className={classes.badge}>
                  <span className={classes.badgeText}>2</span>
                </span>
              ) : null}
            </ListItem>
          </NavLink>
        );
      })}
    </List>
  );
  const brand = (
    <div className={classes.logo}>
      <div className={classes.logoImage}>
        <div className={classes.userDetails}>
          <Typography variant="button">
            {userDetails && `${userDetails.first_name} ${userDetails.last_name}`}
          </Typography>
          <br />
          <Typography variant="caption">{userDetails && userDetails.email}</Typography>
        </div>
      </div>
      <div className={classes.progressBarContainer}>
        <BorderLinearProgress variant="determinate" value={75} />
      </div>
    </div>
  );
  return (
    <div>
      <Hidden mdUp implementation="css">
        <Drawer
          variant="temporary"
          anchor={props.rtlActive ? 'left' : 'right'}
          open={props.open}
          classes={{
            paper: classNames(classes.drawerPaper, {
              [classes.drawerPaperRTL]: props.rtlActive,
            }),
          }}
          onClose={props.handleDrawerToggle}
          ModalProps={{
            keepMounted: true, // Better open performance on mobile.
          }}
        >
          {brand}
          <div className={classes.sidebarWrapper}>
            <Typography className={classes.menuHeading}>MENU</Typography>
            {links}
            {logoutListItem}
          </div>
          <div
            className={classes.background}
            style={{ background: 'linear-gradient(229.5deg, rgb(150, 91, 209) 31%, rgb(77, 62, 193) 115%)' }}
          />
        </Drawer>
      </Hidden>
      <Hidden smDown implementation="css">
        <Drawer
          anchor={'left'}
          variant="permanent"
          open
          classes={{
            paper: classNames(classes.drawerPaper, {
              [classes.drawerPaperRTL]: props.rtlActive,
            }),
          }}
        >
          {brand}
          <div className={classes.sidebarWrapper}>
            <Typography className={classes.menuHeading}>MENU</Typography>
            {links}
            {logoutListItem}
          </div>
          <div
            className={classes.background}
            style={{ background: 'linear-gradient(229.5deg, rgb(150, 91, 209) 31%, rgb(77, 62, 193) 115%)' }}
          />
        </Drawer>
      </Hidden>
    </div>
  );
}

Sidebar.propTypes = {
  rtlActive: PropTypes.bool,
  handleDrawerToggle: PropTypes.func,
  bgColor: PropTypes.oneOf(['purple', 'blue', 'green', 'orange', 'red']),
  logo: PropTypes.string,
  image: PropTypes.string,
  logoText: PropTypes.string,
  routes: PropTypes.arrayOf(PropTypes.object),
  open: PropTypes.bool,
};

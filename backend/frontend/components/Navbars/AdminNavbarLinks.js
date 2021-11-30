import React from 'react';
// @material-ui/core components
import { makeStyles } from '@material-ui/core/styles';
import styles from '../../assets/jss/material-dashboard-react/components/headerLinksStyle.js';
// @material-ui/icons
// core components

const useStyles = makeStyles(styles);

export default function AdminNavbarLinks () {
  const classes = useStyles();
  return (
    <div>
      <div className={classes.manager}>
      </div>
    </div>
  );
}

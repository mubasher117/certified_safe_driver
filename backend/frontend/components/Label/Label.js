import React from 'react';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  label: {
    fontSize: '12px',
    fontFamily: 'Avenir-heavy'
  }
}));

const Label = ({ text, className, ...rest }) => {
  const classes = useStyles();
  return (
    <Typography
      className={`${className} ${classes.label}`}
      {...rest}
      variant="subtitle1"
      component="h6">
      {text}
    </Typography>
  );
};

export default Label;

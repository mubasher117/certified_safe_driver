import { withStyles } from '@material-ui/core/styles';
import LinearProgress from '@material-ui/core/LinearProgress';
import React from 'react';
import StarIcon from '@material-ui/icons/Star';
import Typography from '@material-ui/core/Typography';
import { styles } from './style';

const BorderLinearProgress = withStyles((theme) => ({
  root: {
    height: 7,
    borderRadius: 5
  },
  colorPrimary: {
    backgroundColor: '#EAECEF',
    width: '100%'
  },
  bar: {
    borderRadius: 5,
    background: 'linear-gradient(326.5deg, #00C8E6 7%, #00E6BA 75%)'
  }
}))(LinearProgress);

const Progressbar = ({ totalStars: startValue, starValue, totalReview }) => {
  const value = (startValue / totalReview) * 100;
  const classes = styles();
  return (
    <div className={classes.ProgressBarContainer}>
      <div className={'space-between'}>
              <span>
                <StarIcon className={classes.starColor} />
                <Typography
                  className={classes.starCounts}
                  variant="subtitle1"
                  component="span">
                  {starValue}
                </Typography>
              </span>
        <Typography
          className={classes.starCounts}
          variant="subtitle1"
          component="span">
          {startValue}
        </Typography>
      </div>
      <BorderLinearProgress variant="determinate" value={value} />
    </div>
  );

};
export default Progressbar;

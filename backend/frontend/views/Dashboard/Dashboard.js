import React, { useEffect } from 'react';
// @material-ui/core components
// core components
import GridItem from '../../components/Grid/GridItem.js';
import GridContainer from '../../components/Grid/GridContainer.js';
import Card from '../../components/Card/Card.js';
import CardBody from '../../components/Card/CardBody.js';
import Typography from '@material-ui/core/Typography';
import { styles } from './style';
import CardHeader from '../../components/Card/CardHeader';
import Progressbar from './ProgressBar';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import StarIcon from '@material-ui/icons/Star';
import ArrowDropUpIcon from '@material-ui/icons/ArrowDropUp';
import { useDispatch, useSelector } from 'react-redux';
import { getOnGoingTrips, getReviewsStats } from '../../actions/dashboardActions';
import MaterialTable from 'material-table';
import { Paper } from '@material-ui/core';
import OnGoingTripsMap from './OnGoingTripsMap';
import { PieChart, BarChart, MapsChart } from './charts';

export default function Dashboard() {
  const classes = styles();
  const dispatch = useDispatch();
  const onGoingTrips = useSelector(state => state.dashboard.onGoingTrips.data);
  const onGoingTripsIsLoading = useSelector(state => state.dashboard.onGoingTrips.isLoading);

  let locations = [];
  if (onGoingTrips) {
    const tempLocations = onGoingTrips.map(loc => {
      return {
        lat: Number(loc.dropoff_latitude),
        lng: Number(loc.dropoff_longitude),
      };
    });
    locations = tempLocations.filter(e => e);
  }

  useEffect(() => {
    // dispatch(getOnGoingTrips());
    // dispatch(getReviewsStats());
  }, [dispatch]);

  return (
    <GridContainer>
      <GridItem xs={12} sm={12} md={6}>
        <Typography className={classes.title} variant="subtitle1" component="h2">
          Category wise performace
        </Typography>

        <PieChart />
      </GridItem>
      <GridItem xs={12} sm={12} md={6}>
        <Typography className={classes.title} variant="subtitle1" component="h2">
          Top performing companies
        </Typography>
        <Card>
          <>
            <CardHeader>
              <div className={'space-between'}>
                <Typography className={classes.allTimeText} variant="subtitle1" component="h2">
                  All Times
                </Typography>
                <MoreVertIcon />
              </div>

              <div className={'space-between'}>
                <span>
                  <Typography className={classes.totalRating} variant="subtitle1" component="span">
                    {4.7}
                  </Typography>
                  <Typography className={classes.starCounts} variant="subtitle1" component="span">
                    5
                  </Typography>
                  <StarIcon className={classes.starColor} />
                </span>

                <span>
                  <Typography className={classes.starCounts} variant="subtitle1" component="span">
                    0.4
                  </Typography>
                  <ArrowDropUpIcon className={classes.upArrow} />
                </span>
              </div>
            </CardHeader>
            <CardBody>
              <Progressbar starValue={5} totalStars={'5'} totalReview={5} />
              <Progressbar starValue={4} totalStars={4} totalReview={4} />
              <Progressbar starValue={3} totalStars={3} totalReview={2} />
              <Progressbar starValue={2} totalStars={2} totalReview={4} />
              <Progressbar starValue={1} totalStars={2} totalReview={1} />
            </CardBody>
          </>
        </Card>
      </GridItem>

      <GridItem xs={12} sm={12} md={6} style={{ marginTop: '3rem' }}>
        <Typography className={classes.title} variant="subtitle1" component="h2">
          Company Performance
        </Typography>
        <BarChart />
      </GridItem>
      <GridItem xs={12} sm={12} md={6} style={{ marginTop: '3rem' }}>
        <Typography className={classes.title} variant="subtitle1" component="h2">
          Customers worldwide
        </Typography>

        <MapsChart />
      </GridItem>

      <GridItem xs={12} sm={12} md={12} style={{ marginTop: '3rem' }}>
        <Typography className={classes.title} variant="subtitle1" component="h2">
          Companies
        </Typography>

        <MaterialTable
          isLoading={false}
          components={{
            Container: props => <Paper {...props} elevation={0} />,
          }}
          options={{
            toolbar: false,
            paging: false,
            draggable: false,
          }}
          columns={[
            {
              title: 'Name',
              field: 'name',
              sorting: false,
            },
            {
              title: 'TIME',
              field: 'date',
              sorting: false,
            },
            { title: 'CONTACT NO', field: 'phone', sorting: false },
            { title: 'EMAIL ID', field: 'email', sorting: false },
          ]}
          data={
            [
              {
                name: 'Wasif',
                email: 'wasif.jameel1@gmail.com',
                phone: '+923006263173',
                date: new Date().toISOString(),
              },
              {
                name: 'Jameel',
                email: 'wasif.jameel@crowdbotics.com',
                phone: '+923006263173',
                date: new Date().toISOString(),
              },
              {
                name: 'W.J',
                email: 'wasifjameel@wasifjameel.com',
                phone: '+923006263173',
                date: new Date().toISOString(),
              },
            ] || []
          }
        />
      </GridItem>
    </GridContainer>
  );
}

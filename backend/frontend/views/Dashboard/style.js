import { makeStyles } from '@material-ui/core/styles';

export const styles = makeStyles(theme => ({
  title: {
    fontFamily: 'Avenir-heavy',
    fontSize: 20,
    paddingBottom: theme.spacing(2)
  },
  starColor: {
    color: '#F7B500',
    fontSize: 12
  },
  starCounts: {
    fontSize: 12
  },
  ProgressBarContainer: {
    marginBottom: theme.spacing(3)
  },
  allTimeText: {
    letterSpacing: '2px'
  },
  totalRating: {
    fontSize: '2rem'
  },
  upArrow: {
    color: '#00DBA0'
  },
  onGoingTripWrapper: {
    marginTop: '3rem'
  },
  textField: {
    marginBottom: theme.spacing(2)
  },
  card: {
    paddingLeft: '0px !important',
    paddingRight: '0px !important'
  },
  line: {
    border: '1px solid #dedede'
  },
  ToggleBtnContainer: {
    boxShadow: 'none !important',
    marginTop: '20px'
  },
  btnToggle: {
    border: '2px solid #dedede',
    borderRadius: '50px',
    width: '130px',
    color: '#808080b8',
    background: 'white',
    '&:hover': {
      background: 'linear-gradient(326.5deg, #00C8E6 7%, #00E6BA 75%)',
      border: '2px solid #dedede',
      color: 'white'
    }
  },
  ActiveToggleBtnPaypal: {
    borderRadius: '0px 50px 50px 00px',
    background: 'linear-gradient(326.5deg, #00C8E6 7%, #00E6BA 75%)',
    color: 'white',
    border: 'none'
  },
  ActiveToggleBtnCreditCard: {
    borderRadius: '50px 0px 0px 50px',
    color: 'white',
    background: 'linear-gradient(326.5deg, #00C8E6 7%, #00E6BA 75%)',
    border: 'none'
  },
  loaderContainer: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: 400
  },

  markerContainer: {
    position: 'absolute',
    width: 64,
    height: 64,
    userSelect: 'none',
    backgroundImage: `url('../../assets/images/cb-logo.png')`,
    background: '#46e1fd36',
    borderRadius: '50%',
    transform: 'translate(-50%, -50%)',
    padding: 40,
    '&:hover': {
      zIndex: 1
    }
  },

  markerInnerContainer: {
    position: 'absolute',
    background: 'rgba(70, 225, 253, 0.62)',
    borderRadius: '50%',
    transform: 'translate(-50%, -50%)'
  },

  carMarker: {
    width: 32,
    height: 32
  },
  mapContainer:{
    height: '400px',
    width: '100%'
  },
  marker_container: {
  position: 'absolute',
  width: 64,
  height: 64,
  userSelect: 'none',
  background: 'rgba(70,225,253,0.21)',
  borderRadius: '50%',
  transform: 'translate(-50%, -50%)',
  padding: 40,
},

marker_inner_container: {
  position: 'absolute',
  background: 'rgba(70, 225, 253, 0.62)',
  borderRadius: '50%',
  transform: 'translate(-50%, -50%)',
},

car_marker: {
  width: 32,
  height: 32,
},


}));

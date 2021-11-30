import { makeStyles } from '@material-ui/core/styles';

export const styles = makeStyles(theme => ({

  markerContainer: {
    position: 'absolute',
    width: 64,
    height: 64,
    userSelect: 'none',
    backgroundImage: url('../../assets/images/cb-logo.png'),
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
  }

}));

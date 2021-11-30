import React, { useEffect, useState } from 'react';
import GoogleMapReact from 'google-map-react';
import car from '../../assets/images/car.png';
import { GOOGLE_MAP_KEY } from '../../config/constants';
import { styles } from './style';



export default function OnGoingTripsMap (props) {

  const [center, setCenter] = useState({ lat: 40.7741834, lng: -111.9678745 });
  const [markers, setMarkers] = useState([]);
  const { locations } = props;

  const classes = styles();

  const Marker = () => <div className={classes.marker_container}>

    <div className={classes.marker_inner_container}>
      <img alt={'car marker'} className={classes.car_marker} src={car} />
    </div>
  </div>;



  useEffect(() => {

    setMarkers(locations);
    if (locations.length) {
      setCenter(locations[locations.length-1]);
    }
  }, [locations]);

  return (

    <div className={classes.mapContainer}>
      <GoogleMapReact
        yesIWantToUseGoogleMapApiInternals={false}
        bootstrapURLKeys={{ key: GOOGLE_MAP_KEY }}
        center={center}
        defaultZoom={12}
      >

        {
          markers.map((marker, index) => {

            return <Marker
              key={index}
              lat={marker.lat}
              lng={marker.lng}
            />;

          })
        }

      </GoogleMapReact>
    </div>
  );
}

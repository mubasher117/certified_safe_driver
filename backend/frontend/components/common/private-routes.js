import React from 'react';
import { Redirect, Route } from 'react-router-dom';
import { useSelector } from 'react-redux';

const PrivateRoute = ({ component: Component, ...rest }) => {
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated);
  console.log({ isAuthenticated });
  return (
    <Route
      {...rest}
      render={props => (isAuthenticated === true ? <Component {...props} /> : (
        <Redirect
          to={'/'}
        />
      ))}
    />
  );
};

export default PrivateRoute;

import React from "react";
import { Typography, Grid, Avatar } from "@material-ui/core";
import _ from "lodash";
import { Star } from "@material-ui/icons";
import styles from "./styles";

const UserIcon = ({ photo, first_name, last_name, username, rating }) => {
  const classes = styles();

  let name =
    !_.isEmpty(first_name) && !_.isEmpty(first_name)
      ? `${first_name} ${last_name}`
      : username;
  return (
    <Grid
      container
      direction="row"
      justify="flex-start"
      alignItems="center"
      className={`${classes.noWrap} ${classes.wContent}`}
    >
      {photo ? (
        <Avatar src={photo} />
      ) : (
        <Avatar>{username.substring(0, 1).toUpperCase()}</Avatar>
      )}
      <Grid className={classes.nameContainer}>
        <Typography variant="body1">
          {name}
          <br />
        </Typography>
        <Typography variant="caption" style={{ display: "flex" }}>
          <span>
            <Star className={classes.starIcon} />
          </span>
          <span>{Math.round(rating * 100) / 100}</span>
        </Typography>
      </Grid>
    </Grid>
  );
};

export default UserIcon;

import React from 'react';
// @material-ui/core components
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
// core components
import styles from 'assets/jss/material-dashboard-react/components/tableStyle.js';
import userImage from '../../assets/img/faces/marc.jpg';
import Avatar from '@material-ui/core/Avatar';
import Typography from '@material-ui/core/Typography';
import StarIcon from '@material-ui/icons/Star';

const useStyles = makeStyles(styles);

export default function CustomTable (props) {
  const classes = useStyles();
  const { tableHead, tableData } = props;
  return (
    <div className={classes.tableResponsive}>
      <Table className={classes.table}>
        {tableHead !== undefined ? (
          <TableHead>
            <TableRow className={classes.tableHeadRow}>
              {tableHead.map((prop, key) => {
                return (
                  <TableCell
                    className={classes.tableCell + ' ' + classes.tableHeadCell}
                    key={key}
                  >
                    {prop}
                  </TableCell>
                );
              })}
            </TableRow>
          </TableHead>
        ) : null}
        <TableBody>
          {tableData.map((prop, key) => {
            return (
              <TableRow key={key} className={classes.tableBodyRow}>
                <TableCell className={classes.tableCell} key={key}>
                  <div className={classes.logoImage}>
                    <Avatar className={classes.img} alt="user image" src={userImage} />
                    <div className={classes.userDetails}>
                      <Typography variant="button" className={classes.driverName}>{prop.name}</Typography>
                      <br />
                      <span>
                      <StarIcon className={classes.starColor} />
                        <Typography
                          className={classes.starCounts}
                          variant="subtitle1"
                          component="span">
                            5
                        </Typography>
                      </span>
                    </div>
                  </div>
                </TableCell>
                <TableCell className={classes.tableCell}>
                  {prop.tripCode}
                </TableCell>
                <TableCell className={classes.tableCell}>
                  {prop.time}
                </TableCell>
                <TableCell className={classes.tableCell}>
                  {prop.contactNumber}
                </TableCell>
                <TableCell className={classes.tableCell}>
                  {prop.email}
                </TableCell>
              </TableRow>
            );
          })}
        </TableBody>
      </Table>
    </div>
  );
}

CustomTable.defaultProps = {
  tableHeaderColor: "gray"
};

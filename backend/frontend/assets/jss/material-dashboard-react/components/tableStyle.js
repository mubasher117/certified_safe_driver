import {
  dangerColor,
  defaultFont,
  grayColor,
  infoColor,
  primaryColor,
  roseColor,
  successColor,
  warningColor
} from 'assets/jss/material-dashboard-react.js';

const tableStyle = theme => ({
  warningTableHeader: {
    color: warningColor[0]
  },
  primaryTableHeader: {
    color: primaryColor[0]
  },
  dangerTableHeader: {
    color: dangerColor[0]
  },
  successTableHeader: {
    color: successColor[0]
  },
  infoTableHeader: {
    color: infoColor[0]
  },
  roseTableHeader: {
    color: roseColor[0]
  },
  grayTableHeader: {
    color: grayColor[0]
  },
  table: {
    marginBottom: '0',
    width: '100%',
    maxWidth: '100%',
    backgroundColor: 'white',
    borderSpacing: '0',
    borderCollapse: 'collapse'
  },
  tableHeadCell: {
    color: "inherit",
    ...defaultFont,
    "&, &$tableCell": {
      fontSize: '1em',
      fontFamily: 'Avenir-Heavy',
      paddingBottom: '30px'
    }
  },
  tableCell: {
    ...defaultFont,
    lineHeight: '1.42857143',
    padding: '15px 32px',
    verticalAlign: 'middle',
    fontSize: '0.8125rem'
  },
  tableResponsive: {
    width: "100%",
    // marginTop: theme.spacing(3),
    overflowX: 'auto'
  },
  tableHeadRow: {
    height: '56px',
    color: 'inherit',
    display: 'table-row',
    outline: 'none',
    verticalAlign: 'middle'
  },
  tableBodyRow: {
    height: '48px',
    color: 'inherit',
    display: 'table-row',
    outline: 'none',
    verticalAlign: 'middle'
  },
  logoImage: {
    display: 'flex'
  },
  img: {
    width: 42,
    height: 42,
    verticalAlign: 'middle',
    border: '0'
  },
  userDetails: {
    marginLeft: theme.spacing(1)
  },
  starCounts: {
    fontSize: 12
  },
  starColor: {
    paddingTop: '1px',
    color: '#F7B500',
    fontSize: 12
  },
  driverName: {
    fontFamily: 'Avenir-HeavyOblique'
  }
});

export default tableStyle;

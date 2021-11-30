import React, { useEffect, useState } from 'react';
import MaterialTable from 'material-table';
import { Typography, Paper } from '@material-ui/core';
import { useDispatch, connect } from 'react-redux';
import moment from 'moment';
import { Edit, Add } from '@material-ui/icons';

import companiesListingStyles from './styles';
import { getCompanies, updateCompany, addCompany } from '../../actions/companiesActions';
import Modal from '../../components/Modal';
import EditForm from './EditForm';

function CompaniesListing({ companiesListing: { results }, history: { push }, isLoading = true }) {
  const classes = companiesListingStyles();
  const dispatch = useDispatch();

  const [isEdit, setEdit] = useState(false);
  const [editCompany, setEditCompany] = useState({});

  const handleEditClick = (event, rowData) => {
    setEdit(!isEdit);
    setEditCompany(rowData);
    event.stopPropagation();
  };

  const handleEditSubmit = ({ id, name }) => {
    console.log(id, name);

    if (id) dispatch(updateCompany({ id, name }));
    else dispatch(addCompany({ name }));
    setEdit(false);
  };

  const addNewRecord = event => {
    setEdit(!isEdit);
    event.stopPropagation();
  };

  useEffect(() => {
    dispatch(getCompanies());
  }, []);

  return (
    <>
      <Modal open={isEdit} handleClose={handleEditClick}>
        <EditForm onSubmit={handleEditSubmit} editCompany={editCompany} />
      </Modal>
      <Typography variant="h4" className={classes.mainHeading}>
        Companies List
      </Typography>
      <Add onClick={addNewRecord} />
      <MaterialTable
        options={{
          toolbar: false,
          paging: false,
          draggable: false,
          filtering: true,
        }}
        isLoading={isLoading}
        // onRowClick={handleRowClick}
        components={{
          Container: props => <Paper {...props} elevation={0} />,
        }}
        columns={[
          { title: 'ID', filterPlaceholder: 'ID', field: 'id', sorting: false, hideFilterIcon: true },
          {
            title: 'Name',
            field: 'name',
            filterPlaceholder: 'Name',
            sorting: false,
            hideFilterIcon: true,
          },
          {
            title: 'Updated',
            render: ({ updated }) => moment(updated).format('dddd, MMMM Do YYYY, h:mm:ss a'),
            field: 'updated',
            sorting: false,
            filtering: false,
          },
        ]}
        data={results}
        actions={[
          {
            icon: () => <Edit />,
            tooltip: 'Edit company',
            onClick: handleEditClick,
          },
        ]}
      />
    </>
  );
}

const mapStateToProps = state => {
  const { companiesListing, isLoading } = state.companies;

  return {
    companiesListing,
    isLoading,
  };
};

export default connect(mapStateToProps)(CompaniesListing);

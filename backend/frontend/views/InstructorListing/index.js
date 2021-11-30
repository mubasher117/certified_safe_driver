import React, { useEffect, useState } from 'react';
import MaterialTable from 'material-table';
import { Typography, Paper } from '@material-ui/core';
import { useDispatch, connect } from 'react-redux';
import moment from 'moment';
import { Edit, Add } from '@material-ui/icons';

import studentListingStyles from './styles';
import { getInstructor, updateInstructor, addInstructor } from '../../actions/instructorActions';
import { getCompanies } from '../../actions/companiesActions';
import Modal from '../../components/Modal';
import EditForm from './EditForm';

function InstructorListing({
  companiesListing: { results: companies },
  instructorListing: { results },
  history: { push },
  isLoading = true,
}) {
  const classes = studentListingStyles();
  const dispatch = useDispatch();
  const [isEdit, setEdit] = useState(false);
  const [editInstructor, setEditInstructor] = useState({});

  useEffect(() => {
    dispatch(getInstructor());
    dispatch(getCompanies());
  }, []);

  const handleRowClick = ({}, { id }) => {
    push(`/app/student-report/${id}`);
  };

  const handleEditClick = (event, rowData) => {
    setEdit(!isEdit);
    setEditInstructor(rowData);
    event.stopPropagation();
  };

  const handleEditSubmit = ({ id, username, first_name, last_name, phone, email, company, password }) => {
    // console.log('id in handleEditSubmit', id, !isEmpty(id));
    if (id) dispatch(updateInstructor({ id, username, first_name, last_name, phone, email, info: { company } }));
    else
      dispatch(
        addInstructor({
          username,
          first_name,
          last_name,
          phone,
          email,
          password,
          info: { company },
          is_instructor: true,
        }),
      );
    setEdit(false);
  };

  const addNewRecord = event => {
    setEdit(!isEdit);
    setEditInstructor({});
    event.stopPropagation();
  };

  return (
    <>
      <Modal open={isEdit} handleClose={handleEditClick}>
        <EditForm
          onSubmit={handleEditSubmit}
          editInstructor={{
            id: editInstructor.id,
            username: editInstructor.username,
            first_name: editInstructor.first_name,
            last_name: editInstructor.last_name,
            phone: editInstructor.phone,
            email: editInstructor.email,
            company: editInstructor.info && editInstructor.info.company ? editInstructor.info.company.id : '',
          }}
          companies={companies}
        />
      </Modal>
      <Typography variant="h4" className={classes.mainHeading}>
        Instructor List
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
            title: 'Username',
            filterPlaceholder: 'Username',
            field: 'username',
            sorting: false,
            hideFilterIcon: true,
          },
          {
            title: 'Full Name',
            filterPlaceholder: 'Full Name',
            field: 'first_name last_name',
            sorting: false,
            hideFilterIcon: true,
            render: ({ first_name, last_name }) => `${first_name} ${last_name}`,
          },
          {
            title: 'Email',
            filterPlaceholder: 'Email',
            field: 'email',
            sorting: false,
            hideFilterIcon: true,
          },
          {
            title: 'Phone',
            filterPlaceholder: 'Phone',
            field: 'phone',
            sorting: false,
            hideFilterIcon: true,
          },
          {
            title: 'Company',
            filterPlaceholder: 'Company',
            field: 'info.company.name',
            sorting: false,
            hideFilterIcon: true,
          },
          {
            title: 'Joining Date',
            render: ({ date_joined }) => moment(date_joined).format('DD-MM-YY'),
            field: 'date_joined',
            sorting: false,
            filtering: false,
          },
        ]}
        data={results}
        actions={[
          {
            icon: () => <Edit />,
            tooltip: 'Edit Student',
            onClick: handleEditClick,
          },
        ]}
      />
    </>
  );
}

const mapStateToProps = state => {
  const { instructorListing, isLoading } = state.instructor;
  const { companiesListing, isLoading: companiesLoading } = state.companies;

  return {
    instructorListing,
    isLoading,
    companiesListing,
    companiesLoading,
  };
};

export default connect(mapStateToProps)(InstructorListing);

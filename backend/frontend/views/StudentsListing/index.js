import React, { useEffect, useState } from 'react';
import MaterialTable from 'material-table';
import { Typography, Paper } from '@material-ui/core';
import { useDispatch, connect } from 'react-redux';
import moment from 'moment';
import { Edit, Add } from '@material-ui/icons';

import studentListingStyles from './styles';
import { getStudents, updateStudent, addStudent } from '../../actions/studentsActions';
import { getCompanies } from '../../actions/companiesActions';
import Modal from '../../components/Modal';
import EditForm from './EditForm';

function StudentsListing({
  companiesListing: { results: companies },
  studentsListing: { results },
  history: { push },
  isLoading = true,
}) {
  const classes = studentListingStyles();
  const dispatch = useDispatch();
  const [isEdit, setEdit] = useState(false);
  const [editStudent, setEditStudent] = useState({});

  useEffect(() => {
    dispatch(getStudents());
    dispatch(getCompanies());
  }, []);

  const handleRowClick = ({}, { id }) => {
    push(`/app/student-detailed-report/${id}`);
    toast('adasdsd');
  };

  const handleEditClick = (event, rowData) => {
    setEdit(!isEdit);
    setEditStudent(rowData);
    event.stopPropagation();
  };

  const handleEditSubmit = ({ id, username, first_name, last_name, phone, email, company, password }) => {
    console.log('info', company);
    setEdit(false);
    // let currentCompany = _.find(companies, { id: company });
    if (id) dispatch(updateStudent({ id, username, first_name, last_name, phone, email, info: { company } }));
    else dispatch(addStudent({ username, first_name, last_name, phone, email, password, info: { company } }));
  };

  const addNewRecord = event => {
    setEdit(!isEdit);
    setEditStudent({});
    event.stopPropagation();
  };

  return (
    <>
      <Modal open={isEdit} handleClose={handleEditClick}>
        <EditForm
          onSubmit={handleEditSubmit}
          editStudent={{
            id: editStudent.id,
            username: editStudent.username,
            first_name: editStudent.first_name,
            last_name: editStudent.last_name,
            phone: editStudent.phone,
            email: editStudent.email,
            company: editStudent.info && editStudent.info.company ? editStudent.info.company.id : '',
          }}
          companies={companies}
        />
      </Modal>
      <Typography variant="h4" className={classes.mainHeading}>
        Students List
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
        onRowClick={handleRowClick}
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
            render: ({ first_name, last_name }) => `${first_name} ${last_name}`,
            customFilterAndSearch: (term, { first_name, last_name }) =>
              `${first_name} ${last_name}`.toLowerCase().includes(term.toLowerCase()),
            hideFilterIcon: true,
          },
          {
            title: 'Email',
            filterPlaceholder: 'Email',
            field: 'email',
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
            title: 'Phone',
            filterPlaceholder: 'Phone',
            field: 'phone',
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
  const { studentsListing, isLoading } = state.students;
  const { companiesListing, isLoading: companiesLoading } = state.companies;

  return {
    studentsListing,
    isLoading,
    companiesListing,
    companiesLoading,
  };
};

export default connect(mapStateToProps)(StudentsListing);

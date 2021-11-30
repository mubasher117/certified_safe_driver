// core components/views for Admin layout
import DashboardPage from '../views/Dashboard/Dashboard.js';
import TableList from '../views/TableList/TableList.js';
import CompaniesListing from '../views/CompaniesListing';
import StudentsListing from '../views/StudentsListing';
import InstructorListing from '../views/InstructorListing';
import StudentReport from '../views/StudentReport';

const dashboardRoutes = [
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardPage,
  },
  {
    path: '/Reports',
    name: 'Reports',
    component: StudentReport,
  },
  {
    path: '/companies',
    name: 'Companies',
    component: CompaniesListing,
  },
  {
    path: '/students',
    name: 'Students',
    component: StudentsListing,
  },
  {
    path: '/instructor',
    name: 'Instructor',
    component: InstructorListing,
  },
];

export default dashboardRoutes;

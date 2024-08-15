import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import StudentHome from './components/StudentHome';
import FacultyHome from './components/FacultyHome';
import Meeting from './components/Meeting';
import Attendance from './components/Attendance';

function AppRoutes() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/student/home" element={<StudentHome />} />
        <Route path="/faculty/home" element={<FacultyHome />} />
        <Route path="/meeting/:id" element={<Meeting />} />
        <Route path="/attendance" element={<Attendance />} />
      </Routes>
    </Router>
  );
}

export default AppRoutes;

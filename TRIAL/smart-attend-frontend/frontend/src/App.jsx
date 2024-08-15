import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import StudentHome from './components/StudentHome';
import FacultyHome from './components/FacultyHome';
import MeetingScheduler from './components/MeetingScheduler';
import Attendance from './components/Attendance';
import './App.css';

const App = () => (
  <Router>
    <Switch>
      <Route path="/" exact component={Login} />
      <Route path="/student-home" component={StudentHome} />
      <Route path="/faculty-home" component={FacultyHome} />
      <Route path="/schedule-meeting" component={MeetingScheduler} />
      <Route path="/attendance" component={Attendance} />
    </Switch>
  </Router>
);

export default App;

// src/components/StudentHome.jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const StudentHome = () => {
  const [meetings, setMeetings] = useState([]);
  const [attendance, setAttendance] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const meetingsResponse = await axios.get('/api/student/meetings');
      const attendanceResponse = await axios.get('/api/student/attendance');
      setMeetings(meetingsResponse.data);
      setAttendance(attendanceResponse.data);
    };
    fetchData();
  }, []);

  return (
    <div>
      <h2>Student Home</h2>
      <h3>Scheduled Meetings</h3>
      <ul>
        {meetings.map((meeting) => (
          <li key={meeting.id}>{meeting.title} - {meeting.date}</li>
        ))}
      </ul>
      <h3>Attendance Records</h3>
      <ul>
        {attendance.map((record) => (
          <li key={record.id}>{record.course} - {record.status}</li>
        ))}
      </ul>
    </div>
  );
};

export default StudentHome;

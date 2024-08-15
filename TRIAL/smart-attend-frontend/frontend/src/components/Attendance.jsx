// src/components/Attendance.jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Attendance = () => {
  const [attendance, setAttendance] = useState([]);

  useEffect(() => {
    const fetchAttendance = async () => {
      const response = await axios.get('/api/faculty/attendance');
      setAttendance(response.data);
    };
    fetchAttendance();
  }, []);

  return (
    <div>
      <h2>Attendance</h2>
      <ul>
        {attendance.map((record) => (
          <li key={record.id}>{record.student} - {record.status}</li>
        ))}
      </ul>
    </div>
  );
};

export default Attendance;

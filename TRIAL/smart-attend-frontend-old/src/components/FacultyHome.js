import React, { useState, useEffect } from 'react';
import { fetchCourses, fetchMeetings, fetchStudents, scheduleMeeting } from '../utils/api';

const FacultyHome = () => {
  const [courses, setCourses] = useState([]);
  const [meetings, setMeetings] = useState([]);
  const [students, setStudents] = useState([]);
  const [newMeeting, setNewMeeting] = useState({ topic: '', startTime: '' });

  useEffect(() => {
    // Fetch data on mount
    fetchCourses().then(setCourses);
    fetchMeetings().then(setMeetings);
    fetchStudents().then(setStudents);
  }, []);

  const handleScheduleMeeting = async () => {
    const success = await scheduleMeeting(newMeeting);
    if (success) {
      alert('Meeting scheduled successfully');
      setMeetings([...meetings, newMeeting]);
    } else {
      alert('Failed to schedule meeting');
    }
  };

  return (
    <div>
      <h2>Faculty Home</h2>
      <section>
        <h3>Schedule Meeting</h3>
        <input
          type="text"
          placeholder="Meeting Topic"
          value={newMeeting.topic}
          onChange={(e) => setNewMeeting({ ...newMeeting, topic: e.target.value })}
        />
        <input
          type="datetime-local"
          value={newMeeting.startTime}
          onChange={(e) => setNewMeeting({ ...newMeeting, startTime: e.target.value })}
        />
        <button onClick={handleScheduleMeeting}>Schedule Meeting</button>
      </section>
      <section>
        <h3>Registered Students</h3>
        <ul>
          {students.map((student) => (
            <li key={student.id}>{student.name}</li>
          ))}
        </ul>
      </section>
      <section>
        <h3>Scheduled Meetings</h3>
        <ul>
          {meetings.map((meeting) => (
            <li key={meeting.id}>{meeting.topic} - {meeting.startTime}</li>
          ))}
        </ul>
      </section>
      <section>
        <h3>Manage Attendance</h3>
        {/* Add attendance management here */}
      </section>
    </div>
  );
};

export default FacultyHome;

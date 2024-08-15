// src/components/MeetingScheduler.jsx
import React, { useState } from 'react';
import axios from 'axios';

const MeetingScheduler = () => {
  const [title, setTitle] = useState('');
  const [date, setDate] = useState('');

  const scheduleMeeting = async () => {
    try {
      await axios.post('/api/faculty/schedule-meeting', { title, date });
      alert('Meeting scheduled');
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Schedule Meeting</h2>
      <input type="text" placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} />
      <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
      <button onClick={scheduleMeeting}>Schedule</button>
    </div>
  );
};

export default MeetingScheduler;

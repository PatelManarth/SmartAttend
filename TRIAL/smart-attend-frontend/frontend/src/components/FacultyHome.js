// src/components/FacultyHome.jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const FacultyHome = () => {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const coursesResponse = await axios.get('/api/faculty/courses');
      setCourses(coursesResponse.data);
    };
    fetchData();
  }, []);

  return (
    <div>
      <h2>Faculty Home</h2>
      <h3>Courses</h3>
      <ul>
        {courses.map((course) => (
          <li key={course.id}>{course.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default FacultyHome;


import React from 'react';

function VideoGrid({ participants }) {
  return (
    <div className="video-grid">
      {participants.map((participant, index) => (
        <video key={index} id={`participant-${index}`} />
      ))}
    </div>
  );
}

export default VideoGrid;

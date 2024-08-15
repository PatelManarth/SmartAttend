import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import uitoolkit from '@zoom/videosdk-ui-toolkit';
import { getVideoSDKJWT } from '../utils/zoomUtils';

function Meeting() {
  const { id } = useParams();
  const sessionContainerRef = React.useRef(null);

  useEffect(() => {
    const startMeeting = async () => {
      const role = sessionStorage.getItem('ROLE');
      const config = await getVideoSDKJWT(id, role);
      uitoolkit.joinSession(sessionContainerRef.current, config);

      uitoolkit.onSessionClosed(() => {
        console.log('Session closed');
        uitoolkit.closeSession(sessionContainerRef.current);
      });
    };

    startMeeting();
  }, [id]);

  return <div id="sessionContainer" ref={sessionContainerRef}></div>;
}

export default Meeting;

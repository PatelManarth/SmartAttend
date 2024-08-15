export async function getVideoSDKJWT(meetingId, role) {
  const response = await fetch('/zoom-auth', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ meetingId, role }),
  });

  const data = await response.json();
  return {
    videoSDKJWT: data.signature,
    sessionName: meetingId,
    userName: 'User',
    sessionPasscode: '123',
    features: ['video', 'audio', 'settings', 'users', 'chat', 'share'],
  };
}

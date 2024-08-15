export async function fetchFromBackend(endpoint, method = 'GET', body = null) {
    const response = await fetch(`http://localhost:8000/${endpoint}`, {
      method,
      headers: {
        'Content-Type': 'application/json',
      },
      body: body ? JSON.stringify(body) : null,
    });
    
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
  
    return await response.json();
  }
  
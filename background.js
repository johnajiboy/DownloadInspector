chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  if (message.action === 'checkMalicious') {
    const downloadLink = message.downloadLink;

    fetch('http://localhost:5000/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ downloadLink }),
    })
    .then(response => response.json())
    .then(data => {
      const isMalicious = data.is_malicious;
      sendResponse({ isMalicious });
      })
      .catch(error => {
        console.error(error);
        sendResponse({ error: 'An error occurred while checking the link.' });
      });

    return true;
  }
});
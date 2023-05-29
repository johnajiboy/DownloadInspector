chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.type === 'inspectDownloadLink') {
      const xhr = new XMLHttpRequest();
      xhr.open('POST', 'http://localhost:5000/download');
      xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
          const response = JSON.parse(xhr.responseText);
          sendResponse(response.result);
        }
      };
      xhr.send(`link=${encodeURIComponent(request.link)}`);
      return true;
    }
  });
  
document.addEventListener('mousedown', function (event) {
  if (event.button === 2) {
    const downloadLink = event.target.href;
    if (downloadLink) {
      chrome.runtime.sendMessage({
        type: 'inspectDownloadLink',
        link: downloadLink
      }, function (response) {
        if (response === 'malicious') {
          event.preventDefault();
          alert('This file is malicious. Download aborted.');
        }
      });
    }
  }
});

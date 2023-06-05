document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('linkForm');
  const input = document.getElementById('link');
  const loadingMessage = document.getElementById('loadingMessage');

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    const downloadLink = input.value;

    showLoadingMessage();

    chrome.runtime.sendMessage({ action: 'checkMalicious', downloadLink }, function (response) {
      const isMalicious = response.isMalicious;
      hideLoadingMessage();

      if (isMalicious) {
        alert('The download link is malicious.');
      } else {
        alert('The download link is safe.');
      }
    });
  });

  function showLoadingMessage() {
    loadingMessage.style.display = 'block';
  }

  function hideLoadingMessage() {
    loadingMessage.style.display = 'none';
  }
});

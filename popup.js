// popup.js

document.addEventListener('DOMContentLoaded', function () {
  const linkForm = document.getElementById('linkForm');
  linkForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const downloadLink = document.getElementById('link').value;
    checkMalicious(downloadLink);
  });
});

function checkMalicious(downloadLink) {
  const apiUrl = 'https://www.filescan.io/api/scan/url';

  fetch(apiUrl, {
    method: 'POST',
    headers: {
      'accept': 'application/json',
      'x-apikey': "fQvcUbP0deGU6dToPidZCBDg8p1t7yXrMNDes49k",
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: `url=${encodeURIComponent(downloadLink)}`
  })
    .then(response => response.json())
    .then(data => {
      const id = data.flow_id;
      url = `https://www.filescan.io/api/scan/${id}/report?filter=finalVerdict&sorting=string&other=emulationGraph`
      return fetch(url, {
        method: 'GET',
        headers: {
          'x-apikey': "fQvcUbP0deGU6dToPidZCBDg8p1t7yXrMNDes49k",
          'Content-Type': 'application/json'
        }
      });
    })
    .then(response => response.json())
    .then(data => {
      let isMalicious = false;
      const reports = Array.isArray(data.reports) ? data.reports : []; // Convert data.reports to an array
      for (const report of reports) {
        if (report.finalVerdict && report.finalVerdict.verdict === "MALICIOUS") {
          isMalicious = true;
          break; // Exit the loop if a malicious verdict is found
    }
  }
      displayResult(downloadLink, isMalicious);
    })
    .catch(error => console.error(error));
}

function displayResult(link, isMalicious) {
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = `
    <p>The link <strong>${link}</strong> is ${isMalicious ? 'malicious' : 'safe'}.</p>
  `;
}

document.addEventListener('DOMContentLoaded', function () {
    const loadingMessage = document.getElementById('loadingMessage');
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        showLoadingMessage();
});
function showLoadingMessage() {
    loadingMessage.style.display = 'block';
  }
});
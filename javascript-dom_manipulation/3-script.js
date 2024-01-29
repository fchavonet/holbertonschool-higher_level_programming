document.addEventListener('DOMContentLoaded', function () {
  const toggleHeader = document.querySelector('#toggle_header');

  toggleHeader.addEventListener('click', function () {
    const header = document.querySelector('header');
    header.classList.toggle('red');
    header.classList.toggle('green');
  });
});

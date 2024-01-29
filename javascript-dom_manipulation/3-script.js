document.addEventListener('DOMContentLoaded', function () {
  const header = document.querySelector('header');

  header.addEventListener('click', function () {
    header.classList.toggle('red');
    header.classList.toggle('green');
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const redHeader = document.querySelector("#red_header");

  redHeader.addEventListener('click', function () {
    const header = document.querySelector('header');
    header.style.color = '#FF0000';
  });
});

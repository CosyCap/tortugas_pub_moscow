const slider = document.querySelector('.slider');

function slide() {
  slider.style.transform = 'translateX(-100%)';
  setTimeout(() => {
    const firstSlide = slider.firstElementChild;
    slider.appendChild(firstSlide);
    slider.style.transition = 'none';
    slider.style.transform = 'translateX(0)';
    setTimeout(() => {
      slider.style.transition = 'transform 0.5s ease-in-out';
    });
  }, 500);
}

setInterval(slide, 3000); // Измените интервал смены слайдов по необходимости

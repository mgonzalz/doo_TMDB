document.addEventListener('DOMContentLoaded', function () {
    const miListaContainer = document.querySelector('#mi-lista-container');
    const movieCount = document.querySelectorAll('#mi-lista .movie-card').length;
    const prevButton = document.getElementById('mi-lista-prev');
    const nextButton = document.getElementById('mi-lista-next');

    if (movieCount <= 4) {
        prevButton.classList.add('hidden');
        nextButton.classList.add('hidden');
    } else {
        prevButton.classList.remove('hidden');
        nextButton.classList.remove('hidden');
    }
});

function scrollCarousel(id, direction) {
    const carousel = document.getElementById(id);
    const scrollAmount = carousel.offsetWidth / 2;
    carousel.scrollBy({ left: direction * scrollAmount, behavior: 'smooth' });
}

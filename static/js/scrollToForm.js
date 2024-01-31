document.addEventListener('DOMContentLoaded', function() {
    var successMessage = document.querySelector('.alert-success');
    if (successMessage) {
        var bookSection = document.querySelector('.book_section');
        if (bookSection) {
            window.scrollTo({
                top: bookSection.offsetTop,
                behavior: 'smooth'
            });
        }
    }
});

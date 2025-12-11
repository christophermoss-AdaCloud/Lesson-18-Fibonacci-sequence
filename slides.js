// Slide Navigation JavaScript
let currentSlide = 1;
const totalSlides = 8;

// Show the first slide on load
document.addEventListener('DOMContentLoaded', function() {
    showSlide(currentSlide);
    
    // Add keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowRight' || e.key === ' ') {
            nextSlide();
        } else if (e.key === 'ArrowLeft') {
            prevSlide();
        }
    });
});

function showSlide(n) {
    // Hide all slides
    const slides = document.querySelectorAll('.slide');
    slides.forEach(slide => {
        slide.classList.remove('active');
    });
    
    // Ensure n is within bounds
    if (n > totalSlides) {
        currentSlide = totalSlides;
    } else if (n < 1) {
        currentSlide = 1;
    } else {
        currentSlide = n;
    }
    
    // Show the current slide
    const currentSlideElement = document.getElementById(`slide-${currentSlide}`);
    if (currentSlideElement) {
        currentSlideElement.classList.add('active');
    }
    
    // Scroll to top of slide
    window.scrollTo(0, 0);
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        showSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        showSlide(currentSlide - 1);
    }
}

// Allow clicking on slide number to jump to a specific slide
document.querySelectorAll('.slide-number').forEach((element, index) => {
    element.style.cursor = 'pointer';
    element.addEventListener('click', function() {
        const slideNum = parseInt(this.textContent.match(/\d+/)[0]);
        if (slideNum) {
            showSlide(slideNum);
        }
    });
});

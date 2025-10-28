// --- Image Slider ---
let slideIndex = 1;
// We call showSlides() to display the first slide when the page loads
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls (the dots)
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("slide");
  let dots = document.getElementsByClassName("dot");
  
  // This logic loops the slider back to the start or end
  if (n > slides.length) { slideIndex = 1 }
  if (n < 1) { slideIndex = slides.length }
  
  // Hide all slides
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  
  // Deactivate all dots
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }

  // Show the current slide and activate the current dot
  // This 'if' statement prevents errors if the page doesn't have a slider
  if (slides.length > 0) {
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
  }
}

// --- Optional: Automatic Slideshow ---
// To enable, uncomment the line below. It will change the image every 5 seconds.
setInterval(function() { plusSlides(1); }, 5000);

// --- Removed Image Slider JS (as it's replaced) ---
// You can keep or delete the previous slider functions (plusSlides, currentSlide, showSlides)
// as they are no longer used by the index.html but won't cause harm.

// --- Parallax Scroll Effect for Hero Section ---
document.addEventListener("DOMContentLoaded", function() {
    const heroLeft = document.querySelector('.hero-left');
    const heroRight = document.querySelector('.hero-right');

    if (heroLeft && heroRight) { // Ensure elements exist
        const heroLeftSpeed = parseFloat(heroLeft.dataset.speed || 0.8);
        const heroRightSpeed = parseFloat(heroRight.dataset.speed || 0.9);

        function updateParallax() {
            const scrollPos = window.scrollY;
            const heroHeight = document.querySelector('.hero-split-container').offsetHeight;

            // Only apply parallax if within the hero section's scroll range
            if (scrollPos < heroHeight) {
                heroLeft.style.transform = `translateY(${scrollPos * (1 - heroLeftSpeed)}px)`;
                heroRight.style.backgroundPositionY = `${scrollPos * (1 - heroRightSpeed)}px`;
            } else {
                // Reset or stop moving when out of hero section range
                heroLeft.style.transform = `translateY(0px)`;
                heroRight.style.backgroundPositionY = `center`;
            }
        }

        // Add scroll event listener
        window.addEventListener('scroll', updateParallax);
        // Also call it once on load to set initial position
        updateParallax();
    }
});

// --- (Optional) If you have other JS code, it goes here ---
// For example, if you uncommented the auto-slideshow, it would be here.
// But since the slider is removed, that part is now irrelevant.


window.addEventListener("scroll", function(){
  const heroRight = document.querySelector(".hero-right");
  let scrollY = window.scrollY;
  heroRight.style.transform = `translateY(${scrollY * 0.2}px)`;
});


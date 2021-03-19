document.addEventListener('DOMContentLoaded', function() {
    // carousel
    var elems = document.querySelectorAll('.carousel');
    var instances = M.Carousel.init(elems, {
        fullWidth: true,
        indicators: true,
    });
    console.log("DEBUG: index carousel worked");
    // slider
    var elems = document.querySelectorAll('.slider');
    var instances = M.Slider.init(elems);
    console.log("DEBUG: slider worked");
    // parallax
    var elems = document.querySelectorAll('.parallax');
    var instances = M.Parallax.init(elems);
    console.log("DEBUG: paralax worked");
});
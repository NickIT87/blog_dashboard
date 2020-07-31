M.AutoInit();
// error "options is not defined",delete options var argument from instances
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.carousel');
    var instances = M.Carousel.init(elems);
    console.log("Event listener worked");
});
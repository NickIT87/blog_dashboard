// header navbar
/*
document.addEventListener('DOMContentLoaded', function() {
    console.log("DEBUG: AutoInit, .sidenav");
    //M.AutoInit();
    // explicit init
    var elems = document.querySelectorAll('.sidenav');
    M.Sidenav.init(elems);
});
*/

$(document).ready(function(){
    console.log("DEBUG: JQUERY AutoInit");
    M.AutoInit();
    //$('.sidenav').sidenav();
});


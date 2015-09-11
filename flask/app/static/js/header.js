$(function(){
  var shrinkHeader = 150;
  $(window).scroll(function() {
    var scroll = getCurrentScroll();
      if ( scroll >= shrinkHeader ) {
           $('header').addClass('shrink');
           $('.produkter').fadeOut();
           $('nav').addClass('shrink');
           //$('nav a').addClass('shrink');
        }
        else {
            $('header').removeClass('shrink');
            $('.produkter').fadeIn();
            $('nav').removeClass('shrink');
            $('nav a').removeClass('shrink');
        }
  });
function getCurrentScroll() {
    return window.pageYOffset || document.documentElement.scrollTop;
    }
});

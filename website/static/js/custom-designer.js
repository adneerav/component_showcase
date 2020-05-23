$(function() {
    var header = $(".header");
    $(window).scroll(function() {    
        var scroll = $(window).scrollTop();
    
        if (scroll >= 200) {
            header.removeClass('header').addClass("header-sticky");
        } else {
            header.removeClass("header-sticky").addClass('header');
        }
    });
});
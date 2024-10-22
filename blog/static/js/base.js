$(window).scroll(function() {
    var height = $(window).scrollTop();
    if (height > 300) {
        $('#back_to_top').fadeIn(1000);
    } else {
        $('#back_to_top').fadeOut(1000);
    }
});
$(document).ready(function() {
    $("#back_to_top").click(function(event) {
        event.preventDefault();
        $("html, body").animate({ scrollTop: 0 }, 1000);
        return false;
    });

});
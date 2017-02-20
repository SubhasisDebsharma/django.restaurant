function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

$(document).ready(function() {
    $("div.blog-post").hover(
        function() {
            $(this).find("div.content-hide").slideToggle("fast");
        },
        function() {
            $(this).find("div.content-hide").slideToggle("fast");
        }
    );

    $('.flexslider').flexslider({
        prevText: '',
        nextText: ''
    });

    $('.testimonails-slider').flexslider({
        animation: 'slide',
        slideshowSpeed: 5000,
        prevText: '',
        nextText: '',
        controlNav: false
    });

    $('#Container').mixItUp();

    $(".fancybox").fancybox();
});


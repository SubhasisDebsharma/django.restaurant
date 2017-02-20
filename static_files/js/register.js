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
    $('input').blur(function() {
        var $this = $(this);
        if ($this.val())
            $this.addClass('used');
        else
            $this.removeClass('used');
    });

    var $ripples = $('.ripples');

    $ripples.on('click.Ripples', function(e) {

        var $this = $(this);
        var $offset = $this.parent().offset();
        var $circle = $this.find('.ripplesCircle');

        var x = e.pageX - $offset.left;
        var y = e.pageY - $offset.top;

        $circle.css({
            top: y + 'px',
            left: x + 'px'
        });

        $this.addClass('is-active');

    });

    $ripples.on('animationend webkitAnimationEnd mozAnimationEnd oanimationend MSAnimationEnd', function(e) {
    	$(this).removeClass('is-active');
    });


    $(".register").on("click", function() {
        if(($(".password").val() != $(".rePassword").val()) || $(".password").val().length < 4){
            alert("Type and retype password correctly... (minmum password length 4)")
        }
        else{
            $(".button").attr('type','submit').click()
        }
    })

    $("#formid").submit(function(event){
        event.preventDefault()
        $.ajax({
            url: $("#formid").attr("action"),
            method: "POST",
            data: "name=" + $(".name").val() + "&username=" + $(".username").val() + "&password=" + $(".password").val() + "&email=" + $(".email").val() + "&phone=" + $(".phone").val() + "&address=" + $(".address").val(),
            dataType: "json",
            success: function(data) {
                console.log(data)
                window.location = data.redirectUrl;
            },
            error: function(data) {
                alert(data.responseJSON.status)
            }
        });
    })
});
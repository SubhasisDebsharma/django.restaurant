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

$(document).ready(function(){

    $(".out-for-delivery").on("click",function(){
        element = $(this);
        $.ajax({
            url: "/Kitchen/updateOrderStatusReady/",
            method: "post",
            data: {
                "orderid": element.parent().find(".orderid").val()
            },
            success: function(data) {
                console.log(element.html())
                element.hide()
                element.parent().find(".delivered").show()
                element.parent().find(".status").html(data)
            },
            error: function() {
                alert("Failed ...");
            }
        })
    })

    $(".delivered").on("click",function(){
        element = $(this);
        $.ajax({
            url: "/Kitchen/updateOrderStatusDelivered/",
            method: "post",
            data: {
                "orderid": element.parent().find(".orderid").val()
            },
            success: function(data) {
                element.hide()
                element.parent().find(".out-for-delivery").hide()
                element.parent().find(".status").html(data)
            },
            error: function() {
                alert("Failed ...");
            }
        })
    })

    $(".clickablerow").on("click", function() {
        var orderId = $(this).attr("data-href");
        $(".table-orders [data-order-details-id='"+orderId+"']").toggle();
    })
})
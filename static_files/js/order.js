var cart = {}

$(document).ready(function() {
    $(".quantity-container .plus").on("click", function() {
        var quantity = $(this).parent().find(".quantity");

        quantity.html(~~quantity.html() + 1);

        $(".checkout .quantity").html(~~$(".checkout .quantity").html() + 1);

        addOrderToCart($(this).closest(".portfolio-item"))
    });

    $(".quantity-container .minus").on("click", function() {
        var quantity = $(this).parent().find(".quantity");

        if (quantity.html() !== "0") {
            quantity.html(~~quantity.html() - 1);
            $(".checkout .quantity").html(~~$(".checkout .quantity").html() - 1);
        }

        addOrderToCart($(this).closest(".portfolio-item"))
    });

    $(".checkout").on("click", function() {
        var orderItems = $(".portfolio-item").filter(function() {
            return ~~$(this).find(".quantity").html() > 0
        })

        var orderData = [];

        $.each(orderItems, function(index, orderItem) {
            var menuId      = $(orderItem).find(".menuid").val(),
                quantity    = $(orderItem).find(".quantity").html();

            orderData.push({"menuId": menuId, "quantity": quantity})
        })

        console.log({"orderData": JSON.stringify(orderData)})

        $.ajax({
            url: "/Order/placeOrder/",
            method: "post",
            data: {"orderData": JSON.stringify(orderData)},
            success: function(data) {
                alert(data);

                $(".portfolio-item .quantity").html("0");
                $(".checkout .quantity").html("0");

                cart = [];
                populateCart();
            },
            error: function() {
                alert("Error Placing Order");
            }
        })
    })
})

function addOrderToCart(item) {
    var name = item.find(".menu-name").html()
    var quantity = item.find(".quantity").html()
    var price = item.find(".price").html()
    var imgUrl = item.find(".menu-img").attr("src")

    cart[name] = [quantity, price, imgUrl]

    console.log(cart)

    populateCart()
}

function populateCart() {
    $(".cart-container .dropdown-menu li:not(.divider, .checkout-li)").remove()

    $.each(cart, function(name, val) {
        if (val[0] !== "0") {
            html =  '<li class="clearfix">' +
                        '<img src="' + val[2] + '">' +
                        '<span class="item-name">' + name + '</span>' +
                        '<span class="item-price">' + val[1] + '</span>' +
                        '<span class="item-quantity">Quantity: ' + val[0] + '</span>' +
                    '</li>';

            $(".cart-container .dropdown-menu").prepend(html)
        }
        else {
            delete cart[name]
        }
    })

    if (Object.keys(cart).length == 0) {
        $(".cart-container .dropdown-menu").prepend('<li class="no-items">No Items in cart</li>');
    }

    $(".cart .quantity").html(Object.keys(cart).length)
}
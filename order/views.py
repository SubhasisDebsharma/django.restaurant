from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import json
import logging

from menu.models import MenuDetails
from order.models import OrderDetails, OrderItemDetails
from user.models import UserDetails

logger = logging.getLogger(__name__)

def index(request):
    userid = request.session.get("userid")

    if userid is None:
        context = {
            "menus": MenuDetails.objects.all(),
            "categories": MenuDetails.objects.order_by().values("menu_category").distinct(),
            "userid": None
        }

        return render(
            template_name="order/index.html",
            request=request,
            context=context
        )
    else:
        user = UserDetails.objects.get(userid=userid)

        if user.user_type == UserDetails.USER_TYPE_CUSTOMER:
            context = {
                "menus": MenuDetails.objects.all(),
                "categories": MenuDetails.objects.order_by().values("menu_category").distinct(),
                "userid": userid
            }

            return render(
                template_name = "order/index.html",
                request = request,
                context = context
            )
        elif user.user_type == UserDetails.USER_TYPE_OFFICE:
            return HttpResponseRedirect("/Kitchen/")

def placeOrder(request):
    orderData = json.loads(request.POST.get("orderData"))
    amount = 0.0

    user = UserDetails.objects.get(
        userid = request.session.get("userid")
    )

    orderDetails = OrderDetails(
        userid=user,
        status=OrderDetails.ORDER_STATUS_PREPARING
    )

    orderDetails.save()

    # logger.warning(order)
    # logger.warning(order.orderid)

    for order in orderData:
        menuDetails = MenuDetails.objects.get(menuid = order["menuId"])
        amount += menuDetails.price * int(order["quantity"])

        orderItem = OrderItemDetails(
            orderid = orderDetails,
            menuid = menuDetails,
            price = menuDetails.price * int(order["quantity"]),
            quantity = order["quantity"]
        )

        orderItem.save()

    return HttpResponse("Order Placed")

def myOrders(request):
    orders = OrderDetails.objects.filter(userid=request.session.get("userid")).order_by('-create_date')
    itemsPerOrder = []
    for order in orders:
        itemsPerOrder.append(OrderItemDetails.objects.filter(orderid = order.orderid))
    context = {
        "itemsPerOrder" : itemsPerOrder
    }
    return render(request=request, template_name="order/myorders.html", context=context)
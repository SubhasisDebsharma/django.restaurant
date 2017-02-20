from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from error import HttpError500
from order.models import OrderDetails, UserDetails, OrderItemDetails
import json
import logging
from django.db.models import Count

logger = logging.getLogger(__name__)

def index(request):
    userid = request.session['userid']
    if UserDetails.objects.get(userid = userid).user_type == UserDetails.USER_TYPE_OFFICE:
        orders = OrderDetails.objects.all().order_by('-create_date')
        orderitems = []
        for order in orders:
            orderitems.append(OrderItemDetails.objects.filter(orderid = order.orderid))
        context = {
            "orderitems": orderitems
        }
        return render(template_name="kitchen/index.html", request=request, context=context)
    else:
        return HttpResponseRedirect("/Order/")

def updateOrderStatusReady(request):
    try:
        orderid = json.loads(request.POST.get("orderid"))
        orderItem = OrderDetails.objects.get(orderid = orderid)
        orderItem.status = OrderDetails.ORDER_STATUS_READY
        orderItem.save(update_fields=["status"])
        return HttpResponse(OrderDetails.objects.get(orderid = orderid).status)
    except:
        return HttpError500()

def updateOrderStatusDelivered(request):
    try:
        orderid = json.loads(request.POST.get("orderid"))
        orderItem = OrderDetails.objects.get(orderid=orderid)
        orderItem.status = OrderDetails.ORDER_STATUS_DELIVERED
        orderItem.save(update_fields=["status"])
        return HttpResponse(OrderDetails.objects.get(orderid=orderid).status)
    except:
        return HttpError500()

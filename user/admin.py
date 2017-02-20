from django.contrib import admin
from menu.models import MenuDetails
from user.models import UserDetails
from order.models import OrderDetails, OrderItemDetails

admin.site.register(UserDetails)
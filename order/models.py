from django.db import models
from django.utils import timezone

from menu.models import MenuDetails
from user.models import UserDetails

class OrderDetails(models.Model):
	ORDER_STATUS_PREPARING = 'preparing'
	ORDER_STATUS_READY = 'ready'
	ORDER_STATUS_DELIVERED = 'delivered'

	order_status = (
		(ORDER_STATUS_PREPARING, 'Preparing'),
		(ORDER_STATUS_READY, 'Ready'),
		(ORDER_STATUS_DELIVERED, 'Delivered')
	)

	orderid = models.AutoField(primary_key=True)
	userid = models.ForeignKey(UserDetails, on_delete=models.PROTECT)
	create_date = models.DateTimeField(default=timezone.now, blank=True)
	status = models.CharField(max_length=20, choices=order_status, default=ORDER_STATUS_PREPARING)

	class Meta:
		db_table = 'order_details'
		
class OrderItemDetails(models.Model):
	order_item_id = models.AutoField(primary_key=True)
	orderid = models.ForeignKey(OrderDetails, on_delete=models.PROTECT)
	menuid = models.ForeignKey(MenuDetails, on_delete=models.PROTECT)
	quantity = models.IntegerField()
	price = models.FloatField()

	class Meta:
		db_table = 'order_item_details'
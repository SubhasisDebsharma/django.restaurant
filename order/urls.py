from django.conf.urls import url

from order import views

urlpatterns = [
    url(r'$^', views.index),
    url(r'^placeOrder/', views.placeOrder),
    url(r'^MyOrders/', views.myOrders),
]
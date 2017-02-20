from django.conf.urls import url

from kitchen import views

urlpatterns = [
    url(r'$^', views.index),
    url(r'^updateOrderStatusReady/', views.updateOrderStatusReady),
    url(r'^updateOrderStatusDelivered/', views.updateOrderStatusDelivered),
]
from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^Login/', views.login),
    url(r'^Register/', views.register),
    url(r'^Logout/', views.logout),
    url(r'^authenticate/', views.authenticate),
    url(r'^newRegister/', views.newRegister),
]
from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^cust_home$', views.cust_index),
    url(r'^driver_home$', views.driver_index),
    url(r'^cust_register$', views.cust_register),
    url(r'^cust_login$', views.cust_login),
    url(r'^driver_register$', views.driver_register),
    url(r'^driver_login$', views.driver_login),
    url(r'^success$', views.success),
    url(r'^driver_success$', views.driver_success),
    url(r'^logout$', views.logout),
]
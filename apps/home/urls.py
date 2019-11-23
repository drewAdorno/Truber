from django.conf.urls import url
from . import views

# /home/searchDrivers           takes currentUsers coords
# /home/address_to_coords       takes currentUsers submitted address and converts to coords
 
urlpatterns = [
    url(r'^$', views.index),
    url(r'^driver$', views.driver_home),
    url(r'^searchDrivers/(?P<lat>-?\d+\.\d+)_(?P<lng>-?\d+\.\d+)$', views.searchDrivers),
    url(r'^aToC$', views.address_to_coords),
    url(r'^check_response$', views.check_response),
    url(r'^dropOff$', views.dropOff_address),
    url(r'^driver_dropoff$', views.driver_dropoff),
    url(r'^driver_online/(?P<lat>-?\d+\.\d+)_(?P<lng>-?\d+\.\d+)$', views.driver_online),
    url(r'^driver_fnr$', views.driver_find_new_requests),
    url(r'^driver_accepted$', views.driver_accepted),
    url(r'^driver_updateLoc/(?P<lat>-?\d+\.\d+)_(?P<lng>-?\d+\.\d+)$', views.driver_updateLoc),
    url(r'^driver_offline$', views.driver_offline),
    url(r'^updateLoc$', views.update_loc),
    url(r'^driver_finished$', views.driver_finished),

]
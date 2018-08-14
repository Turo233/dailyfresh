from django.conf.urls import url
from . import views

urlpatterns = [
    url('^pay/$', views.order, name='pay'),
    url('^order_handle/$', views.order_handle, name='handle'),
    url('^confirm_(?P<order_id>[^/]+)/$', views.order_confirm, name='confirm'),
]
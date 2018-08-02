from django.conf.urls import url
from . import views

urlpatterns = [
    url('^pay/$', views.order),
    url('^order_handle/$', views.order_handle),
    url('^conifrm_(\d+)/$', views.order_confirm),
]
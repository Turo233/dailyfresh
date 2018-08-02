from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^login/$', views.login),
    url(r'^checkuserid/$', views.checkuserid),
    url(r'^login_handle/$', views.login_handle),
    url(r'^info/$', views.info),
    url(r'^site/$', views.site),
    url(r'^order_(\d+)/$', views.order),
    url(r'^logout/$', views.logout)
    # url(r'^site_addinfo/$', views.site_addinfo)
]
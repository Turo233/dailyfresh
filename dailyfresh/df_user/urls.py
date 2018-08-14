from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^register_handle/$', views.register_handle, name='reghandle'),
    url(r'^login/$', views.login, name='login'),
    url(r'^checkuserid/$', views.checkuserid, name='check'),
    url(r'^login_handle/$', views.login_handle, name='lohandle'),
    url(r'^info/$', views.info, name='info'),
    url(r'^site/$', views.site, name='site'),
    url(r'^order_(?P<pageNum>[^/]+)/$', views.order, name='order'),
    url(r'^logout/$', views.logout, name='logout')
    # url(r'^site_addinfo/$', views.site_addinfo)
]
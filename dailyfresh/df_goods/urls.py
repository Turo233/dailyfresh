from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='home'),
    url(r'^list_(?P<typeNum>[^_]+)_(?P<pageNum>[^_]+)_(?P<sortNum>[^/]+)/$', views.list, name='list'),
    url(r'^(?P<goods_id>[^/]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.MySearchView(), name='search'),
]
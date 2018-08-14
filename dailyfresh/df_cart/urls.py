from django.conf.urls import url
from . import views

# 配置路由
urlpatterns = [
    url(r'^$', views.cart, name='cart'),
    url(r'^add_(?P<good_id>[^_]+)_(?P<count>[^/]+)/$', views.cart_add, name='add'),
    url(r'^edit_(?P<cart_id>[^_]+)_(?P<count>[^/]+)/$', views.cart_edit, name='edit'),
    url(r'^delete_(?P<cart_id>[^/]+)/$', views.cart_delete, name='delete'),
    url(r'^query_cart/$', views.query_cart, name='query'),
]
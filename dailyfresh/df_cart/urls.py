from django.conf.urls import url
from . import views

# 配置路由
urlpatterns = [
    url(r'^add_(\d+)_(\d+)/$', views.cart_add),
    url(r'^edit_(\d+)_(\d+)/$', views.cart_edit),
    url(r'^delete_(\d+)/$', views.cart_delete),
    url(r'^query_cart/$', views.query_cart),
    url(r'^', views.cart),
]
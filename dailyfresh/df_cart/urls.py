from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cart),
    url(r'^add_(\d+)_(\d+)/$', views.cart_add),
    url(r'^edit_(\d+)_(\d+)/$', views.cart_edit),
    url(r'^delete_(\d+)/$', views.cart_delete),
]
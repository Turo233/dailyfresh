from django.contrib import admin
from .models import CartInfo
# Register your models here.

@admin.register(CartInfo)
class CartInfo_admin(admin.ModelAdmin):
    list_display = ['users', 'goods', 'count']


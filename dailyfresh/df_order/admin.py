from django.contrib import admin
from .models import Order
from .models import Order_detail
from df_user.models import UserInfo
# Register your models here.
class Order_detail_info(admin.TabularInline):
    model = Order_detail

@admin.register(Order)
class Order_admin(admin.ModelAdmin):
    inlines = [Order_detail_info]

    list_display = ["order_id", "order_owner", "order_date",
                    "Ispay", "order_total", "order_address"]


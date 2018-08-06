from django.contrib import admin
from .models import TypeInfo
from .models import GoodsInfo
# Register your models here.
@admin.register(TypeInfo)
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_title']

@admin.register(GoodsInfo)
class Goods_info_admin(admin.ModelAdmin):
    list_display = ['id', 'goods_title', 'goods_price',
                    'goods_unit','goods_click',
                    'goods_stock','goods_type']
    list_per_page = 15


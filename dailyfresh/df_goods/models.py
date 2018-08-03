from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class TypeInfo(models.Model):
    type_title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.type_title

class GoodsInfo(models.Model):
    goods_title = models.CharField(max_length=80)
    goods_pic = models.ImageField(upload_to='df_goods')
    goods_price = models.DecimalField(max_digits=5, decimal_places=2)
    goods_unit = models.CharField(max_length=30, default="500g")
    goods_click = models.IntegerField()
    goods_intru = models.CharField(max_length=200)
    goods_stock = models.IntegerField()
    goods_detail = HTMLField()
    goods_type = models.ForeignKey(TypeInfo)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.goods_title
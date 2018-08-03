from django.db import models

# Create your models here.

# 定义两个模型类，Order存储一个订单的整体内容，是谁的，什么日期等
class Order(models.Model):
    order_id = models.CharField(max_length=20, primary_key=True)
    order_owner = models.ForeignKey('df_user.UserInfo')
    order_date = models.DateTimeField(auto_now=True)
    Ispay = models.BooleanField(default=False)
    order_total = models.DecimalField(max_digits=6, decimal_places=2)
    order_address = models.CharField(max_length=150)

# 这个是与Order相关联，负责其具体的订单商品内容。
class Order_detail(models.Model):
    order_detail = models.ForeignKey(Order)
    order_goods = models.ForeignKey('df_goods.GoodsInfo')
    order_price = models.DecimalField(max_digits=5, decimal_places=2)
    order_count = models.IntegerField()
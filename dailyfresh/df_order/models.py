from django.db import models

# Create your models here.

class Order(models.Model):
    order_id = models.CharField(max_length=20, primary_key=True)
    order_owner = models.ForeignKey('df_user.UserInfo')
    order_date = models.DateTimeField(auto_now=True)
    Ispay = models.BooleanField(default=False)
    order_total = models.DecimalField(max_digits=6, decimal_places=2)
    order_address = models.CharField(max_length=150)

class Order_detail(models.Model):
    order_detail = models.ForeignKey(Order)
    order_goods = models.ForeignKey('df_goods.GoodsInfo')
    order_price = models.DecimalField(max_digits=5, decimal_places=2)
    order_count = models.IntegerField()
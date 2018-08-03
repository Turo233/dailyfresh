from django.db import models

# Create your models here.

# 商品和用户多对多关系，通过cartInfo表来维护其中的关系。
class CartInfo(models.Model):
    # 关联用户
    users = models.ForeignKey('df_user.UserInfo')
    # 关联商品
    goods = models.ForeignKey('df_goods.GoodsInfo')
    # 计算购买数量
    count = models.IntegerField()
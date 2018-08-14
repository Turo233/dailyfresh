from django.shortcuts import render
from django.http import request, JsonResponse, HttpResponseRedirect
from df_cart.models import CartInfo
from df_user.models import UserInfo
from .models import *
from datetime import datetime
from decimal import Decimal
from django.db import transaction
from df_user import user_decorater
from django.urls import reverse
# Create your views here.

# 通过get的方式获取订单信息并进行存储
def order(request):
    user_info = UserInfo.objects.get(id=int(request.session['userid']))
    get = request.GET
    carts_id = get.getlist('carts_id')
    cart_id_list = [int(id) for id in carts_id]
    # id__in 获取数据库中id在列表中的对象
    carts_info = CartInfo.objects.filter(id__in=cart_id_list)
    content = {
        'title':'提交订单',
        'user_page':1,
        'carts_info':carts_info,
        'user_info':user_info,
        'carts_id':carts_id,
    }
    return render(request, 'df_order/place_order.html', content)

# 装饰器创建事务
@transaction.atomic()
def order_handle(request):
    # 创建事务原点
    tran_origin = transaction.savepoint()

    carts_list = []
    carts_list = request.POST['carts_id']
    try:
        # 创建订单对象
        order = Order()
        now = datetime.now()
        user_id = request.session['userid']
        # strftime() 将时间以字符串格式表示
        order.order_id = '{}{}'.format(now.strftime('%Y%m%d%H%M%S'), user_id)
        order.order_owner_id = user_id
        order.order_date = now
        order.order_address = request.POST.get('order_address')
        order.order_total = 0
        order.save()
        # 查看每一条订单
        # 因为传值是通过 ‘，’ 拼接，但如果只有一个值会split失败
        try:
            carts_id = [int(each) for each in carts_list.split(',')]
        except:
            carts_id = int(carts_list[0])

        order_cost = 0
        for each_id in carts_id:
            cart_info = CartInfo.objects.get(id=each_id)
            goods = cart_info.goods
            # 查看货物库存
            if goods.goods_stock >= cart_info.count:
                # 减少库存
                goods.goods_stock -= cart_info.count
                goods.save()
                # 创建订单详情
                detail = Order_detail()
                detail.order_detail = order
                detail.order_goods_id = goods.id
                # 计算单价和数量以计算总价
                each_count = cart_info.count
                detail.order_count = each_count
                each_price = goods.goods_price
                detail.order_price = each_price
                detail.save()
                order_cost += each_count * each_price
                cart_info.delete()
            else:
                transaction.savepoint_rollback(tran_origin)
                return HttpResponseRedirect(reverse('cart:cart'))
        #保存总价格
        order.order_total = order_cost + 10
        order.save()
        transaction.savepoint_commit(tran_origin)
    except Exception as e:
        print(e)
        transaction.savepoint_rollback(tran_origin)
    return HttpResponseRedirect(reverse('user:order', args=(1,)))

# 假装支付。。。
def order_confirm(request, order_id):
    tran_origin = transaction.savepoint()
    try:
        order = Order.objects.get(order_id=order_id)
        order.Ispay = 1
        order.save()
        return JsonResponse({'status':1})
    except Exception as e:
        print(3)
        transaction.savepoint_rollback(tran_origin)
        return JsonResponse({'status':0})
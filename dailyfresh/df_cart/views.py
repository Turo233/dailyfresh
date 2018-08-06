from django.shortcuts import render, redirect
from django.http import request, JsonResponse
from df_user import user_decorater
from .models import CartInfo
from df_goods.models import GoodsInfo
# Create your views here.

# 购物车页面加载处理
@user_decorater.login
def cart(request):
    user_id = request.session['userid']
    # 从购物车数据表拿取全部当前用户的购物车信息
    cart_goods = CartInfo.objects.filter(users=user_id)
    content = {
        'title':'购物车',
        'user_page':1,
        'cart_goods':cart_goods,
    }
    return render(request, 'df_cart/cart.html', content)


# 详情页和列表页的商品添加处理
@user_decorater.login
def cart_add(request, good_id, count):
    user_id = request.session['userid']
    good_id = int(good_id)
    count = int(count)
    cart = CartInfo.objects.filter(users_id=user_id, goods_id=int(good_id))
    # 如果购物车存在此商品信息，进行叠加处理
    if len(cart) >= 1:
        cart = cart[0]
        cart.count += count
    else:
        cart = CartInfo()
        cart.users_id = user_id
        cart.goods_id = good_id
        cart.count = count
    cart.save()
    # 根据是动态处理还是直接跳转进行分离处理
    if request.is_ajax():
        count = CartInfo.objects.filter(users_id=user_id).count()
        return JsonResponse({'count':count, 'cart':cart.id})
    else:
        return redirect('/cart/')


# 对购物车的内容修改进行处理
def cart_edit(request, cart_id, count):
    try:
        cart_info = CartInfo.objects.get(id=int(cart_id))
        new_count = cart_info.count = count
        cart_info.save()
        data = {'ok':0}
    except:
        data = {'ok':count}
    return JsonResponse(data)

# 购物车商品删除处理
def cart_delete(request, cart_id):
    try:
        cart_info = CartInfo.objects.get(id=int(cart_id))
        cart_info.delete()
        data = {'status':1}
    except:
        data = {'status':0}
    return JsonResponse(data)

# 在其他页面显示购物车中内容数量
def query_cart(request):
    if request.session.has_key('userid'):
        userid = request.session['userid']
        count_info = CartInfo.objects.filter(users_id=userid).count()
    else:
        count_info = '未登录'
    return JsonResponse({'data':count_info})


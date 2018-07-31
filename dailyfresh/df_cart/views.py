from django.shortcuts import render, redirect
from django.http import request, JsonResponse
from df_user import user_decorater
from .models import CartInfo
from df_goods.models import GoodsInfo
# Create your views here.

@user_decorater.login
def cart(request):
    user_id = request.session['userid']
    cart_goods = CartInfo.objects.filter(users=user_id)
    content = {
        'title':'购物车',
        'user_page':1,
        'cart_goods':cart_goods,
    }
    return render(request, 'df_cart/cart.html', content)

@user_decorater.login
def cart_add(request, good_id, count):
    user_id = request.session['userid']
    good_id = int(good_id)
    count = int(count)
    cart = CartInfo.objects.filter(users_id=user_id, goods_id=int(good_id))
    if len(cart) >= 1:
        cart = cart[0]
        cart.count += count
    else:
        cart = CartInfo()
        cart.users_id = user_id
        cart.goods_id = good_id
        cart.count = count
    cart.save()
    if request.is_ajax():
        count = CartInfo.objects.filter(users_id=user_id).count()
        return JsonResponse({'count':count})
    else:
        return redirect('/cart')


def cart_edit(request, cart_id, count):
    try:
        cart_info = CartInfo.objects.get(id=int(cart_id))
        new_count = cart_info.count = count
        cart_info.save()
        data = {'ok':0}
    except:
        data = {'ok':count}
    return JsonResponse(data)

def cart_delete(request, cart_id):
    try:
        cart_info = CartInfo.objects.get(id=int(cart_id))
        cart_info.delete()
        data = {'status':1}
    except:
        data = {'status':0}
    return JsonResponse(data)


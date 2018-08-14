from django.shortcuts import render, redirect
from hashlib import sha1
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import UserInfo
from . import user_decorater
from df_goods.models import GoodsInfo
from df_order.models import Order
from django.core.paginator import Paginator
from django.urls import reverse

# Create your views here.

def register(request):
    return render(request, 'df_user/register.html')


def register_handle(request):
    # 接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    # 判断两个密码是否一致
    if upwd != upwd2:
        return HttpResponseRedirect(reverse('user:register'))
    # 密码加密
    s1 = sha1()
    s1.update(upwd.encode('utf-8'))
    upwd3 = s1.hexdigest()
    # 创建对象存储用户信息
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    #注册成功, 转到登录页面
    return HttpResponseRedirect(reverse('user:login'))

# 检查用户名是否已存在
def checkuserid(request):
    username = request.POST.get("uname")
    usercount = UserInfo.objects.filter(uname = username).count()
    return JsonResponse({"count":usercount})

# 查看用户是否保存cookie值，将cookie中保存的用户名信息填入登录页面
def login(request):
    uname = request.COOKIES.get('uname','')
    # uname_error和upwd_error 是与登录界面的js代码做一个交互
    content = {"title": "用户登录", 'uname_error': 0, 'upwd_error': 0, 'uname':uname, 'namevalue': uname}
    return render(request, 'df_user/login.html', content)

# 注销清空session并返回主页
def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('goods:index'))

# 对登录信息进行验证
def login_handle(request):
    post = request.POST
    uname = post.get("username")
    upwd = post.get("pwd")
    ucheck = post.get("checkbox", 0)
    content = {"title": "用户登录", 'uname_error': 0, 'upwd_error': 0, 'ucheck': 0, 'namevalue': uname, 'pwdvalue': upwd}
    # 从数据库中获取可能不存在的值使用filter， 使用get会报错
    users = UserInfo.objects.filter(uname=uname)
    if len(users) == 1:
        # 密码加密验证
        s1 = sha1()
        s1.update(upwd.encode("utf-8"))
        if s1.hexdigest() == users[0].upwd:
            url = request.COOKIES.get('url', '/')
            # 密码验证成功，判断是否需要存cookie，使用HttpResponseRedirect
            red = HttpResponseRedirect(url)
            if ucheck:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            # 存id是以后查这个用户的时候可以根据这个id拿用户数据
            request.session['userid'] = users[0].id
            # 用到uname的地方很多, 每次都在uid中拿的话效率太低
            request.session['uname'] = uname
            return red
        else:
            content['upwd_error'] = 1
            return render(request, 'df_user/login.html', content)
    else:
        content['uname_error'] = 1
        return render(request, 'df_user/login.html', content)

    return render(request, 'df_user/login.html', content)

# 用户中心界面处理，包含用户信息显示以及对商品的最近浏览
@user_decorater.login
def info(request):
    lasted_view = request.COOKIES.get('goods_ids', '')
    views_list = []
    if lasted_view != '':
        good_list = lasted_view.split(',')
        # good_list = map(lambda x: int(x), good_list)
        for each in good_list:
            good_info = GoodsInfo.objects.get(id=int(each))
            views_list.append(good_info)

    uid = request.session.get('userid')
    uname = request.session.get('uname')
    user = UserInfo.objects.get(id=uid)

    content = {'title':'用户中心',
               'user_page': 1,
               'uname': uname,
               'uphone': user.uphone,
               'uaddress': user.uaddress,
               'good_info': views_list}
    return render(request, 'df_user/user_center_info.html', content)

# 订单页内容，根据订单日期和支付情况进行排序显示
@user_decorater.login
def order(request, pageNum):
    user_id = request.session.get("userid")
    orders = Order.objects.filter(order_owner_id=user_id).order_by('-order_date').order_by('Ispay')
    # 使用paginator 对内容进行分页显示
    paginator = Paginator(orders, 2)
    page = paginator.page(int(pageNum))

    content = {'title':'全部订单',
               'user_page':1,
               'orders':orders,
               'paginator':paginator,
               'page':page}
    return render(request, 'df_user/user_center_order.html', content)

# 用户地址页面，通过重新载入的方式导入信息
@user_decorater.login
def site(request):
    user = UserInfo.objects.get(id=request.session.get('userid'))
    if request.method == 'POST':
        post = request.POST
        user.urecive = post.get('reciver', 'xxx')
        user.uaddress = post.get('detial_address', 'xxx省 xxx市 xxx街道')
        user.uphone = post.get('phone_num', 'xxx xxx xxxxx')
        user.upost = post.get('stamp_no')
        user.save()
        # phone_num = phone_num[0:3] + 'xxxx' + phone_num[7:11]
    content = {'title':'用户中心', 'user':user, 'user_page':1}
    return render(request, 'df_user/user_center_site.html', content)

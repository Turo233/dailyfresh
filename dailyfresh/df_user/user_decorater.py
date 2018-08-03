from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# 用来验证是否登录的装饰器
def login(func):
    def login_warper(request, *args, **kwargs):
        if request.session.has_key('userid'):
            return func(request, *args, **kwargs)
        else:
            # 跳转到登录页面，如果登陆成功则跳转回原访问网页
            red = HttpResponseRedirect('/user/login')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_warper
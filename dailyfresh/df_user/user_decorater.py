from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def login(func):
    def login_warper(request, *args, **kwargs):
        if request.session.has_key('userid'):
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_warper
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib.auth.views import login


def login_view(request):
    """用户登录"""
    context = {}
    if request.method == 'POST':
        login(request)
        if not request.user.is_authenticated():
            context['error'] = 'error'

    return render(request, 'blogs/index.html', context)


def logout_view(request):
    """注销用户"""
    logout(request)
    return render(request, 'blogs/index.html')


def register(request):
    """注册"""
    if request.method == 'POST':
        data = request.POST
        print(data['username'])

    return render(request, 'users/register.html')

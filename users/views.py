from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import login as django_login_view
from django.contrib.auth.models import UserManager
from .models import User


def login_view(request):
    """用户登录"""
    context = {}
    if request.method == 'POST':
        django_login_view(request)
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
        user_manager = UserManager()
        username_ = data['username']
        email_ = data['email']
        password_ = data['password']
        nickname_ = data['nickname']

        # new_user = user_manager.create_user(username_, email_, password_, nickname =nickname_)
        new_user = User()
        new_user.username = username_
        new_user.nickname = nickname_
        new_user.email = email_
        new_user.set_password(password_)
        new_user.save()

        print(new_user)
        authenticated_user = authenticate(username = username_, password = password_)
        login(request, authenticated_user)
        return HttpResponseRedirect(reverse('blogs:index'))

    return render(request, 'users/register.html')

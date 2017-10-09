from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import login as django_login_view
# from django.contrib.auth.models import UserManager
from .models import User


def login_view(request):
    """用户登录"""
    context = {}
    if request.method == 'POST':
        django_login_view(request)
        if not request.user.is_authenticated():
            context['error'] = 'error'

    return HttpResponseRedirect(reverse('blogs:index'))


def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('blogs:index'))


def register(request):
    """注册"""
    if request.method == 'POST':
        data = request.POST
        password_ = data['password']
        nickname_ = data['nickname']

        new_user = User()
        new_user.username = data['username']
        new_user.email = data['email']
        new_user.set_password(password_)
        new_user.nickname = nickname_
        new_user.city = data['city']
        new_user.site = data['site']
        new_user.avatar = data['avatar']
        new_user.save()

        # user_manager = UserManager()
        # new_user = user_manager.create_user(username_, email_, password_, nickname=nickname_)

        authenticated_user = authenticate(username=nickname_, password=password_)
        login(request, authenticated_user)
        return HttpResponseRedirect(reverse('blogs:index'))

    return render(request, 'users/register.html')


def edit_info(request):
    """修改信息"""
    user = request.user
    if request.method == 'POST':
        data = request.POST
        # password_ = data['password']
        nickname_ = data['nickname']

        user.username = data['username']
        user.email = data['email']
        # user.set_password(password_)
        user.nickname = nickname_
        user.city = data['city']
        user.site = data['site']
        user.avatar = data['avatar']
        user.save()

        return HttpResponseRedirect(reverse('users:info'))
    else:
        context = {"user": user}
        return render(request, 'users/edit_info.html')


def info(request):
    """用户信息"""
    user = request.user

    context = {"user": user}
    return render(request, 'users/info.html', context)

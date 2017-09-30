from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib.auth.views import login

def login_view(request):
    """用户登录"""
    if request.method == 'POST':
    	login(request)
    	return HttpResponseRedirect(reverse('blogs:index'))

    return render(request, 'blogs:index', context)
    

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('blogs:index'))

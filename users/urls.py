from django.conf import settings
from django.conf.urls import url, include
# from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^login$', views.login_view, name='login_view'),
    url(r'^logout$', views.logout_view, name='logout_view'),
]
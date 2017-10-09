from django.conf import settings
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^login$', views.login_view, name='login_view'),
    url(r'^logout$', views.logout_view, name='logout_view'),
    url(r'^register$', views.register, name='register'),
    url(r'^info$', views.info, name='info'),
    url(r'^edit_info$', views.edit_info, name='edit_info'),
]
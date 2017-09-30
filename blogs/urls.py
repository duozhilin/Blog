from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),
    url(r'^posts/(?P<username>\w+)/$', views.user_index, name='user_index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

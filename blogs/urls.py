from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # topic
    url(r'^topics$', views.topics, name='topics'),
    url(r'^new_topic$', views.new_topic, name='new_topic'),
    url(r'^delete_topic/(?P<topic_id>\d+)/$', views.delete_topic, name='delete_topic'),

    # post
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),
    url(r'^posts/(?P<username>\w+)/$', views.user_index, name='user_index'),
    url(r'^posts/(?P<username>\w+)/list$', views.posts_list, name='posts_list'),
    url(r'^topic/(?P<topic_id>\d+)/posts$', views.posts, name='posts'),
    url(r'^new_post$', views.new_post, name='new_post'),
    url(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),
    url(r'^delete_post/(?P<post_id>\d+)/$', views.delete_post, name='delete_post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

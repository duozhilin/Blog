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

    # tag
    url(r'^tags$', views.tags, name='tags'),
    url(r'^new_tag$', views.new_tag, name='new_tag'),
    url(r'^delete_tag/(?P<tag_id>\d+)/$', views.delete_tag, name='delete_tag'),

    # post
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),
    url(r'^posts/(?P<username>\w+)/$', views.posts_user, name='posts_user'),
    url(r'^posts/topic/(?P<topic_id>\d+)/$', views.posts_topic, name='posts_topic'),
    url(r'^posts/tag/(?P<tag_id>\d+)/$', views.posts_tag, name='posts_tag'),
    url(r'^posts/manager$', views.posts_manger, name='posts_manager'),
    url(r'^new_post$', views.new_post, name='new_post'),
    url(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),
    url(r'^delete_post/(?P<post_id>\d+)/$', views.delete_post, name='delete_post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

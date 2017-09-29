from django.contrib import admin

from blogs.models import Topic, Post#, Tag

admin.site.register(Topic)
admin.site.register(Post)
# admin.site.register(Tag)
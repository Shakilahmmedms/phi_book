from django.contrib import admin
from .models import Posts, Comment,Like
# Register your models here.
admin.site.register(Posts)
admin.site.register(Comment)
admin.site.register(Like)
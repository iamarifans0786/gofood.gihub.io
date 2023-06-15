from django.contrib import admin
from blog.models import blogs,comments
# Register your models here.


class News_blogs_edit(admin.ModelAdmin):
    list_display=[
        'person_name',
        'date',
        'blog_title',
        'blog_img',
        'detail',
    ] 
admin.site.register(blogs,News_blogs_edit)

class Reaction_comments(admin.ModelAdmin):
    list_display=[
        'post',
        'name',
        'comment_body',
    ] 
admin.site.register(comments,Reaction_comments)
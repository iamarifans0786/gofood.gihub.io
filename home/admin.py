from django.contrib import admin
from home.models import home_menu,home_news_blogs,happy_customers

# Register your models here.

class home_menu_edit(admin.ModelAdmin):
    list_display=[
        'dis_name',
        'dis_detail',
        'dis_img',
     ] 

admin.site.register(home_menu,home_menu_edit)

class home_news_blogs_edit(admin.ModelAdmin):
    list_display=[
        'person_name',
        'date',
        'heading',
        'blog_img',
     ] 

admin.site.register(home_news_blogs,home_news_blogs_edit)

class happy_customers_edit(admin.ModelAdmin):
    list_display=[
        'person_name',
        'person_img',
        'address',
        'comments',
     ] 

admin.site.register(happy_customers,happy_customers_edit)




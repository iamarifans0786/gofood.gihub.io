from django.contrib import admin
from menu.models import pasta,pizza,burgur,desserts,breakfast,lunch,dinner,healty

# Register your models here

@admin.register(burgur)
class Admin(admin.ModelAdmin):
    list_display=[
        'dis_name',
        'detail',
        'price'
    ]

@admin.register(pizza)
class Admin(admin.ModelAdmin):
    list_display=[
        'dis_name',
        'detail',
        'price'
    ]

@admin.register(pasta)
class Admin(admin.ModelAdmin):
    list_display=[
        'dis_name',
        'detail',
        'price'
    ]

@admin.register(desserts)
class Admin(admin.ModelAdmin):
    list_display=[
        'dis_name',
        'detail',
        'price'
    ]

@admin.register(breakfast)
class Admin(admin.ModelAdmin):
    list_display=[
        'dis_name',
        'dis_img',
        'detail',
        'price'
    ]   

@admin.register(lunch)
class Admin(admin.ModelAdmin):
    list_display=[
        'dis_name',
        'dis_img',
        'detail',
        'price'
    ] 

@admin.register(dinner)
class Admin(admin.ModelAdmin):
    list_display=[
        'dis_name',
        'dis_img',
        'detail',
        'price'
    ]         

@admin.register(healty)
class Admin(admin.ModelAdmin):
    list_display=[
        'dis_name',
        'dis_img',
        'detail',
        'price'
    ]     
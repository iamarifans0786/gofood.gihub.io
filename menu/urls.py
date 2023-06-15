
from django.contrib import admin
from django.urls import path
from menu import views

urlpatterns = [
path("fastfood/",views.fastfood,name="fastfood"),
path("mainfood/",views.mainfood,name="mainfood"),

]

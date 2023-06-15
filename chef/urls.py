from django.contrib import admin
from django.urls import path
from chef import views

urlpatterns = [
    path("",views.chef,name="chef"),

]

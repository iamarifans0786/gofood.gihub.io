
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path("",views.home, name="homepage"),
path("register/",views.register, name="registration"),
path("login/",views.login_fun, name="login"),
]

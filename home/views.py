from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import home_menu, home_news_blogs, happy_customers

# Create your views here.


def register(request):
    if request.method == "POST":
        frist_name = request.POST.get("fristname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create(
            email=email,
            first_name=frist_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        return HttpResponse("user Created")
    return render(request, "registration.html")


def login_fun(request):
    error=""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            error="Invalid user"
    return render(request, "login.html",{
        "message":error
    })


def home(request):
    if request.user.is_authenticated:
        home_menu_data = home_menu.objects.all()
        home_blogs_data = home_news_blogs.objects.all()
        home_happy_cutommers_data = happy_customers.objects.all()
        data = {
            "home_menu_data": home_menu_data,
            "home_blogs_data": home_blogs_data,
            "home_happy_cutommers_data": home_happy_cutommers_data,
        }
        return render(request, "home.html", data)
    return HttpResponseRedirect("/login")

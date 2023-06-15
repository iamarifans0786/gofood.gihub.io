from django.contrib import admin
from django.urls import path
from testimonial import views

urlpatterns = [
path("",views.testimonial, name="testimonial"),
]

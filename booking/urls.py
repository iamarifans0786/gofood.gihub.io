from django.contrib import admin
from django.urls import path
from booking import views

urlpatterns = [
    path("",views.booking_details,name="booking"),
    # path("book/",views.book_conform,name="book-conform"),
    
]

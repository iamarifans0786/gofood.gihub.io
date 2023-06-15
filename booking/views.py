from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from booking.models import booking

# Create your views here.


def booking_details(request):
    if request.method == "POST":
        name = request.POST.get("full_name")
        email = request.POST.get("email_id")
        phone = request.POST.get("phone_no")
        date = request.POST.get("bookig_date")
        time = request.POST.get("bookig_time")
        guests = request.POST.get("total_guests")
        message = request.POST.get("spacial_message")
        items = booking(
            name=name,
            email=email,
            phone_no=phone,
            date=date,
            time=time,
            guests=guests,
            message=message,
        )
        items.save()
        table=booking.objects.filter(name=name)
        data={
            'name':name,
            'email':email,
            'phone':phone,
            'date':date,
            'time':time,
            'guests':guests,
            'table':table
            }
        return render(request,'book-conform.html',data)
    return render(request, "booking.html")


# def book_conform(request):
#     return render(request,'book-conform.html')
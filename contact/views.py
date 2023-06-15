from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from contact.models import contact_complaint
# Create your views here.

def contact(request):
    if request.method == "POST":
        name=request.POST.get('full_name')
        email=request.POST.get('email_id')
        phone=request.POST.get('phone_no')
        sub=request.POST.get('subject')
        comp=request.POST.get('complaint')
        items=contact_complaint.objects.create(
            name=name,
            email=email,
            mobile_no=phone,
            subject=sub,
            message=comp
        )
        items.save()
    return render(request,'contact.html')
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from testimonial.models import happy_customers

# Create your views here.

def testimonial(request):
    happy_cumstommers=happy_customers.objects.all()
    data={
        'happy_cumstommers':happy_cumstommers
    }
    return render(request, 'testimonial.html',data)
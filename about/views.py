from django.shortcuts import render
from about.models import happy_customers
# Create your views here.

def about(request):
    home_happy_cutommers_data=happy_customers.objects.all()
    data={
        'home_happy_cutommers_data':home_happy_cutommers_data
    }
    return render(request,'about.html',data) 
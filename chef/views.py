from django.shortcuts import render

# Create your views here.

def chef(request):
    return render(request,'chef.html')
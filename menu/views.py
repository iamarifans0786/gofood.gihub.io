from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from menu.models import pizza,pasta,desserts,burgur,breakfast,lunch,dinner,healty
# Create your views here.

def fastfood(request):
    burg=burgur.objects.all()
    piz=pizza.objects.all()
    pas=pasta.objects.all()
    des=desserts.objects.all()
    data={
        'burgur':burg,
        'pizza':piz,
        'pasta':pas,
        'desert':des
    }
    return render(request, 'fastfood.html',data)

def mainfood(request):
    brek=breakfast.objects.all()
    lun=lunch.objects.all()
    din=dinner.objects.all()
    hel=healty.objects.all()
    data={
        'breakefast':brek,
        'lunch':lun,
        'dinner':din,
        'healty':hel
    }
    return render(request, 'mainfood.html',data)    
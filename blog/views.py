from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from blog.models import blogs,comments
# Create your views here.

def blog(request):
    blog=blogs.objects.all()
    return render(request,'blog.html',{
        'data':blog
    })


def blog_explore(request,id=None):
    comment_body = name = None  # default value of input fields None
    
    if request.method == "POST":    # check request
        comment_body=request.POST.get("comment")    # getting data from input fields
        name=request.POST.get("aouther")
    object=blogs.objects.get(id=id)                  # get object from database
    if comment_body and name:
        data=comments(post=object,comment_body=comment_body,name=name) #assing comments to object
        data.save()
        
    all_comment=comments.objects.filter(post=object)  # getting comments of proper object 
    
    data={
        'items':object,
        'all_comment':all_comment
    }
    return render(request,'explore.html',data)    

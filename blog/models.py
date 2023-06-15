from django.db import models
from tinymce.models import HTMLField
# Create your models here.
 
class blogs(models.Model):
    blog_img=models.ImageField(upload_to="blog_img")
    person_name=models.CharField(max_length=20)
    date=models.DateField(auto_now_add=True)
    food=models.CharField(max_length=20)
    blog_title=models.TextField(null=True)
    detail=HTMLField(null=True)

    def __str__(self):
        return self.food
    
    
class comments(models.Model):
    post=models.ForeignKey(blogs,on_delete=models.CASCADE)
    comment_body=models.TextField()
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.comment_body    
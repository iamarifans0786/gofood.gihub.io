from django.db import models

# Create your models here.

class booking(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone_no=models.CharField(max_length=13)
    date=models.DateField()
    time=models.TimeField()
    guests=models.IntegerField()
    message=models.TextField()
    
    def __str__(self):
        return self.name
    

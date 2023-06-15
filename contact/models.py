from django.db import models

# Create your models here

class contact_complaint(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    mobile_no=models.CharField(max_length=13)
    subject=models.CharField(max_length=50)
    message=models.TextField()
    
    def __str__(self):
        return self.name
    
    

    


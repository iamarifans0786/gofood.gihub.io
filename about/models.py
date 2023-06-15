from django.db import models

# Create your models here.

class happy_customers(models.Model):
    comments=models.CharField(max_length=500)
    person_img=models.ImageField(upload_to="home_customers_img")
    person_name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    half_img=models.ImageField( upload_to="home_customers_img")

    def __str__(self):
        return self.person_name
    

from django.db import models

# Create your models here.

class home_menu(models.Model):
    dis_img=models.ImageField(upload_to="home_menu_img")
    dis_name=models.CharField(max_length=50)
    dis_detail=models.CharField(max_length=500)

    def __str__(self):
        return self.dis_name
     
class home_news_blogs(models.Model):
    blog_img=models.ImageField(upload_to="home_blog_img")
    person_name=models.CharField(max_length=20)
    date=models.DateField(auto_now_add=True)
    food=models.CharField(max_length=20)
    heading=models.CharField(max_length=50)
    detail=models.CharField(max_length=500)

    def __str__(self):
        return self.person_name
    
class happy_customers(models.Model):
    comments=models.CharField(max_length=500)
    person_img=models.ImageField(upload_to="home_customers_img")
    person_name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    half_img=models.ImageField( upload_to="home_customers_img")

    def __str__(self):
        return self.person_name
    



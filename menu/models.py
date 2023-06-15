from django.db import models

# Create your models here.
# starters menu 
# burgur 
class burgur(models.Model):
    dis_name=models.CharField(max_length=30)
    detail=models.CharField(max_length=50)
    price=models.FloatField()

# pizza
class pizza(models.Model):
    dis_name=models.CharField(max_length=30)
    detail=models.CharField(max_length=50)
    price=models.FloatField()

# pasta     
class pasta(models.Model):
    dis_name=models.CharField(max_length=30)
    detail=models.CharField(max_length=50)
    price=models.FloatField()

# desert
class desserts(models.Model):
    dis_name=models.CharField(max_length=30)
    detail=models.CharField(max_length=50)
    price=models.FloatField()

#  main course menu 
# breakefast 

class breakfast(models.Model):
    dis_name=models.CharField(max_length=30)
    dis_img=models.ImageField( upload_to="Main_course_menu")
    detail=models.CharField(max_length=50)
    price=models.FloatField()

class lunch(models.Model):
    dis_name=models.CharField(max_length=30)
    dis_img=models.ImageField( upload_to="Main_course_menu")
    detail=models.CharField(max_length=50)
    price=models.FloatField()

class dinner(models.Model):
    dis_name=models.CharField(max_length=30)
    dis_img=models.ImageField( upload_to="Main_course_menu")
    detail=models.CharField(max_length=50)
    price=models.FloatField()

class healty(models.Model):
    dis_name=models.CharField(max_length=30)
    dis_img=models.ImageField( upload_to="Main_course_menu")
    detail=models.CharField(max_length=50)
    price=models.FloatField()

    
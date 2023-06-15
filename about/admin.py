from django.contrib import admin
from about.models import happy_customers
# Register your models here.

class happy_customers_edit(admin.ModelAdmin):
    list_display=[
        'person_name',
        'person_img',
        'address',
        'comments',
     ] 

admin.site.register(happy_customers,happy_customers_edit)
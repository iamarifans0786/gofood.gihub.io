from django.contrib import admin
from booking.models import booking
# Register your models here.

@admin.register(booking)
class booking_details(admin.ModelAdmin):
    list_display=[
        'name',
        'email',
        'phone_no',
        'date',
        'time',
        'guests',
        'message'
    ]
    date_hierarchy=('date')
    list_filter=[
        'name'
    ]
    search_fields=[
        'id'
    ]
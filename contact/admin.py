from django.contrib import admin
from contact.models import contact_complaint

@admin.register(contact_complaint)
class conact(admin.ModelAdmin):
    list_display=[
        'name',
        'email',
        'mobile_no',
        'subject',
        'message',
    ]
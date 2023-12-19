from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(Profile)
admin.site.register(ContactSubmission)
# admin.site.register(User_profile)
# admin.site.register(Location)
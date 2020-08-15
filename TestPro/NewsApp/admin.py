from django.contrib import admin
from .models import News, Sports, RegistrationData

# Register your models here.

admin.site.register(News)
admin.site.register(Sports)
admin.site.register(RegistrationData)

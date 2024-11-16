from django.contrib import admin
from .models import Event, Category, Booking

# Register your models here.
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Booking)
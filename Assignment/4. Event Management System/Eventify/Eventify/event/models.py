from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Event model for storing event details
class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    capacity = models.PositiveIntegerField(default=0) 
    attendees_count = models.PositiveIntegerField(default=0) 

    def is_full(self):
        return self.attendees_count >= self.capacity

    def __str__(self):
        return self.name

# Booking model for tracking event bookings
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"

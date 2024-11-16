from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_event, name='create_event'),  
    path('update/<int:event_id>/', views.update_event, name='update_event'),  
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),  
    path('<int:event_id>/book/', views.book_event, name='book_event'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('my-bookings/delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('my-events/', views.my_events, name='my_events'),

]


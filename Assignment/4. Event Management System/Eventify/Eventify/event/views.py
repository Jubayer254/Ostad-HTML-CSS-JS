from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Booking, Category
from django.http import HttpResponseNotFound

from django.shortcuts import render
from .models import Event, Booking, Category

def home(request):
    events = Event.objects.all()
    categories = Category.objects.all()
    booked_events = []

    query = request.GET.get('q', '')
    if query:
        events = events.filter(
            name__icontains=query) | events.filter(
            date__icontains=query) | events.filter(
            location__icontains=query)

    category_id = request.GET.get('category')
    if category_id:
        events = events.filter(category_id=category_id)

    if request.user.is_authenticated:
        booked_events = Booking.objects.filter(user=request.user).values_list('event_id', flat=True)
    
    return render(request, 'homepage.html', {
        'events': events,
        'booked_events': booked_events,
        'categories': categories,
        'selected_category': category_id,
        'query': query,
    })


@login_required
def create_event(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        location = request.POST['location']
        description = request.POST['description']
        category_id = request.POST.get('category')
        capacity = request.POST.get('capacity', 0)

        event = Event.objects.create(
            name=name,
            date=date,
            location=location,
            description=description,
            created_by=request.user,
            category_id=category_id if category_id else None,
            capacity=capacity
        )
        messages.success(request, 'Event created successfully!')
        return redirect('home')
    
    categories = Category.objects.all()
    return render(request, 'create_event.html', {'categories' : categories})


@login_required
def book_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound("<h1 class='text-3xl font-semibold text-center'>Event not found</h1>")

    if event.is_full():
        messages.error(request, 'This event is fully booked.')
        return redirect('home')

    Booking.objects.get_or_create(user=request.user, event=event)
    event.attendees_count += 1
    event.save()
    messages.success(request, 'Event booked successfully!')
    return redirect('home')


@login_required
def my_bookings(request):
    user_booked_events = Booking.objects.filter(user=request.user)

    context = {
        'user_booked_events': user_booked_events,
    }
    return render(request, 'my_bookings.html', context)

@login_required
def update_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id, created_by=request.user)
    except Event.DoesNotExist:
        return HttpResponseNotFound("<h1 class='text-3xl font-semibold text-center'>Event not found</h1>")
    
    if request.method == 'POST':
        event.name = request.POST['name']
        event.date = request.POST['date']
        event.location = request.POST['location']
        event.description = request.POST['description']
        event.capacity = request.POST.get('capacity', 0)
        
        category_id = request.POST.get('category')
        event.category_id = category_id if category_id else None
        event.save()

        messages.success(request, 'Event updated successfully!')
        return redirect('my_events')

    categories = Category.objects.all()
    return render(request, 'update_event.html', {'event': event, 'categories': categories})

@login_required
def delete_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id, created_by=request.user)
    except Event.DoesNotExist:
        return HttpResponseNotFound("<h1 class='text-3xl font-semibold text-center'>Event not found</h1>")
    
    event.delete()
    messages.success(request, 'Event deleted successfully!')
    return redirect('home')

@login_required
def delete_booking(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id, user=request.user)
    except Booking.DoesNotExist:
        return HttpResponseNotFound("<h1 class='text-3xl font-semibold text-center'>Booking not found</h1>")
    
    event = booking.event

    booking.delete()

    if event.attendees_count > 0:
        event.attendees_count -= 1
        event.save()

    messages.success(request, 'Booking canceled successfully!')
    return redirect('my_bookings')


@login_required
def my_events(request):
    user_events = Event.objects.filter(created_by=request.user)

    context = {
        'user_events': user_events,
    }
    return render(request, 'my_events.html', context)

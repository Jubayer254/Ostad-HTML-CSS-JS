from django.shortcuts import render
from .forms import ProfileForm

# Create your views here.
def add_profiles(request):
    form = ProfileForm()
    return render(request, 'add_author.html', {"form": form})

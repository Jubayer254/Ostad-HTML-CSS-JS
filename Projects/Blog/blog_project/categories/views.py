from django.shortcuts import render
from .forms import CategoryForm

# Create your views here.
def add_categories(request):
    form = CategoryForm()
    return render(request, 'add_author.html', {"form": form})

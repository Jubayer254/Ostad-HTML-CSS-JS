from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def add_posts(request):
    form = PostForm()
    return render(request, 'add_author.html', {"form": form})

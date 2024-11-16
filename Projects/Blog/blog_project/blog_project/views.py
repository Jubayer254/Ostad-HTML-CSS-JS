from django.shortcuts import render, redirect
from posts.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    data = Post.objects.all()
    return render(request, 'home.html', {'data': data})
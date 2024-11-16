from django.shortcuts import render
from posts.models import Post
from django.db.models import Q


def home(request):
    query = request.GET.get('search', '')
    
    if query:
        data = Post.objects.filter(
            Q(title__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()
    else:
        data = Post.objects.all()
    
    return render(request, 'home.html', {'data': data, 'query': query})
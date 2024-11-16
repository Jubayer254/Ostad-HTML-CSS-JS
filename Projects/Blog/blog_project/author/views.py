from django.shortcuts import render, redirect
from .forms import AuthorForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('add_author')  
    else:
        form = AuthorForm()  

    return render(request, 'add_author.html', {"form": form})
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('homepage')  
    else:
        form = RegisterForm()  

    return render(request, 'register.html', {"form": form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password')
            user = authenticate(username = user_name, password = user_password)  

            if user is not None:
                login(request, user=user)
                return redirect('home')
            else:
                return redirect('login')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login')
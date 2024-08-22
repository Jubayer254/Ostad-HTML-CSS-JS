from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'cool_app/abc.html')

def course_list(request, language):
    return HttpResponse(f'Ostad Course list page<br>{language}')
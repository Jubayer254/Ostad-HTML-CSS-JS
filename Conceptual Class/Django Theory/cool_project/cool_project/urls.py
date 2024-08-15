from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello World')

new_url_patterns = [
    path('home/', home),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include(new_url_patterns)),
]


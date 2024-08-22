from django.urls import path, include

from dashboard.views import(
    home, 
    course_list
)

urlpatterns = [
    path('home/', home),
    path('ostad/<language>/courses/', course_list),
]
 
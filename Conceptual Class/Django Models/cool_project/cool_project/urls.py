from django.contrib import admin
from django.urls import path, include
# from dashboard.urls import dashboard_url_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('dashboard/', include(dashboard_url_patterns)),
    path('dashboard/', include("dashboard.urls")),
]


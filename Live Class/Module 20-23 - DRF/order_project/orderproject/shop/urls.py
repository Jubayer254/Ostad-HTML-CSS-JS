from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', views.ProductView, basename='products')
router.register(r'orders', views.OrederViewSet, basename='orders')

urlpatterns = [
    path('register/', views.ResigistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected_view/', views.ProtectedView.as_view(), name='protected_view'),
    path('', include(router.urls)),
    # path('products/', views.ProductView.as_view({"get": "list", "post": "create"}), name='products'),
    
]
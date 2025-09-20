from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, api_root

urlpatterns = [
    path('', api_root, name='api-root'),  # handles /api/
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
]

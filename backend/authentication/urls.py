from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import RegisterView, LogoutView

urlpatterns = [
    # Simple JWT authentication URLs
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('verify/', TokenVerifyView.as_view(), name='verify'),

    # Custom urls
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='register'),
]

from django.urls import path
from .views import RetrieveUpdateDestroyUserView, RetrieveSpecifiedUserView

urlpatterns = [
    path('', RetrieveUpdateDestroyUserView.as_view(), name='user-detail-update-delete'),
    path('<int:pk>/', RetrieveSpecifiedUserView.as_view(), name='user-retrieve'),
]

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .create_receipt import GenerateReceipt, FilterReceipt
from .user_manager import UsersManager

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('generate', GenerateReceipt.as_view(), name='generate_receipt'),
    path('all', GenerateReceipt.as_view(), name='all'),
    path('filter/<str:receiptId>', FilterReceipt.as_view(), name='filter'),
    path('users/', UsersManager.as_view(), name='users'),
]

from django.urls import path
from .views import RegisterView, CurrentUserView, LogoutView, ChangePasswordView

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )

urlpatterns = [
    path("register/", RegisterView.as_view(), name='register'),
    path("login/", TokenObtainPairView.as_view(), name='login'),
    path("refresh/", TokenRefreshView.as_view(), name='refresh'),
    path("me/", CurrentUserView.as_view(), name="current-user"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("change-password/", ChangePasswordView.as_view(), name='change-password'),
]
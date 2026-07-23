from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .api_views import (
    RegisterView,
    LogoutView,
    ProfileView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),

    # Login
    path("login/", TokenObtainPairView.as_view(), name="login"),

    # Refresh Token
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("logout/", LogoutView.as_view(), name="logout"),

    path("profile/", ProfileView.as_view(), name="profile"),
]
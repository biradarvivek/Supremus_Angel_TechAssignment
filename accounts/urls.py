from django.urls import path
from .views import login_view, register_view, logout_view, profile_view

urlpatterns = [
    path(
        "login/",
        login_view,
        name="login-page",
    ),
    path(
        "register/",
        register_view,
        name="register-page",
    ),
     path(
        "logout/",
        logout_view,
        name="logout-page",
    ),
    path(
        "profile/",
        profile_view,
        name="profile-page",
    ),
]
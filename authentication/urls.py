from django.urls import path
from authentication.views import LogoutView, SignUpView, getAllUsers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),

    path("login/refresh/", TokenRefreshView.as_view(), name="refresh"),

    path("logout/", LogoutView.as_view(), name="logout"),

    path("signup/", SignUpView.as_view(), name="signup"),

    path("all-users/", getAllUsers.as_view(), name="all-users"),
]

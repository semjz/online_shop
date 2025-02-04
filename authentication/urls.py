from django.urls import path
from authentication.views import UserSignUpView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from authentication.views import CustomerSignUpView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),

    path("login/refresh/", TokenRefreshView.as_view(), name="refresh"),

    path('signup/customer/', CustomerSignUpView.as_view(), name='customer_register'),
    path('signup/user/', UserSignUpView.as_view(), name='user_register'),

]

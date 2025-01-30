from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .. import views
from ..views import (
    CustomObtainAuthToken,
    CustomTokenObtainPairView,
    ChangePasswordView,
)

urlpatterns = [
    path("register/", views.RegisterApiView.as_view(), name="register"),
    path("token/login/", CustomObtainAuthToken.as_view(), name="token-login"),
    path("token/logout/", views.Logout.as_view(), name="token-logout"),
    path(
        "jwt/create/", CustomTokenObtainPairView.as_view(), name="jwt_create"
    ),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"),
    path(
        "change-password/",
        ChangePasswordView.as_view(),
        name="change-password",
    ),
    path("test-email/", views.SendEmailView.as_view(), name="test-email"),
    path(
        "verify-email/<str:token>/",
        views.VerifyEmail.as_view(),
        name="verify-email",
    ),
    path(
        "resend-verification-email/",
        views.ResendVerificationEmail.as_view(),
        name="resend-verification-email",
    ),
]

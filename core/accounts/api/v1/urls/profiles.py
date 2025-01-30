from django.urls import path, include
from rest_framework.authtoken import views

# from rest_framework.authtoken.views import ObtainAuthToken
from .. import views
from ..views import CustomTokenObtainPairView, ChangePasswordView


app_name = "api-v1"

urlpatterns = [
    path("", views.ProfileView.as_view(), name="profile"),
]

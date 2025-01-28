from django.urls import path, include
from rest_framework.authtoken import views
# from rest_framework.authtoken.views import ObtainAuthToken

from . import views
from .views import CustomObtainAuthToken

app_name = 'api-v1'

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register'),
    path('token/login/', CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.Logout.as_view(), name='token-logout'),
]

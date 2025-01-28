from django.urls import path, include
from rest_framework.authtoken import views
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



from . import views
from .views import CustomObtainAuthToken

app_name = 'api-v1'

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register'),
    path('token/login/', CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.Logout.as_view(), name='token-logout'),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
]

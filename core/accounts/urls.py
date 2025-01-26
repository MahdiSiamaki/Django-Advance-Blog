from django.urls import path, include
from .views import RegisterView

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),  # This includes login, logout, etc
    path('register/', RegisterView.as_view(), name='register'),
    path('api/v1/', include('accounts.api.v1.urls')),
]

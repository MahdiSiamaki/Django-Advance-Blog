from django.urls import path, include
from . import views

app_name = 'api-v1'

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register'),
]

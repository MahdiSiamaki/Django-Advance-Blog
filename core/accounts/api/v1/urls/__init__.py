from django.urls import path, include

urlpatterns = [
    path('profile/', include('accounts.api.v1.urls.profiles')),
    path('', include('accounts.api.v1.urls.accounts')),
]
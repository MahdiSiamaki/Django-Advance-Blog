from django.urls import path, include
from .views import RegisterView, CacheTestView

app_name = "accounts"

urlpatterns = [
    path(
        "", include("django.contrib.auth.urls")
    ),  # This includes login, logout, etc
    path("register/", RegisterView.as_view(), name="register"),
    # path('api/v1/', include('accounts.api.v1.urls')),
    path("api/v2/", include("djoser.urls")),
    path("api/v2/", include("djoser.urls.jwt")),
    path('cache/test/', CacheTestView, name='cache_test'),
]

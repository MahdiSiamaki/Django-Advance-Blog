from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import requests

User = get_user_model()


class RegisterView(CreateView):
    model = User
    template_name = "registration/register.html"
    fields = ["email", "full_name", "password"]
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        # Hash the password before saving
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        return super().form_valid(form)


@cache_page(60)  # Cache for 60 seconds
def CacheTestView(request):
    try:
        response = requests.get('https://c00c889b-7bb6-4c06-abe5-51ef82174d29.mock.pstmn.io/test/delay/5')
        response.raise_for_status()
        return JsonResponse(response.json())
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
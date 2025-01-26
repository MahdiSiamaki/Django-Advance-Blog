from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.urls import reverse_lazy

User = get_user_model()

class RegisterView(CreateView):
    model = User
    template_name = 'registration/register.html'
    fields = ['email', 'full_name', 'password']
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Hash the password before saving
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        return super().form_valid(form)

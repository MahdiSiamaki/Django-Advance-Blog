from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('email', 'password', 'full_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_verified')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'full_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_verified')}),
    )
    list_display = ['email', 'full_name', 'is_staff', 'is_active', 'is_superuser', 'is_verified']
    list_filter = ['is_staff', 'is_active', 'is_superuser', 'is_verified']
    search_fields = ['email', 'full_name']
    ordering = ['email']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image']
    search_fields = ['user__email', 'user__full_name']
    ordering = ['user__email']


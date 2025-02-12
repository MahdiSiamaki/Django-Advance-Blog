from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at', 'updated_at')
    search_fields = ('post__title', 'author__email', 'content')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

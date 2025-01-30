from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("posts", views.PostModelViewSet, basename="post")
router.register("categories", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls

"""urlpatterns = [
    # path('posts/', views.post_list, name='post-list'),
    # path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    # path('posts/', views.PostList.as_view(), name='post-list'),
    # path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
]
"""

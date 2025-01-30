from django.views.generic import RedirectView

from .views import (
    index_view,
    IndexView,
    RedirectToMaktab,
    PostList,
    PostDetail,
    PostCreateView,
    PostEditView,
    PostDeleteView,
)
from django.urls import path, include

app_name = "blog"

urlpatterns = [
    path("", index_view, name="index"),
    path("cbv/", IndexView.as_view(), name="index_cbv"),
    path(
        "go-to-maktabkhooneh/", RedirectToMaktab.as_view(), name="go-to-maktabkhooneh"
    ),
    path("posts/", PostList.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", PostEditView.as_view(), name="post-edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("api/v1/", include("blog.api.v1.urls")),
]

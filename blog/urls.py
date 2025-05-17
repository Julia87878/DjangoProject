from django.urls import path

from blog.apps import BlogConfig
from blog.views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("blogs/", PostListView.as_view(), name="posts_list"),
    path("blogs/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("blogs/new/", PostCreateView.as_view(), name="post_create"),
    path("blogs/update/<int:pk>/", PostUpdateView.as_view(), name="post_update"),
    path("blogs/delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
]

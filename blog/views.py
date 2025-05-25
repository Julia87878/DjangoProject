from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/posts_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active_publication=True)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "image", "is_active_publication"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:posts_list")


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = [
        "title",
        "content",
        "image",
        "is_active_publication",
    ]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:posts_list")

    def get_success_url(self):
        return reverse("blog:post_detail", args=[self.object.pk])


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:posts_list")

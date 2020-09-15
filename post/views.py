from django.shortcuts import render

from django.views.generic import ListView

from post.filters import PostFilter
from post.models import Post


class PostsListView(ListView):
    model = Post

    def get(self, request, *args, **kwargs):
        f = PostFilter(request.GET, queryset=self.queryset)
        self.extra_context = {"filter": f}
        return super().get(request, *args, **kwargs)

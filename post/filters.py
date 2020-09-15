import django_filters

from post.models import Post


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    content = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Post
        fields = {"title", "content", "author"}

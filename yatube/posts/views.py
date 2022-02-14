from django.shortcuts import get_object_or_404, render

from .models import Group, Post

POST_FETCH_SIZE = 10


def index(request):
    posts = Post.objects.select_related('author', 'group')[:POST_FETCH_SIZE]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author')[:POST_FETCH_SIZE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

from django.shortcuts import get_object_or_404, render
from .models import Group, Post

POSTS_ON_MAIN = 10


def index(request):
    posts = Post.objects.all()
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


# Create your views here.
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_ON_MAIN]
    context = {
        'group': group,
        'posts': posts,

    }
    return render(request, 'posts/group_list.html', context)

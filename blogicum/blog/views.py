from django.shortcuts import get_object_or_404, render

from django.db.models.functions import Now

from blog.models import Post
from blog.models import Category


POSTS_PUBLISHED = Post.objects.select_related(
    'category', 'location', 'author').filter(
        pub_date__lte=Now(),
        is_published=True,
        category__is_published=True)

FIVE_RECENT_PUBLICATIONS = 5


def index(request):
    """Функция отображения Ленты записей."""
    template = 'blog/index.html'
    post_list = POSTS_PUBLISHED[:FIVE_RECENT_PUBLICATIONS]
    data = {'post_list': post_list}
    return render(request, template, context=data)


def post_detail(request, post_id):
    """Функция показа записи заданной пользователем."""
    template = 'blog/detail.html'
    post = get_object_or_404(POSTS_PUBLISHED.filter(id=post_id))
    data = {'post': post}
    return render(request, template, context=data)


def category_posts(request, category_slug):
    """Функция показа постов определенной категории."""
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = POSTS_PUBLISHED.filter(category__slug=category_slug)
    data = {'category': category, 'post_list': post_list}
    return render(request, template, context=data)

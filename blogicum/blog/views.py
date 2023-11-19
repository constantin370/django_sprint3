from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from blog.models import Post, Category


def index(request):
    """Функция отображения Ленты записей."""
    template = 'blog/index.html'
    post_list = Post.objects.filter(pub_date__lte=timezone.now(),
                                    is_published=True,
                                    category__is_published=True)
    post_list = post_list.order_by('-pub_date')[:5]
    data = {'post_list': post_list}
    return render(request, template, context=data)


def post_detail(request, post_id):
    """Функция показа записи заданной пользователем."""
    template = 'blog/detail.html'
    post = get_object_or_404(Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True),
        id=post_id)
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
    post_list = Post.objects.all().select_related(
        'author',
        'location',
        'category'
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
        category__slug=category_slug
    ).order_by(
        '-pub_date'
    )
    data = {'category': category, 'post_list': post_list}
    return render(request, template, context=data)

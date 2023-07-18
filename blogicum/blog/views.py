from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post, Category


def posts_filtered():
    return Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def post_detail(request, post_id):
    post = get_object_or_404(posts_filtered(),
                             id=post_id,
                             )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def index(request):
    posts = posts_filtered().order_by('-pub_date')[:5]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def category_posts(request, slug):
    category = get_object_or_404(Category,
                                 slug=slug,
                                 is_published=True)
    posts = posts_filtered().filter(category=category)
    context = {'category': category, 'post_list': posts}
    return render(request, 'blog/category.html', context)

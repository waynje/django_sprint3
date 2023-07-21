from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post, Category


def posts_filtered(posts):
    return posts.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def post_detail(request, post_id):
    return render(request, 'blog/detail.html',
                  {'post': get_object_or_404(
                    posts_filtered(Post.objects),
                    id=post_id)})


def index(request):
    return render(request, 'blog/index.html',
                  {'post_list': posts_filtered(Post.objects).order_by
                   ('-pub_date')[:5]}
                  )


def category_posts(request, slug):
    category = get_object_or_404(Category,
                                 slug=slug,
                                 is_published=True)
    posts = posts_filtered(Post.objects).filter(category=category)
    return render(request, 'blog/category.html',
                  {'category': category,
                   'post_list': posts})

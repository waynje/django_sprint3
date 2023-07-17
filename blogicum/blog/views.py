from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.utils import timezone

now = timezone.now


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id,
                             is_published=True,
                             category__is_published=True,
                             )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def index(request):
    posts = Post.objects.all().filter(
                                      is_published=True,
                                      category__is_published=True,
    ).order_by('pub_date')[:5]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def category_posts(request, slug):
    category = get_object_or_404(Category,
                                 slug=slug,
                                 is_published=True)
    posts = Post.objects.all().filter(
                                      is_published=True,
                                      category__is_published=True,
                                      category=category
    )
    context = {'category': category, 'post_list': posts}
    return render(request, 'blog/category.html', context)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category


def post_list(request):
    posts = Post.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats
    }

    return render(request, 'app/post_list.html', context=context)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    cats = Category.objects.all()

    context = {
        'post': post,
        'cats': cats
    }

    return render(request, 'app/post_detail.html', context=context)


def category(request, cat_id):
    posts = Post.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats
    }

    return render(request, 'app/post_list.html', context=context)

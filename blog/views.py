from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404


# Create your views here.


def post_list(request):
    posts = Post.published.all()  # Post.objects.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

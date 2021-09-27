from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import DetailView

from .forms import *
from .models import User, Post, Comment


def index_view(request):
    posts = Post.objects.all().order_by('-post_publish_time')
    return render(request, 'blog/index.html', context={"posts": posts})


class PostAndAllComments(DetailView):
    model = Post
    template_name = 'blog/detail-view.html'
    context_object_name = 'detail'


def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')

    form = NewPostForm()
    return render(request, 'blog/addpost.html', context={'form': form})


def new_comment(request):
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')

    form = NewCommentForm()
    return render(request, 'blog/addcomment.html', context={'form': form})


def new_category(request):
    if request.method == 'POST':
        form = NewCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')

    form = NewCategoryForm()
    return render(request, 'blog/addcategory.html', context={'form': form})


def new_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')

    form = NewUserForm()
    return render(request, 'blog/adduser.html', context={'form': form})
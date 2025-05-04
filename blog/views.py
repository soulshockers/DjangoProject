from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import CategoryForm, PostForm
from blog.models import Category, Post


def home(request):
    return render(request, 'home.html')


def category_list(request):
    categories = Category.objects.order_by('date_added')
    context = {
        'categories': categories
    }
    return render(request, 'categories/category_list.html', context)


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = category.post_set.order_by('-date_added')
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'categories/category_detail.html', context)


def category_add(request):
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:category_list')

    context = {
        'form': form
    }
    return render(request, 'categories/category_add.html', context)


def category_edit(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    if request.method != 'POST':
        form = CategoryForm(instance=category)
    else:
        form = CategoryForm(instance=category, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:category_detail', category_id=category_id)

    context = {
        'category': category,
        'form': form
    }
    return render(request, 'categories/category_edit.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)


def post_add(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post_add = form.save(commit=False)
            post_add.category = category
            post_add.save()
            return redirect('blog:category_detail', category_id=category_id)

    context = {
        'category': category,
        'form': form
    }
    return render(request, 'posts/post_add.html', context)


def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    category = post.category

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:category_detail', category_id=category.id)

    context = {
        'post': post,
        'category': category,
        'form': form
    }
    return render(request, 'posts/post_edit.html', context)

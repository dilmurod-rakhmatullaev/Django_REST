from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

menu = [
    {'title': "About", 'url_name': 'about'},
    {'title': "Add article", 'url_name': 'add_article'},
    {'title': "Feedback", 'url_name': 'feedback'},
    {'title': "Log in", 'url_name': 'login'},
]

#HttpRequest
def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Home',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About'})

def add_article(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, "Post adding error")
    else:
            form = AddPostForm()
    return render(request, 'women/add_article.html', {'form': form, 'menu': menu, 'title': 'Add article'})

def feedback(request):
    return HttpResponse("Add page")

def login(request):
    return HttpResponse("Log in")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found</h1>")

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context=context)

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.objects.filter(cat_id=category.pk)

    if len(posts) == 0:
        raise Http404("Page not found")

    context = {
        'posts': posts,
        'menu': menu,
        'title': category.name,
        'cat_selected': category.pk,
    }
    return render(request, 'women/index.html', context=context)
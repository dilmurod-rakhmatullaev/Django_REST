from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
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
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Home',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About'})

def add_article(request):
    return HttpResponse("Add article")

def feedback(request):
    return HttpResponse("Add page")

def login(request):
    return HttpResponse("Log in")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found</h1>")

def show_post(request, post_id):
    return HttpResponse(f"Post {post_id}")

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404("Page not found")

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Categories',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)
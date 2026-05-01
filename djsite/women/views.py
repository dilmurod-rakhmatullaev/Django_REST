from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

menu = ["About", "Add article", "Feedback", "Log in"]

#HttpRequest
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Home'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About'})

def categories(request, catid):
    if (request.POST):
        request.POST

    return HttpResponse(f"<h1>Categories</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2026:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Archive per years</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found</h1>")

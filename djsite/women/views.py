from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


#HttpRequest
def index(request):
    return HttpResponse("Hello, world. You're at the Women index.")

def categories(request, catid):
    if (request.GET):
        print(request.GET)
    if(request.POST):
        request.POST

    return HttpResponse(f"<h1>Categories</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2026:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Archive per years</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found</h1>")

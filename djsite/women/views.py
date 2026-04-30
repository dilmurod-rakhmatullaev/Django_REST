from django.http import HttpResponse
from django.shortcuts import render

#HttpRequest
def index(request):
    return HttpResponse("Hello, world. You're at the Women index.")

def categories(request):
    return HttpResponse("<h1>Categories</h1>")
from multiprocessing import context

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

menu = [
    {'title': "About", 'url_name': 'about'},
    {'title': "Add article", 'url_name': 'add_article'},
    {'title': "Feedback", 'url_name': 'feedback'},
    {'title': "Log in", 'url_name': 'login'},
]

class WomenHome(ListView):
    model = Women
    template_name = "women/index.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Women - Home Page'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)

"""
def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Home',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)
"""

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About'})

class AddArticle(CreateView):
    form_class = AddPostForm
    template_name = 'women/add_article.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Adding an article'
        context['menu'] = menu
        return context


"""
def add_article(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
                form.save()
                return redirect('home')
    else:
            form = AddPostForm()
    return render(request, 'women/add_article.html', {'form': form, 'menu': menu, 'title': 'Add article'})
"""

def feedback(request):
    return HttpResponse("Add page")

def login(request):
    return HttpResponse("Log in")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found</h1>")

"""
def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context=context)
"""

class ShowPost(DetailView):
    model = Women
    template_name = "women/post.html"
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['menu'] = menu
        return context

class WomenCategory(ListView):
    model = Women
    template_name = "women/index.html"
    context_object_name = 'posts'
    allow_empty = False  # уже есть, хорошо

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if context['posts']:
            context['title'] = 'Category - ' + str(context['posts'][0].cat)
            context['cat_selected'] = context['posts'][0].cat_id
        else:
            context['title'] = 'Category not found'
            context['cat_selected'] = 0
        context['menu'] = menu
        return context


"""
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
"""
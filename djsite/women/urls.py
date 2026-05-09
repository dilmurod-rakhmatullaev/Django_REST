from django.urls import path, re_path
from django.utils import archive

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_article/', add_article, name='add_article'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
]
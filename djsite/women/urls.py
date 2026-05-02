from django.urls import path, re_path
from django.utils import archive

from .views import *

urlpatterns = [
    path('', index, name='home'),    #http://127.0.0.1:8000/women/
    path('about/', about, name='about'),
    path('add_article/', add_article, name='add_article'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post')
]
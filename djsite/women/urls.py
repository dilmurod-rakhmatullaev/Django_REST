from django.urls import path, re_path
from django.utils import archive

from .views import *

urlpatterns = [
    path('', index, name='home'),    #http://127.0.0.1:8000/women/
    path('cats/<int:catid>/', categories),  #http://127.0.0.1:8000/women/cats/1/
    re_path(r'^archive/(?P<year>[0-9]{4})/$', archive),
]
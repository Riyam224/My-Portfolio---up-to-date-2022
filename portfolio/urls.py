from urllib.parse import urlparse
from django.urls import path
from . import views 


app_name = 'portfolio'

urlpatterns = [
    path('' , views.index  , name='index'),
    path('about/' , views.about , name='about'),
    path('work/' , views.work  , name='work'),
    path('services/' , views.services , name='services'),
]

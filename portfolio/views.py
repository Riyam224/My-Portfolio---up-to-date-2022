import re
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request , 'portfolio/index.html' , {})


def about(request):
    return render(request , 'portfolio/about.html' , {})

def work(request):
    return render(request , 'portfolio/work.html' , {})

def services(request):
    return render(request , 'portfolio/services.html' , {})
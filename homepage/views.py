from django.shortcuts import render
from .models import Blog
import random
from django.core.paginator import Paginator


def home_view(request):
    blogs = Blog.objects.all()
    random_blogs = random.sample(list(blogs), 3)
    context = {'random_blogs': random_blogs}
    return render(request, 'home.html', context)

def blog(request):
    blogs = Blog.objects.all().order_by('-time')
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)


def blogpost (request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {'blog': blog}
    return render(request, 'blogpost.html', context)

def iceland_view(request):

    return render(request, 'iceland.html')

def norway_view(request):

    return render(request, 'norway.html')

def winter_view(request):

    return render(request, 'winter.html')

def coversvol1_view(request):

    return render(request, 'coversvol1.html')

def intheautumnforest_view(request):

    return render(request, 'intheautumnforest.html')

def bc_view(request):

    return render(request, 'bc.html')
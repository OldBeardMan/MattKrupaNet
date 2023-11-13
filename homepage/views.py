from django.shortcuts import render, redirect
from .forms import SubscribeForm

def home_view(request):
    return render(request, 'home.html')
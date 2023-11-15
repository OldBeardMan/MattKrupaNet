from django.shortcuts import render, redirect
from .forms import SubscribeForm

def home_view(request):

    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Utwórz widok potwierdzenia zapisu
    else:
        form = SubscribeForm()

    return render(request, 'home.html', {'form': form})



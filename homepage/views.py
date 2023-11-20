from django.shortcuts import render, redirect
from .forms import SubscribeForm

def home_view(request):

    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('done')  # Utwórz widok potwierdzenia zapisu
    else:
        form = SubscribeForm()

    return render(request, 'home.html', {'form': form})

def iceland_view(request):

    return render(request, 'iceland.html')

def norway_view(request):

    return render(request, 'norway.html')

def winter_view(request):

    return render(request, 'winter.html')

def coversvol1_view(request):

    return render(request, 'coversvol1.html')

def intheautumnforest_view(request):

    return render(request, 'intheautumnforestview.html')



from django.shortcuts import render, redirect
from .forms import SubscribeForm, MessageForm

def home_view(request):

    if request.method == 'POST':
        form1 = SubscribeForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('done')  # Utwórz widok potwierdzenia zapisu
    else:
        form1 = SubscribeForm()


    if request.method == 'POST':
        form2 = MessageForm(request.POST)
        if form2.is_valid():
            form2.save()
           
    else:
        form2 = MessageForm()

    return render(request, 'home.html', {'form1': form1, 'form2': form2})




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

from django.shortcuts import render, redirect
from .forms import SubscribeForm

def home_view(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Tutaj możesz zapisać e-mail w pliku, wysłać go do zewnętrznego API itp.
            with open('subscribers.txt', 'a') as f:
                f.write(email + '\n')
    else:
        form = SubscribeForm()

    return render(request, 'home.html', {'form': form})


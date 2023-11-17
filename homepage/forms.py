from django import forms
from .models import Subscriber

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'custom-input',
                'placeholder': 'Some awesome person'
            }),
        }
        labels = {
            'email': '',
        }
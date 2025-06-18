from django import forms
from .models import Service

class MarkCompletedForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['tech_desc', 'price']
        widgets = {
            'tech_desc': forms.Textarea(attrs={
                'class': 'form-textarea w-full border-zinc-300 rounded',
                'rows': 4,
                'placeholder': 'Describe the work done...'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-input w-full border-zinc-300 rounded',
                'step': '0.01'
            }),
        }
        
        
class RequestServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['client_desc']
        widgets = {
            'tech_desc': forms.Textarea(attrs={
                'class': 'form-textarea w-full border-zinc-300 rounded',
                'rows': 4,
                'placeholder': 'Describe the issue...'
            }),
        }
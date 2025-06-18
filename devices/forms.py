from django import forms
from .models import Device
from users.models import CustomUser


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['serial_number', 'device_type', 'device_brand', 'installation_date', 'warranty_expiry', 'status', 'user']
        widgets = {
            'installation_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-input w-full border-zinc-300 rounded'
            }),
            'serial_number': forms.TextInput(attrs={'class': 'form-input w-full border-zinc-300 rounded'}),
            'device_type': forms.TextInput(attrs={'class': 'form-input w-full border-zinc-300 rounded'}),
            'device_brand': forms.TextInput(attrs={'class': 'form-input w-full border-zinc-300 rounded'}),
            'status': forms.Select(attrs={'class': 'form-select w-full border-zinc-300 rounded'}),
            'user': forms.Select(attrs={'class': 'form-select w-full border-zinc-300 rounded'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = CustomUser.objects.filter(role='technician')   
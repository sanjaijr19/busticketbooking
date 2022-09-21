from django import forms
from busapp.models import Driver

class DriverForm(forms.ModelForm):
    class Meta:
        model=Driver
        fields='__all__'

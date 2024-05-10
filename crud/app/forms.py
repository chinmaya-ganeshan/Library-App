from django import forms
from .models import app

class BookCreate(forms.ModelForm):
    class Meta:
        model = app
        fields = '__all__'

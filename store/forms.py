from django import forms
from .models import Puppy

class AdoptionForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    puppy_id = forms.IntegerField(widget=forms.HiddenInput())
# store/forms.py

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

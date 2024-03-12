from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    name = forms.CharField(label='Your Name', widget=forms.TextInput(attrs={'class': 'custom-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'custom-input'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'custom-input', 'rows': 4}))
    class Meta:
        model = ContactUs
        fields = '__all__'
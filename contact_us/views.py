from django.shortcuts import render,redirect
from django.contrib import messages
from .models import ContactUs
from .forms import ContactUsForm
# Create your views here.

def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submit successfully.!')
            return redirect('contact_us')  
    else:
        form = ContactUsForm()

    return render(request, 'contact_us.html', {'form': form})

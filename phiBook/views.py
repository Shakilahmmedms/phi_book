from django.shortcuts import render
from django.views.generic import TemplateView
from posts.models import Posts,Comment
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import DeleteView,DetailView

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def dashboard(request):
    data = Posts.objects.all()
    comment = Comment.objects.all()
    return render(request, 'dashborad.html', {'data' : data,'comments':comment, })


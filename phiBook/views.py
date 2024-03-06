from django.shortcuts import render
from django.views.generic import TemplateView
from posts.models import Posts,Comment
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import DeleteView,DetailView



def home(request):
    data = Posts.objects.all()
    comment = Comment.objects.all()
    return render(request, 'index.html', {'data' : data,'comments':comment})


from django.shortcuts import render
from django.views.generic import TemplateView
from posts.models import Posts


def home(request):
    data = Posts.objects.all()
    return render(request, 'index.html', {'data' : data})


from django.shortcuts import render,redirect
from django.http import HttpResponse
from .import forms
from .import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import DeleteView,DetailView
from django.contrib.auth.models import User
from .models import  Posts,Like
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            new_post = post_form.save(commit=False)  
            new_post.user = request.user 
            new_post.save() 
            return redirect('home')
    else:   
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form': post_form})




# def like_post(request, id):
#     post = Posts.objects.get(id=id)
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             post.post_like += 1
#             post.save()
#             return redirect('delails_post_view.html')
#     return render('index.html',{'post_like':post} )



class DetailPostViews(DetailView):
    model = models.Posts
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'

    def post(self,request, *args, **kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        posts = self.get_object()
       
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.posts = posts
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.object
        comments = posts.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context




@login_required
def edit_post(request, id):
    post = models.Posts.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    print(post.title)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, request.FILES, instance=post) 
        if post_form.is_valid():
            post_form.user = request.user
            post_form.save()
            return redirect('home')
    return render(request, 'add_post.html', {'form': post_form})


    

@login_required
def delete_post(request,id):
    post = models.Posts.objects.get(pk =id)
    post.delete()
    return redirect('home')






        
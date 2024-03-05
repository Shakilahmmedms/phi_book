from django.shortcuts import render,redirect
from .import forms
from .import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import DeleteView,DetailView


# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)  
            new_post.user = request.user 
            new_post.save() 
            return redirect('home')
    else:   
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form': post_form})

def detail_post_view(request, id):
    posts = models.Posts.objects.get(id=id)
    
    if request.method == 'POST':
        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.posts = posts
            new_comment.save()
    
    comments = posts.comments.all()
    comment_form = forms.CommentForm()
    
    context = {
        'posts': posts,
        'comments': comments,
        'comment_form': comment_form
    }
    
    return render(request, 'post_details.html', context)


# def my_posts(request):
#     posts = models.Posts.objects.filter(user=request.user)
#     return render(request, 'profile.html', {'posts': posts})



def like_post(request, id):
    post = models.Posts.objects.get(id=id)
    like, created = models.Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect('post_detail', id=id)

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
def edit_post(request,id):
    post = models.Posts.objects.get(pk =id)
    post_form = forms.PostForm(instance=post)
    print(post.title)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.user = request.user
            post_form.save()
            return redirect('homepage')
    return render(request,'add_post.html', {'form':post_form})

@login_required
def delete_post(request,id):
    post = models.Posts.objects.get(pk =id)
    post.delete()
    return redirect('homepage')
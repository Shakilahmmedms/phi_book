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
from .models import  Posts
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

def detail_post_view(request, id):
    posts = models.Posts.objects.get(id=id)
   
    if request.method == 'POST':
        posts.post_like += 1
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


def like_post(request, id):
    post = Posts.objects.get(id=id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            post.post_like += 1
            post.save()
            return redirect('delails_post_view.html')
    return render('post_details.html',{'post_like':post} )



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



# @login_required
# def like_post(request, id):
#     like = models.Posts.objects.get(id=id)
#     likes = models.Posts.objects.all()
#     user = request.user
#     models.Like.objects.create(user=request.user, like=like.post_like)  
#     like.post_like += 1
#     user.save()
#     like.save()
#     return render(request, './accounts/profile.html', {'likes': likes})





# @login_required
# def like_post(request, id):
#     post = get_object_or_404(Posts, id=id)
#     like, created = .objects.get_or_create(user=request.user, post=post)

#     if created:
#         post.post_like += 1
#         post.save()
#         like.like = 1
#         like.like_permi = True
#         like.save()
#         return redirect('details_post_view', post_id=id)  
    
#     return render('post_details.html',{'like': like})


# def dislike_post(request, post_id):
#     post = get_object_or_404(Posts, id=post_id)
#     like, created = Like.objects.get_or_create(user=request.user, post=post)

#     if created:
#         post.post_dislike += 1
#         post.save()
#         like.dislike = 1
#         like.dislike_permi = True
#         like.save()
#         return redirect('delails_post_view', post_id=post_id)
#     return render('post_details.html',{'like': like_post})
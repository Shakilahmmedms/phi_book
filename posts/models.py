from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/uploads/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    likes =  models.ManyToManyField(User, related_name='liked_posts', blank=True)
  
    def __str__(self):
        return self.title

class Comment(models.Model):
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, blank = True, null = True)

    def __str__(self):
        return self.name

# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='likes')
#     like = models.IntegerField(default=0,null=True,blank=True)
#     dislike = models.IntegerField(default=0,null=True,blank=True)
#     like_permi = models.BooleanField(default=False,null=True,blank=True)
#     dislike_permi = models.BooleanField(default=False,null=True,blank=True)
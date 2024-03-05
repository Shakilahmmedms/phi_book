from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank = True, null = True)

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

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_history')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add=True, blank = True, null = True)

    def __str__(self):
        return self.user
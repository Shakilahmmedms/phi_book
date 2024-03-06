from django.db import models
from django.contrib.auth.models import User
from posts.models import Posts
# Create your models here.

# class UserAccounts(models.Model):
    
#     user = models.OneToOneField(User, related_name = 'account', on_delete = models.CASCADE)
    
#     image = models.ImageField(upload_to='accounts/images/')
   
#     street_address = models.CharField(max_length=100, blank = True, null = True)
#     city = models.CharField(max_length= 100, blank = True, null = True)
#     country = models.CharField(max_length=100, blank = True, null = True)

#     def __str__(self):
#         return self.user.first_name
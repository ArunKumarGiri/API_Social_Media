from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    caption = models.TextField()
    # date = models.DateField(auto_now_add=True, null=True)
    # date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.user} + {self.caption[:20]}"

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    followers = models.IntegerField()
    following = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return str(self.user)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_date = models.DateTimeField(auto_now=True) 
    
class Comments(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date =models.DateTimeField(auto_now=True) 
    # comment_date = models.DateTimeField(default=timezone.now)
    
class Friends(models.Model):
    user = models.ForeignKey(User,related_name='to_user', on_delete=models.CASCADE)
    friend= models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now=True)







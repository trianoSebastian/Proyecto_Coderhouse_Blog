from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


# Modelo de usuario personalizado
class User(AbstractUser):
    user_avatar=models.OneToOneField('posts.User',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.username

class Avatar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='avatars',null=True,blank=True)
    
    def __str__(self):
        return f"User: {self.user}  -  Image: {self.image}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        url = reverse("detail", kwargs={"slug": self.slug})
        print("******URL:", url)
        return url
    
    def get_like_url(self):
        return reverse("like", kwargs={"slug": self.slug})
    
    @property
    def get_comment_count(self):
        return self.comment_set.all().count()

    @property
    def get_view_count(self):
        return self.postview_set.all().count()
    
    @property
    def get_like_count(self):
        return self.like_set.all().count()    
    
    @property
    def comments(self):
        return self.comment_set.all().order_by('-timestamp')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



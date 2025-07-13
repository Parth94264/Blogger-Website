from django.db import models


from django.db import models
from django.contrib.auth.models import User

class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ratings = models.FloatField(default=0)
    

    def __str__(self):
        return self.user.username   

class Blog(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE, related_name='blogs')
    rating = models.FloatField(default=0)
    views = models.IntegerField(default=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    viewers = models.ManyToManyField(User, related_name='viewed_blogs', blank=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
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
    viewers = models.ManyToManyField(User, related_name='viewed_blogs', blank=True)
    
    
    def __str__(self):
        return self.title

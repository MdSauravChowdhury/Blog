from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.FileField(upload_to='author/picture')
    bio = models.TextField()

    def __str__(self):
        return self.name.username


class category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name



class Post(models.Model):
    title = models.CharField(max_length=150)
    post_category = models.ForeignKey(category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/picture')
    descriptions = models.TextField()
    post_author = models.ForeignKey(author, on_delete=models.CASCADE)
    blockquote = models.TextField()
    highlight = models.CharField(max_length=150)
    posted = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        if len(self.title) > 50:
            return self.title[:50] + "..."
        return self.title


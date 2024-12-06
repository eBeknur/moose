from django.core.files.images import ImageFile
from django.db import models
from django.db.models import ImageField, CASCADE


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField( blank=True , null=True)
    image = ImageField(upload_to='posts/')
    author = models.CharField(max_length=100)
    author_image = ImageField(upload_to='posts_author/')
    author_positions = models.CharField(max_length=100)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    website = models.TextField(max_length=100)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField(max_length=100)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

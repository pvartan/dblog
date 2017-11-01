from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    """создание коротких записией в блог"""

    title = models.CharField(max_length=75)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)
    owner = models.ForeignKey(User)

    public = models.BooleanField()

    bid = models.PositiveIntegerField()

    def __str__(self):
        """возвращает заголовок"""
        return self.title

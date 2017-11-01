from django import forms
from django.utils.text import slugify

from . models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'public', 'bid']
        labels = {'title': '', 'text': '', 'public': 'Make public'}

        def save(self):
            instance = super(BlogPost, self).save(commit=False)
            instance.slug = slugify(instance.title)
            instance.save()
            return instance()
            


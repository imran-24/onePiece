from django.db import models
from django.utils import timezone
from django.utils.text import slugify 
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True,blank=True)
    content = models.TextField()
    time = models.TimeField(default=timezone.now)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self): # new
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
# Create your models here.
from .utils import slugify_instance_title
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True,blank=True)
    content = models.TextField()
    time = models.TimeField(default=timezone.now)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



def article_pre_save(sender, instance, *args, **kwargs):
    print("pre_save")
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):
    print("post_save")
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)
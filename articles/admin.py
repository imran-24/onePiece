from django.contrib import admin

# Register your models here.
from .models import Article
class ArtilceAdmin(admin.ModelAdmin):
    list_display= ['id','title','content','slug','timestamp','updated']
    search_field =['id','title']

admin.site.register(Article,ArtilceAdmin)
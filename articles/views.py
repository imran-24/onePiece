from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import Http404
from .models import Article
from django.db.models import Q
# Create your views here.

from .forms import ModelArticle

def searchArticle(request):
     query = request.GET.get("q")
     qs = Article.objects.all()
     if query is not None:
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        qs = Article.objects.filter(lookups) 
               
     context ={
                    "object_list": qs
              }
     return render(request, "articles/search.html",context=context)

def createArticle(request):
    form = ModelArticle(request.POST or None)
    context = {'form' : form }
    if form.is_valid():
        obj = form.save()
        context['object'] = obj 
        context['created'] = True
        context[form] = ModelArticle()
        return redirect(obj.get_absolute_url())
    return render(request,'createArticle.html',context= context)

def home(request):

    object = Article.objects.all
    context = {"obj" : object }

    return render(request,'home.html',context= context)

def detailed_view(request,slug= None):
    context ={}
    if id is not None: 
        try:
            object = Article.objects.get(slug = slug )
        except Article.DoesNotExist:
            raise Http404
        context = {'object' : object}
        
    return render(request,'detailed_view.html',context = context)
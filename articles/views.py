from django.http.response import Http404
from django.shortcuts import render
from django.http import Http404
from .models import Article

# Create your views here.

from .forms import ModelArticle

def createArticle(request):
    form = ModelArticle(request.POST or None)
    context = {'form' : form }
    if form.is_valid():
        obj = form.save()
        context['object'] = obj 
        context['created'] = True
        context[form] = ModelArticle()
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
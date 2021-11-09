from django.shortcuts import render

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

def detailed_view(request,id= None):
    context ={}
    if id is not None: 
        object = Article.objects.get(id = id )
        context = {'object' : object}

    return render(request,'detailed_view.html',context = context)
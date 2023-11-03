from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.


def index(request):

    articles = Article.objects.all()


    context = {
        'articles' : articles,
    }

    return render(request,'index.html',context)


def create(request):

    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form
    }
    return render(request,'form.html',context)

        
    # 1. get 형태일 때 2. post 형태일떄 3. invalid 형태일때 
    
def delete(request,id):

    article = Article.objects.get(id=id)

    article.delete()

    return redirect('articles:index')
    
def update(request,id):

    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
    }

    return render(request,'form.html',context)

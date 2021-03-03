from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('date')

    return render(request, 'articles/article_list.html', {'articles':articles})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)  # a coluna slug da tabela será buscada com o parâmetro slug passado para o método
    return render(request, 'articles/article_detail.html', {'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)  # files come in another parameter of the request, not in the POST
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)  # commit=False means we will do something else with this before saving.
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
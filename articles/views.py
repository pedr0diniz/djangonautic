from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('date')

    return render(request, 'articles/article_list.html', {'articles':articles})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)  # a coluna slug da tabela será buscada com o parâmetro slug passado para o método
    return render (request, 'articles/article_detail.html', {'article':article})
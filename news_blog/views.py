from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

ARTICLES = [
    {
        'id': 1,
        'title': 'First news',
        'text': 'This is the worst first article'
    },
    {
        'id': 2,
        'title': 'Second news',
        'text': 'This is the amazing second article'
    }]


def index(request):
    return render(request, 'news_blog/news_list.html', {'articles': ARTICLES})


def get_article(request, article_id):
    article = ARTICLES[article_id - 1]
    return render(request, 'news_blog/news_article.html', {'article': article})


def get_about_me(request):
    return render(request, 'news_blog/about.html')

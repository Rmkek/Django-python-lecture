from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Article, Author, Comment


def index(request):
    articles = Article.objects.all().order_by('published_date')

    return render(request, 'news_blog/news_list.html', {'articles': articles})


def get_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        author = Author.objects.filter(article__pk=article_id)
        comment = Comment.objects.filter(article=article)
        print(comment)

    except (Article.DoesNotExist, Author.DoesNotExist):
        return HttpResponseNotFound()

    return render(request, 'news_blog/news_article.html', {'article': article, 'author': author[0], 'comment': comment[0]})


def get_about_me(request):
    return render(request, 'news_blog/about.html')

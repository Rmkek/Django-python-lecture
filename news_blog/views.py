from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.utils import timezone

from .models import Article, Author, Comment

from .forms import ArticleForm, CommentForm


def index(request):
    articles = Article.objects.all().order_by('published_date')

    return render(request, 'news_blog/news_list.html', {'articles': articles})


def get_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        author = Author.objects.filter(article__pk=article_id)[0]
        comments = Comment.objects.filter(article=article)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()

    return render(request, 'news_blog/news_article.html', {'article': article, 'author': author, 'comments': comments})


def get_about_me(request):
    return render(request, 'news_blog/about.html')


def new_article(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            article.save()
            return redirect('article', article_id=article.pk)
    return render(request, 'news_blog/edit_article.html', {'form': form})


def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            article.save()
            return redirect('article', article_id=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'news_blog/edit_article.html', {'form': form})


def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.published_date = timezone.now()
            comment.save()
            return redirect('article', article_id=comment.article_id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'news_blog/edit_comment.html', {'form': form})

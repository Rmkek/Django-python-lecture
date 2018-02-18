from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.get_article, name='article'),
    path('new/', views.new_article, name="new_article"),
    path('<int:article_id>/edit_article', views.edit_article, name="edit_article"),
    path('<int:comment_id>/edit_comment', views.edit_comment, name="edit_comment")
]

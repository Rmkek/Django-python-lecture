from django.db import models
from django.utils import timezone
import uuid


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def remove(self):
        self.delete()

    def __str__(self):
        return '{}'.format(self.title)


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField(max_length=2500, null=False)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Comment by {} in {}'.format(self.author, self.article)

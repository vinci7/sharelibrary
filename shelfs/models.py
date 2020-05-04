from django.db import models


class Book(models.Model):
    douban_book_id = models.IntegerField(null=False)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=10)
    publisher = models.CharField(max_length=50)
    pubdate = models.CharField(max_length=10)
    translator = models.CharField(max_length=200)
    image_small = models.URLField(max_length=200)
    rating_number = models.IntegerField(default=0)
    rating_average = models.SmallIntegerField(default=0)
    tags = models.CharField(max_length=50)
    isbn10 = models.CharField(max_length=10)
    isbn13 = models.CharField(max_length=13)
    url = models.URLField(max_length=200)
    catalog = models.TextField()
    author_intro = models.TextField()
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

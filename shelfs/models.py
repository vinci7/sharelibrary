from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    station = models.CharField(max_length=100)
    
    def __str__(self):
        return '{} ({})'.format(self.user.username, self.area)

class Book(models.Model):
    douban_book_id = models.IntegerField(null=False)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=10)
    publisher = models.CharField(max_length=50)
    pubdate = models.CharField(max_length=10)
    translator = models.CharField(max_length=200)
    douban_small_image_url = models.URLField(max_length=200)
    image_url = models.URLField(max_length=200, default="")
    rating_number = models.IntegerField(default=0)
    rating_average = models.SmallIntegerField(default=0)
    tags = models.CharField(max_length=50)
    isbn10 = models.CharField(max_length=10)
    isbn13 = models.CharField(max_length=13)
    url = models.URLField(max_length=200)
    catalog = models.TextField()
    author_intro = models.TextField()
    summary = models.TextField()
    price = models.CharField(max_length=15, default="")
    pages = models.IntegerField(default=0)
    owners = models.ManyToManyField(UserProfile)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ({})'.format(self.title, self.author)

    def bind(self, bookDict):
        self.douban_book_id = bookDict['id']
        self.title = bookDict['title']
        self.subtitle = bookDict['subtitle']
        self.author = ';'.join(bookDict['author'])
        self.publisher = bookDict['publisher']
        self.pubdate = bookDict['pubdate']
        self.translator = ';'.join(bookDict['translator'])
        self.douban_small_image_url = bookDict['images']['small']
        self.rating_number = bookDict['rating']['numRaters']
        self.rating_average = int(float(bookDict['rating']['average'])*10)
        self.tags = bookDict['tags'][0]['title']
        self.isbn10 = bookDict['isbn10']
        self.isbn13 = bookDict['isbn13']
        self.url = bookDict['url']
        self.catalog = bookDict['catalog']
        self.author_intro = bookDict['author_intro']
        self.summary = bookDict['summary']
        self.price = bookDict['price']
        self.pages = bookDict['pages']

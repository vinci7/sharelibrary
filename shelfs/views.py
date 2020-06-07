from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Book, UserProfile
from . import utils

# Create your views here.

@login_required
def index(request):
    books = Book.objects.values('title', 'tags', 'author', 'url', 'douban_small_image_url', 'rating_average', 'rating_number', 'isbn13')
    for book in books:
        showStar = {
            'full': round(book['rating_average']/10)//2,
            'half': round(book['rating_average']/10) % 2,
            'empty': 5 - (round(book['rating_average']/10)//2 + round(book['rating_average']/10) % 2)
        }
        book['showStar'] = showStar
    context = {
        'books': books,
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect("index")
        else:
            template = loader.get_template('login.html')
            return HttpResponse(template.render(None, request))
    elif request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.add_message(request, messages.WARNING, 'Error, the user is not existed.')
            return redirect("login")


@login_required
def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, 'logout success')
    return redirect("login")


@login_required
def shelf(request):
    template = loader.get_template('shelf.html')
    return HttpResponse(template.render(None, request))

@login_required
def profile(request):
    template = loader.get_template('profile.html')
    user = User.objects.get(id = request.user.id)
    books = user.book_set.all()
    context = {
        'user': user,
        'books': books,
    }
    return HttpResponse(template.render(context, request))

@login_required
def profile_by_id(request, id):
    template = loader.get_template('profile.html')
    try:
        user = User.objects.get(id = id)
        books = user.book_set.all()
    except User.DoesNotExist:
        raise Http404("User does not exist.")
    context = {
        'user': user,
        'books': books,
    }
    return HttpResponse(template.render(context, request))


@login_required
def book(request, isbn):
    template = loader.get_template('book.html')
    try:
        book = Book.objects.get(isbn13 = isbn)
    except Book.DoesNotExist:
        raise Http404("Book does not exist.")

    showStar = {
        'full': round(book.rating_average/10)//2,
        'half': round(book.rating_average/10) % 2,
        'empty': 5 - (round(book.rating_average/10)//2 + round(book.rating_average/10) % 2)
    }
    book.showStar = showStar
    owners = book.owners.all()

    context = {
        'user': request.user,
        'book': book,
        'owners': owners,
    }
    
    return HttpResponse(template.render(context, request))


@login_required
def isbn(request):
    user = request.user
    if request.method == 'GET':
        template = loader.get_template('isbn.html')
        return HttpResponse(template.render(None, request))
    elif request.method == 'POST':
        isbn = request.POST['isbn']
        if utils.get_by_isbn(user, isbn) != None:
            messages.add_message(request, messages.SUCCESS, 'add success')
            return redirect("isbn")
        else:
            messages.add_message(request, messages.ERROR, 'add failed')
            return redirect("isbn")

@login_required
def get_by_isbn(request, isbn):
    user = request.user
    return HttpResponse(utils.get_by_isbn(user, isbn))

def ping(request):
    user = request.user
    print(user)
    print(user.id)
    print(type(user))
    user = UserProfile.objects.get(id = user.id)
    print(user)
    return HttpResponse("pong")

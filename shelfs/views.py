from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(None, request))


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
    return HttpResponse(template.render(None, request))

@login_required
def isbn(request):
    template = loader.get_template('isbn.html')
    return HttpResponse(template.render(None, request))

def get_by_isbn(request, isbn):
    return HttpResponse(isbn)

def ping(request):
    return HttpResponse("pong")

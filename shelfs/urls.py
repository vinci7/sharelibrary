from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('isbn', views.isbn, name='isbn'),
    path('shelf', views.shelf, name='shelf'),
    path('get_by_isbn/<int:isbn>', views.get_by_isbn, name='get_by_isbn'),

    path('ping', views.ping, name='ping'),
]

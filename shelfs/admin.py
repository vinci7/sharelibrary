from django.contrib import admin
from .models import Book, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Book)
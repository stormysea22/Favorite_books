from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from login_app.models import User
from book_app.models import Book



# Create your views here.
class BookList(ListView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'description']
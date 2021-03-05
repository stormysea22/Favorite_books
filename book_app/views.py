from django import template
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from login_app.models import User
from book_app.models import Book
register = template.Library()


# Create your views here.
class BookList(ListView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.uploaded_by = User.objects.get(id=self.request.session['user_id'])
        return super().form_valid(form)

class BookEdit(UpdateView):
    model = Book
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.uploaded_by = User.objects.get(id=self.request.session['user_id'])
        return super().form_valid(form)

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

def book_detail(request, book_id):
    context= {
        'book' : Book.objects.get(id=book_id),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'book_app/book_detail.html', context)

def make_favorite(request, book_id):
    User.objects.get(id=request.session['user_id']).liked_books.add(book_id)
    return redirect('books_detail', book_id=book_id)

def un_favorite(request, book_id):
    User.objects.get(id=request.session['user_id']).liked_books.remove(book_id)
    return redirect('books_detail', book_id=book_id)

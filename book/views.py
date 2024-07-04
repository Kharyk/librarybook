
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import LibraryBook
from .forms import BookForm

class BookListView(ListView):
    model = LibraryBook
    template_name = 'book_list.html'

class BookDetailView(DetailView):
    model = LibraryBook
    template_name = 'book_detail.html'

class AddBookView(CreateView):
    model = LibraryBook
    form_class = BookForm
    template_name = 'add_book.html'

class EditBookView(UpdateView):
    model = LibraryBook
    form_class = BookForm
    template_name = 'edit_book.html'

class DeleteBookView(DeleteView):
    model = LibraryBook
    template_name = 'delete_book.html'
    success_url = '/books/'
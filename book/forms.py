from django import forms
from book.models import LibraryBook

class BookForm(forms.ModelForm):
    class Meta:
        model = LibraryBook
        fields = ('title', 'author', 'publication_date', 'isbn', 'publisher', 'description')
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from books.models import get_books


def book(request):
    books = get_books

    return render(request, 'books.html', {
        'books': books
    })

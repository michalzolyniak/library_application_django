from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from books.models import get_books, get_book_detail


def book(request):
    books = get_books

    return render(request, 'books.html', {
        'books': books
    })


def book_details(request, book_id):
    book_data = get_book_detail(book_id)

    return render(request, 'book_details.html', {
        'book_details': book_data
    })

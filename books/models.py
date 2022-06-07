from django.db import models

RATING = ((1, "*"),
          (2, "**"),
          (3, "***"),
          (4, "****"),
          (5, "*****"),)


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=64, null=False)


def get_authors():
    return Author.objects.all()


class Book(models.Model):
    isbn = models.CharField(max_length=13)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    is_loaned = models.BooleanField(default=False)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)


def get_books():
    return Book.objects.all()


def get_book_detail(book_id):
    book_details = Book.objects.all()
    return book_details.filter(id=book_id)


class Category(models.Model):
    name = models.CharField(max_length=64, null=False)
    book_category = models.ManyToManyField(Book)


def get_categories():
    return Category.objects.all()


class Client(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)


def get_clients():
    return Client.objects.all()


class Loan(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)


class Rating(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING)
    comment = models.TextField(null=True)
    date_add = models.DateTimeField(auto_now_add=True)

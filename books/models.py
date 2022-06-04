from django.db import models


# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=13)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    is_loaned = models.BooleanField(default=False)


def get_books():
    return Book.objects.all()


class Author(models.Model):
    name = models.CharField(max_length=64, null=False)


def get_authors():
    return Author.objects.all()


class Category(models.Model):
    name = models.CharField(max_length=64, null=False)


def get_categories():
    return Category.objects.all()


class Client(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)


def get_clients():
    return Client.objects.all()

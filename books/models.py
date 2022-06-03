from django.db import models


# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=13)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    is_loaned = models.BooleanField(default=False)


def get_books():
    return Book.objects.all()

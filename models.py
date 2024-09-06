from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)  # Title of the book
    author = models.CharField(max_length=100)  # Author of the book

    def __str__(self):
        return self.title  # This will display the book title in the Django admin or when queried

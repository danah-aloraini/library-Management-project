from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    #requirement 5: many-to-many relationship between users and books
    reserved_by = models.ManyToManyField(User, blank=True, related_name="reserved_books")

    def __str__(self):
        return self.title
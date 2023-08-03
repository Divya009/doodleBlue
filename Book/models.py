from django.db import models

# Create your models here.

class Book(models.Model):
	book_name = models.TextField()
	book_genre = models.CharField(max_length=128)
	published_at = models.DateTimeField()
	added_datetime = models.DateTimeField(auto_now_add=True)
	updated_datetime = models.DateTimeField(auto_now=True)
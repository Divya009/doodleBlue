from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings

from rest_framework import generics

from Book.models import Book
from Book.serializers import BookSerializer

class BookView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

	@method_decorator(cache_page(settings.CACHE_IN_TIMEOUT))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)
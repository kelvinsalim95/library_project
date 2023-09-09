from django.conf import settings
from src.book.serializer import BookSerializer
from src.user.models import User
from rest_framework.exceptions import APIException
from django.core.exceptions import ObjectDoesNotExist


class BookService:
    def __init__(self, request , username):
        self.request = request
        self.username = username
  
    def create(self):
        if User.isUserLibrarian(self.username) == False:
            raise APIException('You need to be a librarian to add a new book')

        serializer = BookSerializer(data=self.request)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return serializer.data
        

from rest_framework import  viewsets, response, status, mixins
from src.book.serializer import BookSerializer
from src.book.services import BookService
from src.book.models import Book
from src.user.models import User
from rest_framework.exceptions import APIException


class BookViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    
    serializer_class = BookSerializer

    def list(self, request, *args, **kwawrgs):
        username = request.META.get('HTTP_USERNAME')

        if User.isUserLibrarian(username) == False:
            raise APIException('You need to be a librarian to check book list')
        
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def create(self, request, *args, **kwawrgs):
        username = request.META.get('HTTP_USERNAME')
        print(username)
        bookService = BookService(request.data, username)
        result = bookService.create()
        return response.Response({'status_code': 201, 'data': result}, status=status.HTTP_201_CREATED)
    
    
   

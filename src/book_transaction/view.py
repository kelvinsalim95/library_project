from rest_framework import  viewsets, response, status, mixins
from src.book_transaction.serializer import BorrowedBookSerializer
from src.book.serializer import BookSerializer
from src.book_transaction.models import BorrowedBook
from src.book_transaction.services import BorrowedBookService
from src.user.models import User
from rest_framework.exceptions import APIException
import json


class BorrowedBookViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    
    serializer_class = BorrowedBookSerializer

    def list(self, request, *args, **kwawrgs):
        username = request.META.get('HTTP_USERNAME')

        if username is None :
            title =request.data.get("title")
            if title is None:
                raise APIException('need provide title!')
            borrowedBookService = BorrowedBookService(request.data)
            queryset = borrowedBookService.checkBookByTitle()
            if queryset is None:
                 queryset = BorrowedBook.objects.filter(book = title).order_by("return_date").first()
                 return response.Response({"Message": f"the book that you are looking for is not available right now", "available_in": f"{queryset.return_date}"},  status=status.HTTP_200_OK)
            serializer = BookSerializer(queryset, many=True)
            return response.Response(serializer.data)
    

        if User.isUserLibrarian(username):
            queryset = BorrowedBook.objects.all()
        
        if User.isUserStudent(username):
            queryset = BorrowedBook.objects.filter(user_mapper = username)

    
        serializer = BorrowedBookSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def create(self, request, *args, **kwawrgs):
        username = request.META.get('HTTP_USERNAME')
        if User.isUserLibrarian(username) == False:
            raise APIException('You need to be a librarian to add a new book')
        
        borrowedBookService = BorrowedBookService(request.data)
        result = borrowedBookService.create()
        return response.Response({'status_code': 201, 'data': result}, status=status.HTTP_201_CREATED)
    
    def put(self, request):
        username = request.META.get('HTTP_USERNAME')
        borrowedBookService = BorrowedBookService(request.data)
        is_return = request.data.get("is_return")
        is_renew  = request.data.get("is_renew")

        if is_return is not None:
            if User.isUserLibrarian(username):
                borrowedBookService.returnBook()
            else:
                raise APIException('username is invalid')
        
        if is_renew is not None:
            if User.isUserStudent(username):
                borrowedBookService.renewBorrowedBook(username=username)
            else:
                raise APIException('username is invalid')
    
        return response.Response({'status_code': 200, 'data': 'success'}, status=status.HTTP_200_OK)
        

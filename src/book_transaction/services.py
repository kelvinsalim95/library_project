from django.conf import settings
from src.book_transaction.serializer import BorrowedBookSerializer
from src.user.models import User
from rest_framework.exceptions import APIException
from django.core.exceptions import ObjectDoesNotExist
from src.book_transaction.models import BorrowedBook
from src.book.models import Book
from django.utils import timezone
from datetime import timedelta


class BorrowedBookService:
    def __init__(self, request):
        self.request = request
  
    def create(self):
        serializer = BorrowedBookSerializer(data=self.request)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return serializer.data
        
    def renewBorrowedBook(self, username):
        id = self.request.get("id")
        is_renew = self.request.get("is_renew", False)
        record = BorrowedBook.objects.filter(id = id, user_mapper=username).first()
        if record is not None:            
            if record.is_renewed == True and is_renew == True:
                raise APIException("You already have renew this once and it cannot be renew again")
            
            record.return_date = record.return_date + timedelta(days=30)
            record.is_renewed = is_renew

            result = record.save()
            return self.request
        else:
            raise APIException('Record that you are looking for not found')
    
    def returnBook(self):
        id = self.request.get("id")
        is_return = self.request.get("is_return", False)
        record = BorrowedBook.objects.filter(id = id).first()
        record.is_return = is_return
        result = record.save()
        return self.request
    
    def checkBookByTitle(self):
        serializer = BorrowedBookSerializer(data=self.request)
        title = self.request.get("title")
        if serializer.checkAvailableBook(title):
            book = Book.objects.filter(title= title).first()
            borrowedBookCount = BorrowedBook.objects.filter(book = title, is_return=False).count()
            if book == None:
                raise APIException("Book That you are Trying to book is not available")

            book_available = book.copies_available
            book.copies_available = book_available - borrowedBookCount
            print(book_available - borrowedBookCount)
            return {book}

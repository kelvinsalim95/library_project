from rest_framework import serializers
from .models import BorrowedBook
from src.book.models import Book
from rest_framework.exceptions import APIException
from django.utils import timezone
from datetime import timedelta
from src.user.models import User


class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = '__all__'  # Include all fields in the serializer
    
    def create(self, validated_data):
        borrowed_date = timezone.now()
        return_date = borrowed_date + timedelta(days=30)
        user = validated_data.get('user_mapper', None)
        book = validated_data.get('book', None)
        if User.isUserStudent(username=user):
            if self.checkAvailableBook(book):
                borrowedBook, created = BorrowedBook.objects.update_or_create(
                    book=validated_data.get('book', None),
                    user_mapper=user,
                    borrowed_date = borrowed_date,
                    return_date = return_date,
                    defaults={
                        'book': validated_data.get('book', None),
                        'user_mapper': user,
                        'borrowed_date': borrowed_date,
                        'return_date': return_date,
                    })
            
                if created:
                    return borrowedBook
                else:
                    raise APIException("Error while trying to creat book")
            else:
                raise APIException("Book is not available for now")
        else:   
            raise APIException("Student doesn't exist")

        
    def checkAvailableBook(self, title):
        book = Book.objects.filter(title= title).first()
        borrowedBookCount = BorrowedBook.objects.filter(book = title, is_return=False).count()
        if book == None:
            raise APIException("Book That you are Trying to book is not available")
    
        book_available = book.copies_available
        if book_available > borrowedBookCount:
            return True

        return False

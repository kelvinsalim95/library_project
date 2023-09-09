from django.urls.conf import include
from rest_framework import routers
from django.urls import path, include
from src.user.view import CreateUserViewSet
from src.book.view import BookViewSet
from src.book_transaction.view import BorrowedBookViewSet
from django.urls import path, include


router = routers.DefaultRouter(trailing_slash=False)
router.register('user',  viewset=CreateUserViewSet, basename ='create_user')
router.register('book',  viewset=BookViewSet, basename ='book')
router.register('borrowBook',  viewset=BorrowedBookViewSet, basename ='borrowBook')

urlpatterns =[
    path('' , include(router.urls))
]

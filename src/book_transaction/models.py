from django.db import models
from src.book.models import Book
from src.user.models import User
from src.utils.models import TimeTrackedModel
from django.utils import timezone
from datetime import timedelta

class BorrowedBook(TimeTrackedModel):
    book = models.CharField(max_length=100)
    user_mapper = models.CharField(max_length=100)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)
    is_return = models.BooleanField(default=False)
    is_renewed = models.BooleanField(default=False)
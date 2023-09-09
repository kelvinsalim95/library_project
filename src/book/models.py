from django.db import models
from src.utils.models import TimeTrackedModel

class Book(TimeTrackedModel):
    title = models.CharField(max_length=100)
    copies_available = models.IntegerField()
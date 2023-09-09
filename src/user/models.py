from django.db import models
from src.utils.models import TimeTrackedModel
from rest_framework.exceptions import APIException
from django.core.exceptions import ObjectDoesNotExist


class User(TimeTrackedModel):
    
    username =  models.CharField(max_length=255, null=False, blank=False, unique=True)
    type =  models.CharField(max_length=255, null=False, blank=False)

    def findUserByIdAndType(username, type):
        return User.objects.filter(username = username, type = type)
    
    def isUserLibrarian(username):
        try:
            user = User.objects.filter(username = username, type = 'librarian')
            if len(user) < 1 :
                return False
            else:
                return True
        except ObjectDoesNotExist:
            raise APIException('You need to be a librarian to add a new book')
        
    def isUserStudent(username):
        try:
            user = User.objects.filter(username = username, type = 'student')
            if len(user) < 1 :
                return False
            else:
                return True
        except ObjectDoesNotExist:
            raise APIException('You need to be a librarian to add a new book')
    
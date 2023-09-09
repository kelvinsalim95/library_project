from django.conf import settings
from src.user.serializer import UserSerializer



class UserService:
    def __init__(self, request):
        self.request = request
    
    def createUser(self):
        serializer = UserSerializer(data=self.request)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return serializer.data
        

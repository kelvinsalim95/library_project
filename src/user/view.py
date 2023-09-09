from rest_framework import  viewsets, response, status, mixins
from src.user.serializer import UserSerializer
from src.user.services import UserService


class CreateUserViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):

    serializer_class = UserSerializer

    def create(self, request, *args, **kwawrgs):
    
        userService = UserService(request.data)
        result = userService.createUser()
        return response.Response({'status_code': 201, 'data': result}, status=status.HTTP_201_CREATED)
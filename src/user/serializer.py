from rest_framework import serializers
from .models import User
from rest_framework.exceptions import APIException


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Include all fields in the serializer
    
    def create(self, validated_data):
        type = validated_data.get('type', None).lower()
        if type != 'student' and type != 'librarian':
            raise APIException("Type needs to be student or librarian")
    
        username, created = User.objects.update_or_create(
            username=validated_data.get('username', None),
            type=type,
            defaults={
                'username': validated_data.get('username', None),
                'type': type
            })
    
        if created:
            return username
        else:
            raise APIException("Error while trying to create User")
     
         
            

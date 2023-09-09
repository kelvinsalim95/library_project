from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import APIException


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields in the serializer
    
    def create(self, validated_data):
        book, created = Book.objects.update_or_create(
            title=validated_data.get('title', None),
            copies_available=validated_data.get('copies_available', None),
            defaults={
                'title': validated_data.get('title', None),
                'copies_available': validated_data.get('copies_available', None),
            })
    
        if created:
            return book
        else:
            print("enter")
            raise APIException("Error while trying to creat book")
     
         
            

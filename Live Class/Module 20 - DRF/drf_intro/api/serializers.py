from rest_framework import serializers
from .models import Task, Book, Author

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = "__all__"
        fields = ['id', 'title', 'description', 'created_at', 'completed']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'author']

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title is too short")
        return value
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'books']
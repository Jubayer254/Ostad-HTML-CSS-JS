from django.shortcuts import render
from django.http import FileResponse # if need to send any file to client
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response
from .models import Task, Author, Book
from .serializers import TaskSerializer, BookSerializer, AuthorSerializer
from rest_framework import status
from rest_framework.exceptions import NotFound, ValidationError

from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from django.shortcuts import get_object_or_404

from  rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission

# Create your views here.

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if obj.id == 1:
            return True
        return False


class OutofStockException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Out of stock'
    default_code = 'out_of_stock'


@api_view(['GET'])
def hello(request):
    return Response ({"messege":"Hello World"})

@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CLASS BASED

class TaskList(APIView):
    # http://127.0.0.1:8000/api/task_list/?q=asd
    def get(self, request):
        # queryset
        print(request.GET.get('q'))
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        # JSON, FORM
        print(request.data)
        # print(request.body)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

@permission_classes([IsAuthenticated, CustomPermission]) 
class TaskDetail(APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            self.check_object_permissions(request, task)
        except Task.DoesNotExist:
            # return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
            # raise NotFound('Task not found')
            raise OutofStockException()
        
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            if "x" in serializer.data['title']:
                raise ValidationError('Title cannot contain x')
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@permission_classes([IsAuthenticated, CustomPermission])
class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    def list(self, request, *args, **kwargs):
        print("This is custome method")
        return super().list(request, *args, **kwargs)
    
    @action(detail=False, methods=['GET','POST'])
    def send_mail(self, request):
        print("Sending mail...")
        return Response({"message":"Mail has been sent"},status=status.HTTP_200_OK)

class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

# VIEW SET
#-----------------#
# List --> GET
# Create --> POST
# Retrieve --> GET
# Update --> PUT
# Partial Update --> PATCH
# Destroy -> DELETE
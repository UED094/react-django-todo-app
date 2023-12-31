from rest_framework import viewsets
from todo_api.serializers import TodoSerializer
from todo.models import Todo


# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

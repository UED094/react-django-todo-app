from django.views.generic import ListView
from todo.models import Todo
from todo_api.serializers import TodoSerializer
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render


class TodoList(ListView):
    model = Todo


def index(request):
    template = loader.get_template('todo/index.html')
    return HttpResponse(template.render())

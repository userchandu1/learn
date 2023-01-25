from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


#
def hello(request):
    return HttpResponse("Hello World! kya baat hai website bana raha launada")


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


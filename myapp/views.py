from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


#
def hello(request):
    return HttpResponse("Hello World! text added to test new branch")


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from list_app.models import Task


# Create your views here.


class TaskList(ListView):
    model = Task


class TaskDetail(DetailView):
    model = Task

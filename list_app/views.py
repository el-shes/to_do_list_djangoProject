from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from list_app.models import Task


# Create your views here.


class TaskList(ListView):
    model = Task


class TaskDetail(DetailView):
    model = Task


class CreateTask(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')

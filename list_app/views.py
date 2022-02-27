from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from list_app.models import Task


# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'list_app/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskList(ListView):
    model = Task


class TaskDetail(DetailView):
    model = Task


class CreateTask(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')


class UpdateTask(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')


class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')

from django.urls import path
from .views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask, CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('', TaskList.as_view(), name="tasks"),
    path('task/<int:pk>', TaskDetail.as_view(), name="task"),
    path('create-task/', CreateTask.as_view(), name="create-task"),
    path('task-update/<int:pk>', UpdateTask.as_view(), name="update-task"),
    path('task-delete/<int:pk>', DeleteTask.as_view(), name="delete-task"),

]
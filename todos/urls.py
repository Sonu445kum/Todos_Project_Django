from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.todo_create, name="todo_create"),
    path("edit/<int:pk>/", views.todo_edit, name="todo_edit"),
    path("delete/<int:pk>/", views.todo_delete, name="todo_delete"),
]

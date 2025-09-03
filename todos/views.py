from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Todo
from .forms import TodoForm

@login_required
def home(request):
    # Home page lists todos + create/edit/delete buttons
    todos = Todo.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "todos/home.html", {"todos": todos})

@login_required
def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, "Todo created")
            return redirect("todos:home")
    else:
        form = TodoForm()
    return render(request, "todos/todo_form.html", {"form": form})

@login_required
def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo updated")
            return redirect("todos:home")
    else:
        form = TodoForm(instance=todo)
    return render(request, "todos/todo_form.html", {"form": form, "todo": todo})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == "POST":
        todo.delete()
        messages.success(request, "Todo deleted")
        return redirect("todos:home")
    return render(request, "todos/todo_confirm_delete.html", {"todo": todo})
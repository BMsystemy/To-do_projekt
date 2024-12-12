from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required


def task_list(request):
    filter_param = request.GET.get('filter', 'all')  # Domyślny filtr to "wszystkie"

    # Filtrujemy zadania dla zalogowanego użytkownika
    tasks = Task.objects.filter(user=request.user)

    if filter_param == 'completed':  # Jeśli filtr to "zrobione"
        tasks = tasks.filter(completed=True)
    elif filter_param == 'todo':  # Jeśli filtr to "do zrobienia"
        tasks = tasks.filter(completed=False)

    return render(request, 'todo/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/edit_task.html', {'form': form, 'task': task})
def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed  # Zmień status na przeciwny
    task.save()
    return redirect('task_list')  # Przekieruj z powrotem na listę zadań

def change_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.completed = 'completed' in request.POST
        task.save()
    return redirect('task_list')
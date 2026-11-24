from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Display all tasks and add a new task
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            Task.objects.create(title=title)

        return redirect('home')

    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})


# Update task
def update_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('home')

    return render(request, 'update.html', {'task': task})


# Delete task
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()

    return redirect('home')
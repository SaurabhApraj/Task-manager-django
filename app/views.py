from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from app.forms import TasksForm
from .models import Tasks
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    return render(request, 'app/index.html')

def task(request):
    tasklist = Tasks.objects.all()
    task_paginator = Paginator(tasklist, 5)
    page_num = request.GET.get('page')
    task = task_paginator.get_page(page_num)
    return render(request, 'app/task.html', {'task': task})

def taskdetail(request, id):
    taskdetail = Tasks.objects.get(pk=id)
    return render(request, 'app/taskdetail.html', {'taskdetail': taskdetail})

def edittask(request, id):
    taskedit = Tasks.objects.get(pk=id)
    return render(request, 'app/edittask.html')


def createtask(request):
    form = TasksForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TasksForm()
    context ={
        'form':form
    }
    return render(request, 'app/createtask.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('TaskPage')
        else:
            messages.info(request, 'Username OR Password is incorrect')
            return render(request, 'app/index.html')
    return render(request, 'app/login.html')
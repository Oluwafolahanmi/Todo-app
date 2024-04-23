from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def sqi_home(request):
    todos = Todo.objects.all()
    form = TodoForm()
    context = {'todos': todos, 'form': form}
    return render(request, 'index1.html', context)

def addform(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        newtodo=Todo(text=request.POST['text'])
        newtodo.save()
    return redirect('sqi')

def paid(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.status= True
    todo.save()
    return redirect('sqi') 

def deletepaid(request):
    todo = Todo.objects.filter(status=True).delete()
    return redirect('sqi')

def deleteunpaid(request):
    todo = Todo.objects.filter(status=False).delete()
    return redirect('sqi')

def deleteall(request):
    todo = Todo.objects.all().delete()
    return redirect('sqi')
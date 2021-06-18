from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoItem

# Create your views here.
def ViewTodo(request):
    all_todo_item = TodoItem.objects.all()
    return render(request, 'index.html',
    {'all_items' : all_todo_item})

def TodoAdd(request):
    item_baru = TodoItem(context = request.POST['context'])
    item_baru.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_delete = TodoItem.objects.get(id=todo_id)
    item_delete.delete()
    return HttpResponseRedirect('/todo/')
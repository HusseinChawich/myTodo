from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import listItems
from todoList.models import task

# Create your views here.

def v_listItems(request):
    myListItems = listItems.objects.all().values()
    template = loader.get_template('itemList.html')
    context = {
        'ListItems': myListItems,
    }
    return HttpResponse(template.render(context,request))

def v_tasks(request, filter_id):
    myTasks = task.objects.filter(listName=filter_id).values()
    template = loader.get_template('tasks.html')
    context = {
        'tasks': myTasks,
    }
    return HttpResponse(template.render(context,request))
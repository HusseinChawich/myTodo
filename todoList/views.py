from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import listItems, task

# Create your views here.

def v_listItems(request):
    myListItems = listItems.objects.all().values()
    template = loader.get_template("itemList.html")
    context = {
        'ListItems': myListItems,
    }
    return HttpResponse(template.render(context,request))
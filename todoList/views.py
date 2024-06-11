from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import listItems, task

from .serializers import listItemsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import listItemsForm

# Create your views here.

def v_listItems(request):
    result = listItems.objects.all()
    serializers = listItemsSerializer(result, many=True)
    #myListItems = listItems.objects.all().values()
    template = loader.get_template('itemList.html')
    context = {
        'ListItems': serializers.data,
    }
    return HttpResponse(template.render(context,request))

def v_tasks(request, filter_id):
    myTasks = task.objects.filter(listName=filter_id).values()
    template = loader.get_template('tasks.html')
    context = {
        'tasks': myTasks,
    }
    return HttpResponse(template.render(context,request))

class listItemsView(APIView):
    def get(self, request, *args, **kwargs):
        result = listItems.objects.all()
        serializers = listItemsSerializer(result, many=True)
        return Response({'status':'success',"listItems":serializers.data}, status=200)

    def post(self, request):
        serializers = listItemsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'status':'success',"data":serializers.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status':'error',"data":serializers.errors}, status=status.HTTP_400_BAD_REQUEST)

def add_item(request):
    form = listItemsForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, 'add_item.html', context)
from django.contrib import admin
from .models import listItems, task
from .forms import listItemsForm, taskForm

# Register your models here.

class listItemsAdmin(admin.ModelAdmin):
    list_display = ['name']
    form = listItemsForm
    # list_filter = ['name']
    search_fields = ['name']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['listName', 'dateCreated', 'taskText', 'finishedAt']
    form = taskForm
    list_filter = ['dateCreated']
    search_fields = ['taskText']


admin.site.register(listItems, listItemsAdmin)
admin.site.register(task, TaskAdmin)
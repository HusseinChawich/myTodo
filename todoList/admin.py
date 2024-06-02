from django.contrib import admin
from .models import listItems, task

# Register your models here.
admin.site.register(listItems)
admin.site.register(task)
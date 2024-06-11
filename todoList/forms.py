from django import forms
from .models import listItems, task

class listItemsForm(forms.ModelForm):
    class Meta:
        model = listItems
        fields = ['name']

class taskForm(forms.ModelForm):
    class Meta:
        model = task
        # fields = ['dateCreated', 'taskText']
        fields = '__all__'
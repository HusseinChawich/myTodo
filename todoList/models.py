from django.db import models

# Create your models here.
class listItems(models.Model):
    name = models.CharField(max_length=50)

class task(models.Model):
    listName = models.ForeignKey(listItems, on_delete=models.CASCADE)
    dateCreated = models.DateField(initial = today, required = True)
    taskText = models.CharField(max_length=max, required = True)
    complete = models.BinaryField(default=0)
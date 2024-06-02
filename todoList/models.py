from django.db import models

# Create your models here.
class listItems(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class task(models.Model):
    listName = models.ForeignKey(listItems, on_delete=models.CASCADE)
    dateCreated = models.DateField()
    taskText = models.CharField(max_length=200)
    finishedAt = models.DateTimeField()

    def __str__(self):
        return f"{self.dateCreated} {self.taskText} {self.finishedAt}"
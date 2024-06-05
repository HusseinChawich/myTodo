from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.v_listItems, name='listItems'),
    path('todo/tasks/<int:filter_id>', views.v_tasks, name='tasks')
]
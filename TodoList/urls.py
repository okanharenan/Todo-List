from django.urls import path
from TodoList.views import TodoListAndCreate

urlpatterns = [
    path('todo/', TodoListAndCreate.as_view())
]
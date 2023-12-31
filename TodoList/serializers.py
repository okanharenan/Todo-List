from rest_framework import serializers
from TodoList.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id","name","done","created_at"]
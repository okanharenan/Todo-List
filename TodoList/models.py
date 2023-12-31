from django.db import models

#criando um model para API
class Todo(models.Model):
    name = models.CharField(max_length=150)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

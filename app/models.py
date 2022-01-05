from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    status_choice = (
        (0, 'Not Completed'),
        (1, 'Completed'),
    )
    task_name = models.CharField(max_length=100)
    status = models.IntegerField(choices=status_choice)
    owner_id = models.ForeignKey(User,on_delete=models.CASCADE, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name

class Subtasks(models.Model):
    subtask_name = models.CharField(max_length=100)
    task_id = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.subtask_name
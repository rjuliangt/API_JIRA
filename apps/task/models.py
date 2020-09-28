# Django imports for create models
from django.db import models


# Create the model for Jira tasks
class Task(models.Model):
    """
    The tasks have the attributes of: task name , status (default='Por hacer' ,'Haciendo','Hecho')
    and an responsible user
    """
    STATUS_OPTIONS = (
        (0, 'To Do'),
        (1, 'Doing'),
        (2, 'Done'),
    )
    task_name = models.CharField(max_length=70)
    status = models.CharField(default='To Do', choices=STATUS_OPTIONS)
    create_date = models.DateField()

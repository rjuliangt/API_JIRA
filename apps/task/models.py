# Django imports for create models
from django.db import models
from apps.user.models import User


# Create the model for Jira tasks
class Task(models.Model):
    """
    The tasks have the attributes of: task name , status (default='To Do' ,'Doing','Done')
    and a manager user, also creation one to many relationship from user to task,
    to enter a state you can use indexes from 0 to 2 (0 = to do, 1 = doing, 2 = done)
    """
    STATUS_OPTIONS = (
        ('To Do', 'To Do'),
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    )
    task_name = models.CharField(max_length=100)
    status = models.CharField(default='To Do', choices=STATUS_OPTIONS, max_length=10)
    create_date = models.DateField(auto_now_add=True)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{0},{1},{2},{3},{4}'.format(self.id, self.task_name, self.status, self.create_date, self.fk_user)

# Django imports for create models
from django.db import models


# Create the model for Jira users
class User(models.Model):
    USER_ROLE = (
        ('Resp', 'Responsible'),
        ('Admin', 'Administrator'),
    )
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=95)
    role = models.CharField(choices=USER_ROLE)
    password = models.CharField()

# Django imports for create models
from django.db import models


# Create the model for Jira users
class User(models.Model):
    """
    The user can have one of the following roles (responsible or administrator),
    will have names and surnames, email, password
    """
    USER_ROLE = (
        ('Manager', 'Manager'),
        ('Admin', 'Administrator'),
    )
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=95)
    password = models.CharField(max_length=30)
    create_date = models.DateField(auto_now=True)
    role = models.CharField(choices=USER_ROLE, max_length=15)

    def __str__(self):
        return '{0},{1},{2},{3},{4},{5},{6}'.format(self.id, self.first_name, self.last_name, self.email,
                                                    self.password, self.create_date, self.role)

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_responsible = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def get_responsible_profile(self):
        responsible_profile = None
        if hasattr(self, 'responsible'):
            responsible_profile = self.responsible
        return responsible_profile

    def get_admin_profile(self):
        admin_profile = None
        if hasattr(self, 'administrator'):
            admin_profile = self.administrator
        return admin_profile

    class Meta:
        db_table = 'auth_user'


class ResponsibleProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)


class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)
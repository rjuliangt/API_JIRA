# Generated by Django 3.1.1 on 2020-09-29 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('task', '0003_auto_20200928_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='fk_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]

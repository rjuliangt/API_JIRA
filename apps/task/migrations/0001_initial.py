# Generated by Django 3.1.1 on 2020-09-29 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=70)),
                ('status', models.CharField(choices=[(0, 'To Do'), (1, 'Doing'), (2, 'Done')], default='To Do', max_length=10)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('fk_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
# imports of rest_framework
from rest_framework import serializers
# import of models
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Creation of task model serialization and all attribs
    """
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'status', 'create_date', 'fk_user', 'fk_owner']

    def create(self, validated_data):
        instance = Task()
        instance.task_name = validated_data.get('task_name')
        instance.status = validated_data.get('status')
        instance.create_date = validated_data.get('create_date')
        instance.fk_user = validated_data.get('fk_user')
        instance.owner = validated_data.get('fk_owner')
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.task_name = validated_data.get('task_name', instance.task_name)
        instance.status = validated_data.get('status', instance.status)
        instance.create_date = validated_data.get('create_date', instance.create_date)
        instance.fk_user = validated_data.get('fk_user', instance.fk_user)
        instance.fk_owner = validated_data.get('fk_owner', instance.fk_owner)
        instance.save()
        return instance

    # function to validate if there is a task with same task name
    def validate(self, data):
        user = Task.objects.filter(task_name=data)
        if len(user) != 0:
            raise serializers.ValidationError('This task name already exists.')
        else:
            return data

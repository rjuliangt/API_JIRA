from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Creation of user model serialization
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'create_date', 'role']

    def create(self, validated_data):
        instance = User()
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.email = validated_data.get('email')
        instance.password = validated_data.get('password')
        instance.create_date = validated_data.get('create_date')
        instance.role = validated_data.get('role')
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.create_date = validated_data.get('create_date', instance.create_date)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance

    # function to validate if there is a task with same task name
    def validate(self, data):
        user = User.objects.filter(email=data)
        if len(user) != 0:
            raise serializers.ValidationError('This task name already exists.')
        else:
            return data

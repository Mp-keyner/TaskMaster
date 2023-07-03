from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ('id', 'name', 'description', 'done')
        fields = '__all__'

from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    price = serializers.CharField(max_length=64)
    period = serializers.CharField(max_length=64)

    class Meta:
        model = Service
        fields = '__all__'

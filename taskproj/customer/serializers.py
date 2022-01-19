from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(max_length=50)
    phonenumber = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=64)

    class Meta:
        model = Customer
        fields = ('__all__')

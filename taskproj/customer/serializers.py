from rest_framework import serializers
from .models import Customer, CustomerService


class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    identity_number = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=64)
    address = serializers.CharField(max_length=50)
    location = serializers.CharField(max_length=64)

    class Meta:
        model = Customer
        fields = ('__all__')


class CustomerServiecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerService
        fields = ('__all__')

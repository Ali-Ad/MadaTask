from .serializers import CustomerSerializer
from .models import Customer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render





class CustomerList(ViewSet):

    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data )


    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(item)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            item = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


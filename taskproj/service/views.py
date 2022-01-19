from django.shortcuts import render
from django.http import HttpResponse
from .models import Service
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ServiceSerializer


class ServicesView(APIView):
    def get(self, request, id=None):
        if id:
            service = Service.objects.get(id=id)
            serializer =ServiceSerializer(service)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

from .serializers import ServiceSerializer
from .models import Service
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render

from .forms import InputForm

def create_view(request):

    context = {}
    form = InputForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "index.html", context)

class Servicelist(ViewSet):

    def list(self, request):
        queryset = Service.objects.all()
        serializer = ServiceSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = Service.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ServiceSerializer(item)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            item = Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)

    def update(self, request, pk=None):
        try:
            item = Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            return Response(status=404)
        serializer = ServiceSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

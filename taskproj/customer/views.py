from .serializers import CustomerSerializer
from .models import Customer
from .serializers import CustomerSerializer,CustomerServiecsSerializer
from .models import Customer ,CustomerService
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.shortcuts import render ,redirect
from .forms import InputForm
from .forms import InputForm


def create_customer(request):

    context = {}
    form = InputForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "index.html", context)

def list_view(request):
    context = {}
    form = InputForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "index.html", context)

class CustomerList(ViewSet):

    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(status=404)
        serializer = CustomerSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


# for customerservice == >>>

def create_views(request):

    context = {}
    form = CustomerServicesForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "index.html", context)



class CustomerService(ViewSet):

    def list(self, request):
        queryset = CustomerService.objects.all()
        serializer = CustomerServiecsSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = CustomerService.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CustomerServiecsSerializer(item)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            item = CustomerService.objects.get(pk=pk)
        except CustomerService.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)

    def update(self, request, pk=None):
        try:
            item = CustomerService.objects.get(pk=pk)
        except CustomerService.DoesNotExist:
            return Response(status=404)
        serializer = CustomerServiecsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


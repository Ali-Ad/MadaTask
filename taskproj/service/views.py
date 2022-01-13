from django.shortcuts import render
from django.http import HttpResponse
from .models import Service


def add(request):
    sname = request.GET.get('sname')
    sprice = request.GET.get('sprice')
    speriod = request.GET.get('speriod')
    namex =Service.objects.filter(sname=sname).exists() 
    if(namex!=True):
        Service.objects.create(sname=sname,sprice=sprice,speriod=speriod)
        return HttpResponse('sucess')
    else:
        return HttpResponse('already exist')


    

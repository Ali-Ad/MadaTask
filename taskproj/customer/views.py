from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.core import serializers

from service.models import Service

from .models import Customer


def addcustomer(request):
    fullname= request.GET.get('fullname')
    phonenumber =request.GET.get('phonenumber')
    email =request.GET.get('email')
    address = request.GET.get('address')
    userexist =Customer.objects.filter(fullname=fullname).exists() 
    if (userexist!=None):
        Customer.objects.create(fullname=fullname,phonenumber=phonenumber ,email=email ,address=address)
        return HttpResponse('customer added Successfully')
    else:
        return HttpResponse('customer username already exist')



def search(request):
    fullname = request.GET.get('fullname')
    userexist =Customer.objects.filter(fullname=fullname).exists() 
    if(userexist!=None):
        data = serializers.serialize('json', Customer.objects.filter(fullname=fullname))
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponse('no customer with this name ')

def edit(request):
    fullname = request.GET.get('fullname')
    newName =request.GET.get('newName')
    newPhonenumber =request.GET.get('newPhonenumber')
    newEmail =request.GET.get('newEmail')
    newAddress = request.GET.get('newAddress')
    userexist = Customer.objects.filter(fullname=fullname).exists()
    if(userexist!=None):
        Customer.objects.filter(fullname=fullname).update(fullname=newName,phonenumber=newPhonenumber,email=newEmail,address=newAddress)
        return HttpResponse('Edit Successfully')
    else:
        return HttpResponse('no value')

def delete(request):
    fullname = request.GET.get('fullname')
    userexist =Customer.objects.filter(fullname=fullname).exists()
    if(userexist!=False):
        Customer.objects.filter(fullname=fullname).delete()
        return HttpResponse('done')
    else:
        return HttpResponse("please enter valied username")


def listServ(request):
    data = serializers.serialize('json', Customer.objects.all())
    return HttpResponse(data, content_type='application/json')
    
def addServ(request):
    fullname = request.GET.get('fullname')
    userexist =Customer.objects.filter(fullname=fullname).exists() 
    if (userexist!=None):
      #  Customer.objects.create(fullname=fullname,phonenumber=phonenumber ,email=email ,address=address ,)
        return HttpResponse('customer added Successfully')
    else:
        return HttpResponse('customer username already exist')
    



    

   

    




    

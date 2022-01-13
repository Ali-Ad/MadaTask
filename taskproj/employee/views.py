from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Login

def login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    if(username!=None and password!=None):
        user = get_object_or_404(Login,username=username , password=password)
        if(user!=None):
            return HttpResponse('login successfully')
        else:
            return HttpResponse('ygh,')
        
def add(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    userexist =Login.objects.filter(username=username).exists() 
    if(username!=None and password!=None):
        if(userexist==False):
            Login.objects.create(username=username,password=password)
            return HttpResponse('username && password added successfully')
        return HttpResponse('username already exist')

def update(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    newpassword = request.GET.get('newpassword')
    user = get_object_or_404(Login,username=username , password=password)
    if(username!=None and user!=None):
        Login.objects.update(username=username , password=newpassword)
        return HttpResponse('password update Successfully ')
    else:
        return HttpResponse('username or password does not exist ')

        



 
   


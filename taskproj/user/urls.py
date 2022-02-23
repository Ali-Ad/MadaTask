from django.urls import path, include
from rest_framework import routers
from .views import *

urlpatterns = [
    path('list/', UserListView.as_view()),
    path('about/', AboutUs.as_view())



]

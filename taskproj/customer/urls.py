from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from . import views
from .views import *


router = routers.DefaultRouter()
router.register(r'viewset',  CustomerList,basename='customer')

urlpatterns = [
    path('', include(router.urls)),
    path('create', create_view),


]

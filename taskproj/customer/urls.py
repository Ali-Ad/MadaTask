from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from . import views
from .views import *


router = routers.DefaultRouter()
router.register(r'viewset',  CustomerList,basename='customer')
router.register(r'viewset',  CustomerService,basename='CustomerService')

urlpatterns = [
    path('', include(router.urls)),
    path('create', create_customer),
    path('ee', create_views),




]

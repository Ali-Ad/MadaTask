from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'viewset',  Servicelist,basename='services')

urlpatterns = [
    path('', include(router.urls)),
    path('create', create_view),
]

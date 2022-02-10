from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'viewset',  UserList,basename='UserList')

urlpatterns = [
    path('', include(router.urls)),
    path('create', create_view),
]

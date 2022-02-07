from django.urls import path, include
from rest_framework import routers
from . import views
from .views import CustomerList


router = routers.DefaultRouter()
router.register(r'viewset',  CustomerList,basename='customer')

urlpatterns = [
    path('', include(router.urls)),

]

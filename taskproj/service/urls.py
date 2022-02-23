from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from django.conf import settings

urlpatterns = [

    path('create', create_view),
    path('list/', login_required(ServiceListView.as_view()),name="service_list"),

]

from django.urls import path, include
from rest_framework import routers
from .views import *

urlpatterns = [
    path('list/', UserListView.as_view()),
    path('lock/', TemplateView.as_view(template_name="account/lock.html")),
    path('hh/',login_required(ChangePasswordView.as_view()),name="change_pass"),
    path('ee/',ResetPassView.as_view(),name="reset"),

]

from django.urls import path
from . import views
urlpatterns = [
    path('login',views.login , name='login'),
    path('add' , views.add , name='add'),
    path('update' , views.update ,name='update')
]
from django.urls import path
from . import views
urlpatterns = [
    path('add', views.addcustomer, name='add'),
    path('search',views.search,name='search'),
    path('edit' , views.edit,name='edit'),
    path('delete',views.delete , name='delete'),
    path('listServ',views.listServ ,name='listServ')
]     
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('cliente/<int:ID_CLIENTE>/', views.getCliente, name='getCliente'),
    path('obtener-disponibles/', views.getDisponibles, name='getDisponibles'),
    path('agregarCliente/', views.addCliente, name= 'addCliente'),
    path('agregarArriendo/', views.addArriendo, name= 'addArriendo'),
    #path('inicio/<int:pk>/edit/', views.regis_edit , name ='regis_edit'),
]
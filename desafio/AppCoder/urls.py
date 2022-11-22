from django.urls import path
from .views import saludo,probandoTemplate,desafio

urlpatterns = [
    path('saludo/', saludo),
    path('template/', probandoTemplate),
    path('', desafio),
]

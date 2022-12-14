from django.urls import path
from .views import saludo,probandoTemplate,desafio,altaData

urlpatterns = [
    path('saludo/', saludo),
    path('template/', probandoTemplate),
    path('', desafio),
]

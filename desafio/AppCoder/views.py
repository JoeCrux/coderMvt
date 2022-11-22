from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
# Create your views here.
from AppCoder.models import Persona

def saludo(request):
	return HttpResponse('Hola Django - Coder')

def probandoTemplate(request):
    return render(request,'template1.html')

def desafio(request):
    personas = Persona.objects.all()
    return render(request,'desafioMvt.html',{"personas":personas})


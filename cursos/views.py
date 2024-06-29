from django.shortcuts import render
from .models import Actividad
# Create your views here.

def actividad(request):
    actividades = Actividad.objects.all()
    return  render(request,"cursos/principal.html",{'9B':actividades})
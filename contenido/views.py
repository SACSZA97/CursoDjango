from django.shortcuts import render , HttpResponse

# Create your views here.

def principal(request):
     return render(request,"contenido/principal.html")

def contacto(request):

    return render(request,"contenido/contacto.html")

def formulario(request):

    return render(request,"contenido/cursos.html")

def base(request):

    return render(request,"contenido/base.html")
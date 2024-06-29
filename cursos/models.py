from django.db import models
from ckeditor .fields import RichTextField
# Create your models here.

class Cursos(models.Model):
    nombre = models.TextField(verbose_name="Nombre")
    curso = models.TextField(verbose_name="Curso")
    email = models.EmailField(verbose_name="Correo")
    turno = models.CharField(max_length=10,verbose_name="turno")
    created = models.DateTimeField(auto_now_add=True,verbose_name="creado")
    updated = models.DateTimeField(auto_now_add=True,verbose_name="actualizado")
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="INE")
    class Meta: 
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]

        def __str__(self):
         return self.curso

class Actividad(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre = models.TextField(verbose_name="Curso")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    desc = RichTextField(verbose_name="Descripcion")

    class Meta: 
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["created"]
    
    def __str__(self):
        return "Actividades del curso: " + self.nombre
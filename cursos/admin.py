from django.contrib import admin
from .models import Cursos
from .models import Actividad
# Register your models here.

class AdministrarCursos(admin.ModelAdmin):
    readonly_fields  = ('created', 'updated')
    list_display = ('id','nombre','created','updated')
    search_fields = ('id','created','updated')
    date_hierarchy = 'created'
    list_filter = ('curso','turno')

admin.site.register(Cursos, AdministrarCursos)

class AdministrarActividad(admin.ModelAdmin):
    readonly_fields  = ('id','created')
    list_display = ('id','nombre','created','desc')
    search_fields = ('id','nombre','created')
    date_hierarchy = 'created'
    list_filter = ('nombre','created')

admin.site.register(Actividad, AdministrarActividad)
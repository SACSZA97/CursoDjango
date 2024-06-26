from django.contrib import admin
from .models import Cursos
# Register your models here.

class AdministrarCursos(admin.ModelAdmin):
    readonly_fields  = ('created', 'updated')
    list_display = ('id','nombre','created','updated')
    search_fields = ('id','created','updated')
    date_hierarchy = 'created'
    list_filter = ('curso','turno')

admin.site.register(Cursos, AdministrarCursos)
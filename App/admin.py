from django.contrib import admin
from App.models import Docente


class DocenteAdmin(admin.ModelAdmin):
  list_display = ['nombre', 'apellido', 'fono', 'nivelAcademico', 'cursosAsignados', 'especialidad']

# Register your models here.
admin.site.register(Docente, DocenteAdmin)
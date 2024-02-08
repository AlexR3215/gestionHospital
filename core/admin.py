from django.contrib import admin

from .models import Hospital,Medico,Paciente

# Register your models here.


#Crear las clases del admin 
class HospitalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Hospital._meta.fields]
    list_filter = ('nombre','direccion','tipo','director')

#Registralrlos en la interfaz, se pasa la clase como la clase del admin
#La clase obtiene los campos y la clase admin muestra los campos deseados de la clase

admin.site.register(Hospital, HospitalAdmin)


class MedicoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Medico._meta.fields]
    list_filter = ('nombre','especialidad','hospitales')

admin.site.register(Medico, MedicoAdmin)

class PacienteAdmin( admin.ModelAdmin):
    list_display=[field.name for field in Paciente._meta.fields]
    list_filter = ('nombre','sexo','medico_tratante','hospital')

admin.site.register(Paciente, PacienteAdmin)
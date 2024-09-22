from django.contrib import admin
from .models import Medico, Hospital, Servicio, HospitalServicio, DirectorHospital, MedicoHospitalServicio, Habitacion, Cama, Paciente, Visita

# Registering each model in the admin panel

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('idmedico', 'dni', 'nombres','apellido_paterno','apellido_materno', 'fecha_nacimiento')

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('idhospital', 'codigo_hospital', 'nombre', 'ciudad', 'telefono')

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('idservicio', 'nombre_completo', 'comentario')

@admin.register(HospitalServicio)
class HospitalServicioAdmin(admin.ModelAdmin):
    list_display = ('idhospitalservicio', 'idhospital', 'idservicio', 'fecha_inicio', 'fecha_fin')

@admin.register(DirectorHospital)
class DirectorHospitalAdmin(admin.ModelAdmin):
    list_display = ('iddirectorhospital', 'idmedico', 'idhospital', 'fecha_inicio', 'fecha_fin')

@admin.register(MedicoHospitalServicio)
class MedicoHospitalServicioAdmin(admin.ModelAdmin):
    list_display = ('idmedicohospitalservicio', 'idmedico', 'idhospital', 'idservicio', 'fecha_inicio', 'fecha_fin')

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('idhabitacion', 'nombre_completo', 'idhospitalservicio')

@admin.register(Cama)
class CamaAdmin(admin.ModelAdmin):
    list_display = ('idcama', 'nombre_completo', 'idhabitacion', 'esta_ocupada')

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('codhist', 'dni', 'apellidos_nombre', 'fecha_nacimiento', 'num_seguridad_social')

@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('idvisita', 'fecha', 'hora', 'idhospital', 'idservicio', 'idmedico', 'codhist', 'diagnostico', 'tratamiento', 'es_ingreso', 'idcama', 'fecha_alta')


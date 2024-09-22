from django.contrib import admin
from .models import HospitalUsuario

@admin.register(HospitalUsuario)
class HospitalUsuarioAdmin(admin.ModelAdmin):
    list_display = ('idhospitalusuario', 'usuario', 'hospital', 'fecha_inicio', 'fecha_fin')
    search_fields = ('usuario__username', 'hospital__nombre')
    list_filter = ('hospital',)

    # Si quieres hacer que las fechas se muestren de manera más conveniente
    date_hierarchy = 'fecha_inicio'


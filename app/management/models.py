from django.db import models
from django.contrib.auth.models import User
from red.models import Hospital

class HospitalUsuario(models.Model):
    idhospitalusuario = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'HospitalUsuario'
        managed = True

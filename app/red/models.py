from django.db import models

class Medico(models.Model):
    idmedico = models.AutoField(db_column='idMedico', primary_key=True)
    dni = models.CharField(unique=True, max_length=9)
    nombres = models.CharField(db_column='nombres', max_length=100)
    fecha_nacimiento = models.DateField(db_column='fechaNacimiento')
    apellido_paterno = models.CharField(db_column='apellidoPaterno', max_length=100, null=True, blank=True)
    apellido_materno = models.CharField(db_column='apellidoMaterno', max_length=100, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Medico'

    def __str__(self) -> str:
        full_name = self.nombres
        if self.apellido_paterno:
            full_name += ' ' + self.apellido_paterno
        if self.apellido_materno:
            full_name += ' ' + self.apellido_materno
        return full_name


class Hospital(models.Model):
    idhospital = models.AutoField(db_column='idHospital', primary_key=True)
    codigo_hospital = models.CharField(db_column='codigoHospital', max_length=255)
    nombre = models.CharField
    codigo_hospital = models.CharField(db_column='codigoHospital', max_length=255)
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Hospital'

    def __str__(self) -> str:
        return self.nombre


class Servicio(models.Model):
    idservicio = models.AutoField(db_column='idServicio', primary_key=True)
    nombre_completo = models.CharField(db_column='nombreCompleto', max_length=200)
    comentario = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Servicio'

    def __str__(self) -> str:
        return self.nombre_completo

class HospitalServicio(models.Model):
    idhospitalservicio = models.AutoField(db_column='idHospitalServicio', primary_key=True)
    idhospital = models.ForeignKey(Hospital, db_column='idHospital', on_delete=models.CASCADE)
    idservicio = models.ForeignKey(Servicio, db_column='idServicio', on_delete=models.CASCADE)
    fecha_inicio = models.DateField(db_column='fechaInicio')
    fecha_fin = models.DateField(db_column='fechaFin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HospitalServicio'

    def __str__(self) -> str:
        return str(self.idhospitalservicio) + ' ' + self.idhospital.codigo_hospital + ' - ' + self.idservicio.nombre_completo

class DirectorHospital(models.Model):
    iddirectorhospital = models.AutoField(db_column='idDirectorHospital', primary_key=True)
    idmedico = models.ForeignKey(Medico, db_column='idMedico', on_delete=models.CASCADE)
    idhospital = models.ForeignKey(Hospital, db_column='idHospital', on_delete=models.CASCADE)
    fecha_inicio = models.DateField(db_column='fechaInicio')
    fecha_fin = models.DateField(db_column='fechaFin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DirectorHospital'


class MedicoHospitalServicio(models.Model):
    idmedicohospitalservicio = models.AutoField(db_column='idMedicoHospitalServicio', primary_key=True)
    idmedico = models.ForeignKey(Medico, db_column='idMedico', on_delete=models.CASCADE)
    idhospital = models.ForeignKey(Hospital, db_column='idHospital', on_delete=models.CASCADE)
    idservicio = models.ForeignKey(Servicio, db_column='idServicio', on_delete=models.CASCADE)
    fecha_inicio = models.DateField(db_column='fechaInicio')
    fecha_fin = models.DateField(db_column='fechaFin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MedicoHospitalServicio'


class Habitacion(models.Model):
    idhabitacion = models.AutoField(db_column='idHabitacion', primary_key=True)
    nombre_completo = models.CharField(db_column='nombreCompleto', max_length=200)
    idhospitalservicio = models.ForeignKey(HospitalServicio, db_column='idHospitalServicio', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Habitacion'

    def __str__(self) -> str:
        return self.nombre_completo


class Cama(models.Model):
    idcama = models.AutoField(db_column='idCama', primary_key=True)
    nombre_completo = models.CharField(db_column='nombreCompleto', max_length=200)
    idhabitacion = models.ForeignKey(Habitacion, db_column='idHabitacion', on_delete=models.CASCADE)
    esta_ocupada = models.BooleanField(db_column='estaOcupada', default=False)

    class Meta:
        managed = False
        db_table = 'Cama'

    def __str__(self) -> str:
        return self.nombre_completo


class Paciente(models.Model):
    codhist = models.AutoField(db_column='codHist', primary_key=True)
    dni = models.CharField(max_length=9)
    apellidos_nombre = models.CharField(db_column='apellidosNombre', max_length=100)
    fecha_nacimiento = models.DateField(db_column='fechaNacimiento')
    num_seguridad_social = models.CharField(db_column='numSeguridadSocial', max_length=15)
    otros_datos = models.CharField(db_column='otrosDatos',max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Paciente'

    def __str__(self) -> str:
        return self.apellidos_nombre

class Visita(models.Model):
    idvisita = models.AutoField(db_column='idVisita', primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    idhospital = models.ForeignKey(Hospital, db_column='idHospital', on_delete=models.CASCADE)
    idservicio = models.ForeignKey(Servicio, db_column='idServicio', on_delete=models.CASCADE)
    idmedico = models.ForeignKey(Medico, db_column='idMedico', on_delete=models.CASCADE)
    codhist = models.ForeignKey(Paciente, db_column='codHist', on_delete=models.CASCADE)
    diagnostico = models.CharField(max_length=255)
    tratamiento = models.CharField(max_length=255)
    es_ingreso = models.BooleanField(db_column='esIngreso', default=False)
    idcama = models.ForeignKey(Cama, db_column='idCama', blank=True, null=True, on_delete=models.SET_NULL)
    fecha_alta = models.DateField(db_column='fechaAlta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Visita'

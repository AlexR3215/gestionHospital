from django.db import models

# Create your models here.

class Hospital(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    TIPOS_HOSPITAL = [
        ('public', 'Público'),
        ('privado', 'Privado'),
        # Agrega más opciones según sea necesario
    ]
    tipo = models.CharField(max_length=20, choices=TIPOS_HOSPITAL)
    capacidad = models.IntegerField()
    director = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    hospitales = models.ManyToManyField(Hospital)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    SEXOS = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        # Agrega más opciones según sea necesario
    ]
    sexo = models.CharField(max_length=1, choices=SEXOS)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
    diagnostico = models.TextField()
    medico_tratante = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='pacientes')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='pacientes')

    def __str__(self):
        return self.nombre
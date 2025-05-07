from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, EmailValidator

class Pacientes(models.Model):
    nombre_paciente = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    apellido1_paciente = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    apellido2_paciente = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    edad_paciente = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    email_paciente = models.EmailField(unique=True, validators=[EmailValidator()])
    direccion_paciente = models.TextField(blank=True, null=True)
    telefono_paciente = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido1} {self.apellido2}"

class Doctores(models.Model):
    nombre_doctor = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    anos_experiencia = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    email_doctor = models.EmailField(unique=True, validators=[EmailValidator()])
    telefono_doctor = models.CharField(max_length=20, blank=True, null=True)
    direccion_doctor = models.TextField(blank=True, null=True)
    especialidad = models.ManyToManyField('Especialidades', through='Doctores_Especialidades')
    
    def __str__(self):
        return f"{self.nombre} ({self.anos_experiencia} años de experiencia)"

class Especialidades(models.Model):
    nombre_especialidad = models.CharField(max_length=100, unique=True, validators=[MinLengthValidator(3)])

    def __str__(self):
        return self.nombre

class Citas(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctores, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cita con {self.doctor} el {self.fecha} a las {self.hora}"

# Modelo de relación entre Doctores y Especialidades
class Doctores_Especialidades(models.Model):
    doctor = models.ForeignKey(Doctores, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.doctor} - {self.especialidad}"

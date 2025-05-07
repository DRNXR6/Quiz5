from rest_framework import serializers
from .models import *

class PacientesSerializer(serializers.ModelSerializer):
    def validar_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return value

    def validar_email(self, value):
        if not value:
            raise serializers.ValidationError("El correo electrónico es obligatorio.")
        return value

    class Meta:
        model = Pacientes
        fields = '__all__'

class DoctoresSerializer(serializers.ModelSerializer):
    def validar_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre del doctor debe tener al menos 3 caracteres.")
        return value

    class Meta:
        model = Doctores
        fields = '__all__'

class EspecialidadesSerializer(serializers.ModelSerializer):
    def validar_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre de la especialidad debe tener al menos 3 caracteres.")
        return value

    class Meta:
        model = Especialidades
        fields = '__all__'

class CitasSerializer(serializers.ModelSerializer):
    def validar_motivo(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("El motivo debe contener al menos 10 caracteres.")
        return value

    class Meta:
        model = Citas
        fields = '__all__'

class DoctoresEspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctores_Especialidades
        fields = '__all__'

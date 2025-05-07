from rest_framework.generics import *
from .models import *
from .serializers import *

class PacientesListCreateView(ListCreateAPIView):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer

class PacientesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer
############################################

class DoctoresListCreateView(ListCreateAPIView):
    queryset = Doctores.objects.all()
    serializer_class = DoctoresSerializer

class DoctoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Doctores.objects.all()
    serializer_class = DoctoresSerializer
############################################

class EspecialidadesListCreateView(ListCreateAPIView):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer

class EspecialidadesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer
############################################

class CitasListCreateView(ListCreateAPIView):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer

class CitasDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer
############################################

class DoctoresEspecialidadesListCreateView(ListCreateAPIView):
    queryset = Doctores_Especialidades.objects.all()
    serializer_class = DoctoresEspecialidadesSerializer

class DoctoresEspecialidadesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Doctores_Especialidades.objects.all()
    serializer_class = DoctoresEspecialidadesSerializer

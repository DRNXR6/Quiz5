from .views import *
from django.urls import path

urlpatterns = [
    path("pacientes/", PacientesListCreateView.as_view(), name="pacientes-list-create"),
    path("pacientes/<int:pk>/", PacientesDetailView.as_view(), name="pacientes-edit"),

    path("doctores/", DoctoresListCreateView.as_view(), name="doctores-list-create"),
    path("doctores/<int:pk>/", DoctoresDetailView.as_view(), name="doctores-edit"),

    path("especialidades/", EspecialidadesListCreateView.as_view(), name="especialidades-list-create"),
    path("especialidades/<int:pk>/", EspecialidadesDetailView.as_view(), name="especialidades-edit"),

    path("citas/", CitasListCreateView.as_view(), name="citas-list-create"),
    path("citas/<int:pk>/", CitasDetailView.as_view(), name="citas-edit"),

    path("doctor-especialidad/", DoctoresEspecialidadesListCreateView.as_view(), name="doctor-especialidad-list-create"),
    path("doctor-especialidad/<int:pk>/", DoctoresEspecialidadesDetailView.as_view(), name="doctor-especialidad-edit"),
]

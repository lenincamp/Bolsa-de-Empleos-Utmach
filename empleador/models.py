from django.db import models
from principal.models import Persona, Empleados

class Empleadores(Persona):
    Tipo_Persona = models.CharField(max_length=100, null=True)
    Nombre_Comercial = models.CharField(max_length=250, null=True)
    Tipo_Empresa = models.CharField(max_length=250, null=True)
    Pagina_Web = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.Nombre+" "+self.Apellido


class Oferta_Laboral(models.Model):
    Num_Oferta=models.CharField(max_length=15)
    Cargo_Solicitado=models.CharField(max_length=50)
    Numero_Cargos=models.IntegerField()
    Tipo_Contrato=models.CharField(max_length=50)
    Relacion_Laboral=models.CharField(max_length=50)
    Fecha_inicio=models.DateField()
    Fecha_fin=models.DateField()
    Fax=models.CharField(max_length=50)
    Contacto = models.CharField(max_length=150)
    Telefono = models.CharField(max_length=10)
    Celular = models.CharField(max_length=10)
    Correo=models.CharField(max_length=75)
    Discapacidad=models.CharField(max_length=50, default="Indistinto")
    id_Empleador=models.ForeignKey(Empleadores)


class Perfil_Cargo(models.Model):
    Instruccion=models.CharField(max_length=50)
    Area_Estudio=models.CharField(max_length=100)
    Remuneracion=models.CharField(max_length=50)
    Experiencia_minima=models.IntegerField()
    Experiencia_maxima=models.IntegerField()
    Conocimientos_cargo=models.CharField(max_length=350)
    Actividades_Desem=models.CharField(max_length=450)
    Capacitacion=models.CharField(max_length=100)
    Jornadas_Trabajo=models.CharField(max_length=100)
    Informacion_Adicional=models.CharField(max_length=100)
    id_Oferta=models.ForeignKey(Oferta_Laboral)


class Postulante(models.Model):
    id_Empleado=models.ForeignKey(Empleados)
    id_Oferta=models.ForeignKey(Oferta_Laboral)
    fecha_postulacion=models.DateField()
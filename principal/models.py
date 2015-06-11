from django.db import models
from django.utils import timezone

class Provincias(models.Model):
    NombreP = models.CharField(max_length=100)
    def __str__(self):
        return self.NombreP
class Ciudad(models.Model):
    NombreC     = models.CharField(max_length=100)
    idProvincia = models.ForeignKey(Provincias)
    def __str__(self):
         return self.NombreC

class Direccion(models.Model):
    Calle_Principal=models.CharField(max_length=75)
    Calle_Secundaria=models.CharField(max_length=75)
    Referencia=models.CharField(max_length=125)
    Sector=models.CharField(max_length=75)
    Numero=models.CharField(max_length=6)
    id_ciudad=models.ForeignKey(Ciudad)
    id_usuario=models.BigIntegerField()
    empleado = models.BooleanField()

class Persona(models.Model):
    CedulaRuc   = models.CharField(max_length=13)
    Nombre   = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Telefono1 = models.CharField(max_length=10)
    Telefono2 = models.CharField(max_length=10)
    Correo   = models.CharField(max_length=150)
    Clave    = models.CharField(max_length=16)
    class Meta:
        abstract=True


class Empleados(Persona):
    Etnia=models.CharField(max_length=75, null=True)
    Estado_Civil=models.CharField(max_length=50, null=True)
    Estado_Laboral=models.CharField(max_length=50, null=True)
    Fecha_Nacimiento=models.DateField(null=True)
    Tipo_Sangre = models.CharField(max_length=5, null=True)
    Sexo = models.CharField(max_length=1, null=True)
    def __str__(self):
         return self.Nombre+" "+self.Apellido

class Especiales(models.Model):
    Discapacidad=models.BooleanField(default=False)
    Enf_Catastrofica=models.BooleanField(default=False)
    Fam_enf_Severa=models.BooleanField(default=False)
    Fam_enf_Catastrofica=models.BooleanField(default=False)
    id_Empleado=models.ForeignKey(Empleados)

class Preferencias_laborales(models.Model):
    Sector_Publico=models.BooleanField(default=False)
    Sector_Privado=models.BooleanField(default=False)
    Aspiracion_Salarial=models.CharField(max_length=50)
    Lugar_Residencia=models.BooleanField(default=False)

class Detalle_Pref_Empl(models.Model):
    id_Empleado=models.ForeignKey(Empleados)
    id_Preferencias=models.ForeignKey(Preferencias_laborales)
    ciudad=models.ForeignKey(Ciudad)

class Oficios(models.Model):
    Nombre=models.CharField(max_length=75)
    def __str__(self):
         return self.Nombre

class SubActividades(models.Model):
    Descripcion=models.CharField(max_length=500)
    id_oficio=models.ForeignKey(Oficios)
    id_Empleado=models.ForeignKey(Empleados)

class Instruccion_Formal(models.Model):
    Nivel_Instruccion=models.CharField(max_length=75)
    Institucion=models.CharField(max_length=75)
    Titulo_Obtenido=models.CharField(max_length=75)
    Registro_Senescyt=models.CharField(max_length=50)
    id_Empleado=models.ForeignKey(Empleados)

class Idiomas(models.Model):
    Idioma=models.CharField(max_length=50)
    Nivel_hablado=models.CharField(max_length=50)
    Nivel_escrito=models.CharField(max_length=50)
    id_Empleado=models.ForeignKey(Empleados)

class Capacitaciones(models.Model):
    Institucion=models.CharField(max_length=150)
    Tipo_Evento=models.CharField(max_length=50)
    Area_Estudios=models.CharField(max_length=50)
    Nombre_Evento=models.CharField(max_length=250)
    Tipo_Certificado=models.CharField(max_length=50)
    Fecha_Desde=models.DateField()
    Fecha_Hasta=models.DateField()
    Dias=models.CharField(max_length=10)
    Horas=models.CharField(max_length=10)
    id_Empleado=models.ForeignKey(Empleados)

class AreaTrabajo(models.Model):
    Nombre=models.CharField(max_length=100)

class Experiencia(models.Model):
    Institucion=models.CharField(max_length=150)
    Puesto=models.CharField(max_length=100)
    Fecha_Desde=models.DateField(default=timezone.now)
    Fecha_Hasta=models.DateField(default=timezone.now)
    Actividades=models.TextField()
    Empleado=models.ForeignKey(Empleados)
    Area_Trabajo=models.ForeignKey(AreaTrabajo)

    def __unicode__(self):
        return self.Institucion


class Logros(models.Model):
    Tipo_Logro=models.CharField(max_length=50)
    Descripcion=models.CharField(max_length=250)
    id_Empleado=models.ForeignKey(Empleados)

class Referencias_Personales(models.Model):
    Nombres=models.CharField(max_length=150)
    Apellidos=models.CharField(max_length=150)
    Telefono=models.CharField(max_length=13)
    Correo=models.CharField(max_length=100)
    id_Empleado=models.ForeignKey(Empleados)



from django.db import models
from django.forms import ModelForm
from ubigeo.models import Ubigeo
#import obras.models


SEXO_CHOICES = (('0', 'Varon'), ('1', 'Mujer'), )

#estado_ch es para no eliminar por accidente un registro importante
ESTADO_CHOICES = (('0', 'Habilitado'), ('1', 'Eliminado'), )

ESTADO_CIVIL_CHOICES = (
    ('0', 'Soltero'), ('1', 'Casado'), ('2', 'Divorciado'), ('3', 'Viudo'), )


class Categoria(models.Model):
    descripcion = models.CharField(max_length=75)

    def __unicode__(self):
        return '%s' % (self.descripcion)


class Instruccion(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s' % (self.nombre)


class Tipo_Vivienda(models.Model):
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s' % (self.descripcion)


class Especialidad(models.Model):
    nombre = models.CharField(max_length=75)

    def __unicode__(self):
        return '%s' % (self.nombre)


class Base(models.Model):
    """
    Almacena los datos de una base, ejemplo: Tarapoto, Juanjui
    Y algunos datos que se necesitan para imprimir carnets

    correlativo: guarda el ultimo id de un afiliado, para x base
    """
    distrito = models.ForeignKey(Ubigeo)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=250)
    date_fundacion = models.DateField()
    logo = models.ImageField(upload_to='logos', blank=True)
    correlativo = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return '%s'%(self.nombre)


class Afiliado(models.Model):
    '''
    Registro de los afiliados

    id: es el numero de registro en el sistema
    correlativo: es el numero de afiliado en el padron
    '''
    correlativo = models.IntegerField(null=True)
    base = models.ForeignKey(Base, null=True)
    categoria = models.ForeignKey(Categoria)
    especialidad = models.ForeignKey(Especialidad)
    instruccion = models.ForeignKey(Instruccion)
    lugar_nacimiento = models.ForeignKey(Ubigeo)
    residencia = models.ForeignKey(Ubigeo, related_name='+')
    tipo_vivienda = models.ForeignKey(Tipo_Vivienda)
    apellidos = models.CharField(max_length=65)
    cuspp = models.CharField(max_length=12, null=True, blank=True)
    direccion = models.CharField(max_length=175, null=True, blank=True)
    dni = models.CharField(max_length=8, unique=True)
    essalud = models.CharField(max_length=16, null=True, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='0',blank=True)
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_CHOICES)
    fecha_inscripcion = models.DateField(null=True, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to='afiliados', blank=True, null=True)
    nombres = models.CharField(max_length=65)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    telefono = models.CharField(max_length=9, null=True, blank=True)

    def __unicode__(self):
        return '%s %s' % (self.nombres, self.apellidos)


class Tipo_Familiar(models.Model):
    nombre = models.CharField(max_length=35)

    def __unicode__(self):
        return '%s' % (self.nombre)


class Familiar(models.Model):
    afiliado = models.ForeignKey(Afiliado)
    tipo_familiar = models.ForeignKey(Tipo_Familiar)
    nombres = models.CharField(max_length=75)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    def __unicode__(self):
        return '%s' % (self.nombres)
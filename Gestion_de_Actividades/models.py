from django.db import models

# Create your models here.

# MODELO PARA COMPANIA
class Compania(models.Model):
    tipo = models.CharField(choices=("Persona Natural", "Persona Juridica", "Asociacion", "Consorcio",))
    nombre = models.CharField(max_length=40)
    ruc = models.CharField(max_length=13, null=True)
    direccion = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=15, null=True)
    correo = models.EmailField(null=True)
    representante = models.CharField(max_length=40)
    est = models.PositiveSmallIntegerField(editable=False, choices=(0, 1,), default=0)

# MODELO PARA CONTRATO
class Contrato(models.Model):
    numero_de_contrato = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=150)
    oferta = models.DecimalField(decimal_places=2)
    contratista = models.ManyToOneRel(field=Compania)
    fiscalizador = models.ManyToOneRel(field=Compania)
    est = models.PositiveSmallIntegerField(editable=False, choices=(0, 1,), default=0)


# MODELOS PARA GEOGODIGO
class Provincia(models.Model):
    codigo = models.PositiveSmallIntegerField(max_length=2)
    descripcion = models.CharField(max_length=30)
    est = models.PositiveSmallIntegerField(editable=False, choices=(0, 1,), default=0)

class Canton(models.Model):
    codigo = models.PositiveSmallIntegerField(max_length=2)
    descripcion = models.CharField(max_length=30)
    provincia = models.ForeignKey(Provincia)
    est = models.PositiveSmallIntegerField(editable=False, choices=(0, 1,), default=0)

class Sector(models.Model):
    codigo = models.PositiveSmallIntegerField(max_length=3)
    descripcion = models.CharField(max_length=30)
    canton = models.ForeignKey(Canton)
    est = models.PositiveSmallIntegerField(editable=False, choices=(0, 1,), default=0)

class Ruta(models.Model):
    codigo = models.PositiveSmallIntegerField(max_length=3)
    descripcion = models.CharField(max_length=30)
    sector = models.ForeignKey(Sector)
    est = models.PositiveSmallIntegerField(editable=False, choices=(0, 1,), default=0)

class Geocodigo(models.Model):
    secuencia = models.PositiveSmallIntegerField(max_length=7)
    ruta = models.ForeignKey(Ruta)
    est = models.PositiveSmallIntegerField(editable=False, choices=(0, 1,), default=0)

#MODELO MARCA DEL MEDIDOR
class Marca(models.Model):
    nombre = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=3)
    est = models.PositiveSmallIntegerField(editable=False, choices=(0, 1,), default=0)

    def __str__(self):
        return '%s-%s' % (self.abreviatura, self.nombre)

#MODELO PARA DATOS GENERALES DEL MEDIDOR
class Medidor(models.Model):
    fabrica = models.CharField(max_length=11)
    plan = models.CharField(max_length=1)
    serie = models.CharField(max_length=9)
    marca = models.OneToOneField(Marca)
    tension = models.PositiveIntegerField(max_length=3)
    estado = models.CharField(max_length=20)
    est = models.PositiveSmallIntegerField(editable=False, choices=(0, 1,), default=0)

#MODELO DEL CLIENTE
class Cliente(models.Model):
    ruc_ci = models.CharField(max_length=13)
    titular = models.CharField(max_length=40)
    cuenta = models.CharField(max_length=7)
    direccion = models.CharField(max_length=50)
    geocodigo = models.OneToOneField(Geocodigo)
    deuda = models.DecimalField(decimal_places=2)
    meses_adeudados = models.PositiveSmallIntegerField(max_length=4)
    estado = models.CharField(max_length=20)
    est = models.PositiveSmallIntegerField(editable=False, choices=(0, 1,), default=0)

#MODELO PARA MATERIAL
class Material(models.Model):
    nombre = models.CharField(max_length=90)
    cantidad = models.DecimalField(max_digits=2)
    unidad = models.CharField(choices=("UNIDAD(ES)", "METRO(S)",), default="UNIDAD(ES)")
    tipo_de_adquisicion = models.CharField(choices=("CONTRATANTE", "PROPIA",), default="CONTRATANTE")
    est = models.PositiveSmallIntegerField(editable=False, choices=(0, 1,), default=0)

#MODELO PARA MANO DE OBRA
class Mano_de_Obra(models.Model):
    descripcion = models.CharField(max_length=30)
    



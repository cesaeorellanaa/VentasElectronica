from django.db import models


# Create your models here.

class Cliente(models.Model):
    Nombre = models.CharField(max_length=500,
        help_text='Ej. César')
    Apellidos = models.CharField(max_length=500,
        help_text='Ej. Orellana')
    CorreoElectronico = models.CharField(max_length=500,
        help_text='Ej. ce.orellanaa@alumnos.duoc.cl')
    Direccion = models.CharField(max_length=500,
        help_text='Antonio Varas 666')
    Ciudad = models.CharField(max_length=500,
        help_text='Providencia')
    Pais = models.CharField(max_length=500,
        help_text='Chile')
    CodigoPostal = models.CharField(max_length=500,
        help_text='8640000')
    Telefono = models.CharField(max_length=500,
        help_text='+5692222222')


    def str(self):
        return self.CorreoElectronico





























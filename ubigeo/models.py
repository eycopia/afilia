from django.db import models


class Ubigeo(models.Model):
    departamento = models.IntegerField()
    provincia = models.IntegerField()
    distrito = models.IntegerField()
    nombre = models.CharField(max_length=70)

    def __unicode__(self):
        return '%s' % self.nombre
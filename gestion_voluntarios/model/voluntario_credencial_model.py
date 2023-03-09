import django
from django.db import models

from gestion_voluntarios.model.voluntario_model import Voluntario

django.setup()


class VoluntarioCredencial(models.Model):
    correo = models.CharField(max_length=30, default='')
    clave = models.CharField(max_length=20, default='')
    voluntario = models.ForeignKey('Voluntario', on_delete=models.CASCADE)

    @staticmethod
    def obtener_id_voluntario_por_correo_y_clave(correo, clave):
        try:
            voluntario_credencial = VoluntarioCredencial.objects.get(correo=correo, clave=clave)
            id_voluntario = Voluntario.obtener_voluntario_por_id(voluntario_credencial.voluntario.id).id
            return id_voluntario

        except VoluntarioCredencial.DoesNotExist:
            return None

        except Voluntario.DoesNotExist:
            return None

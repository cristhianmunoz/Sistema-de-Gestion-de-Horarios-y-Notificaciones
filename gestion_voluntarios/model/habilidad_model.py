import django
from django.core.exceptions import ValidationError
from django.db import models

from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica

django.setup()


class Habilidad(models.Model):
    titulo = models.CharField(max_length=20, choices=HabilidadMedica.choices)
    descripcion = models.CharField(max_length=200, default='')
    horas_experiencia = models.PositiveIntegerField(default=0)
    voluntario = models.ForeignKey('Voluntario', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Comprobando que el título de la habilidad exista
        if self.titulo not in HabilidadMedica:
            return

        # Comprobando que la cantidad de horas de experiencia sea correcta
        if not self.horas_experiencia > 0:
            return

        for habilidad in self.obtener_habilidades_por_id_voluntario(self.voluntario.id):
            # Comprobando que no se haya registrado la misma habilidad anteriormente para el voluntario
            if habilidad.titulo == self.titulo and habilidad.voluntario.id:
                return

        super().save(*args, **kwargs)

    @staticmethod
    def eliminar_habilidad(id_habilidad):
        try:
            Habilidad.objects.get(id=id_habilidad).delete()
            return True

        except Habilidad.DoesNotExist:
            return False

    @staticmethod
    def agregar_habilidad(habilidad):
        try:
            habilidad.save()
            return True

        except ValidationError:
            return False

    @staticmethod
    def editar_habilidad(habilidad):
        try:
            Habilidad.objects.filter(id=habilidad.id).update(
                titulo=habilidad.titulo,
                descripcion=habilidad.descripcion,
                horas_experiencia=habilidad.horas_experiencia
            )
            return True

        except ValidationError:
            return False

        except Habilidad.DoesNotExist:
            return False

    @staticmethod
    def obtener_habilidades_por_id_voluntario(id_voluntario):
        try:
            habilidades = Habilidad.objects.filter(voluntario_id=id_voluntario)
            return list(habilidades)

        except Habilidad.DoesNotExist:
            return None

    @staticmethod
    def obtener_numero_habilidades_por_id_voluntario(id_voluntario):
        try:
            return Habilidad.objects.filter(voluntario_id=id_voluntario).count()

        except Habilidad.DoesNotExist:
            return 0



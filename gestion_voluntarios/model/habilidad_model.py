import django
from django.core.exceptions import ValidationError
from django.db import models

from gestion_voluntarios.model.habilidad_medica_model import HabilidadMedica

django.setup()


class Habilidad(models.Model):
    # Campos de la clase Habilidad
    titulo = models.CharField(max_length=20, choices=HabilidadMedica.choices)
    descripcion = models.CharField(max_length=200, default='')
    horas_experiencia = models.PositiveIntegerField(default=0)
    voluntario = models.ForeignKey('Voluntario', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Comprobando que el título de la habilidad exista
        if self.titulo not in HabilidadMedica:
            return

        for habilidad in self.obtener_habilidades_por_id_voluntario(self.voluntario.id):
            # Comprobando que no se haya registrado la habilidad anteriormente para el voluntario
            if habilidad.titulo == self.titulo and habilidad.voluntario.id:
                return

        super().save(*args, **kwargs)

    # Recibe el código de una habilidad y la trata de eliminar de la base de datos
    @classmethod
    def eliminar_habilidad(cls, id_habilidad):
        try:
            habilidad = Habilidad.objects.get(id=id_habilidad)
            habilidad.delete()
            return True
        except Habilidad.DoesNotExist:
            return False

    # Agrega una habilidad nueva a la base de datos
    def agregar_habilidad(self):
        try:
            habilidad_nueva = Habilidad(
                titulo=self.titulo,
                descripcion=self.descripcion,
                horasExperiencia=self.horas_experiencia,
                voluntario=self.voluntario
            )
            # validar los campos del modelo antes de guardarlo
            habilidad_nueva.full_clean()
            habilidad_nueva.save()
            return True
        except ValidationError:
            # Maneja la excepción de validación de campos requeridos
            return False

    # Actualiza una habilidad existente tomando los valores de los campos de la instancia actual
    def editar_habilidad(self):
        try:
            habilidad_existente = self.objects.get(id=self.id)
            habilidad_existente.titulo = self.titulo
            habilidad_existente.descripcion = self.descripcion
            habilidad_existente.horas_experiencia = self.horas_experiencia
            habilidad_existente.save()
            return True
        except Habilidad.DoesNotExist:
            # Maneja la excepción si la Habilidad no existe para actualizarla
            return False

    # Método que recibe el código de un voluntario y retorna una lista de habilidades
    @staticmethod
    def obtener_habilidades_por_id_voluntario(id_voluntario):
        habilidades = Habilidad.objects.filter(voluntario_id=id_voluntario)
        return list(habilidades)

    @staticmethod
    def obtener_numero_habilidades_por_id_voluntario(id_voluntario):
        try:
            return Habilidad.objects.filter(voluntario_id=id_voluntario).count()
        except Habilidad.DoesNotExist:
            return 0

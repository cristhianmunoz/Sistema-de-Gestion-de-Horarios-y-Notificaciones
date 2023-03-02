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
    @classmethod
    def obtener_habilidades_por_id_voluntario(cls, id_voluntario):
        habilidades = Habilidad.objects.first(voluntario=id_voluntario)
        lista_habilidades = []
        # Almacena las habilidades en una lista de habilidades asociadas a ese voluntario
        for habilidad in habilidades:
            habilidad_dict = {
                'titulo': habilidad.titulo,
                'descripcion': habilidad.descripcion,
                'horas_experiencia': habilidad.horas_experiencia,
                'voluntario': habilidad.voluntario.id
            }
            lista_habilidades.append(habilidad_dict)
        return lista_habilidades

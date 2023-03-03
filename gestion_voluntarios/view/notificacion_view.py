from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from gestion_voluntarios.model.voluntario_model import Voluntario


class NotificacionView(View):
    def get(self, request, pk):
        # Obtener los datos de otra clase
        mi_voluntario = Voluntario.objects.get(pk=pk)
        voluntario = request.get_voluntarios()
        titulo = f"Emergencia médica: {voluntario.nombre}"
        print(voluntario.nombre)
        # Renderizar el template con los datos
        return render(request, '../static/templates/gestion_voluntarios/notificacion.html',
                      {'titulo': titulo})

    def post(self, request, pk):
        # Obtener los datos de otra clase
        mi_voluntario = Voluntario.objects.get(pk=pk)

        # Obtener la opción seleccionada por el usuario
        opcion = request.POST.get('opcion')

        # Manejar la opción seleccionada por el usuario
        if opcion == 'confirmar':
            print("Ha confirmado su asistencia")
            # Hacer algo si el usuario confirma la acción
        elif opcion == 'rechazar':
            print("Ha rechazado la emergencia médica")
            # Hacer algo si el usuario rechaza la acción

        # Redirigir al usuario a otra página
        return HttpResponseRedirect('/otra-pagina/')

    def notificar_emergencia(request):
        voluntario = request.get_voluntarios()
        titulo = f"Emergencia médica: {voluntario.nombre}"
        print(voluntario.nombre)
        return render(request, '../static/templates/gestion_voluntarios/notificacion.html', {'titulo': titulo})

    def get_voluntarios(self):
        """voluntarios = [
            Voluntario('Juan', 'Pérez', 30, 'Sutura', 'D'),
            Voluntario('Pepe', 'Rodríguez', 35, 'Primeros Auxilios', 'D'),
            Voluntario('Tomás', 'Muenala', 40, 'Sutura', 'D'),
            Voluntario('Ana', 'Freire', 25, 'Sutura', 'O'),
            Voluntario('Gerardo', 'Zapata', 23, 'Sutura', 'O')
        ]"""
        voluntarios = Voluntario('Juan', 'Pérez', 30, 'Sutura', 'D')

        return voluntarios

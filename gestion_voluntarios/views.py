from django.http import HttpResponse

from gestion_voluntarios.models import Voluntario


def index(request):
    person = Voluntario(nombre='John', apellido='Salazar', edad=20)
    person.save()

    return HttpResponse(Voluntario.objects.all()[0].nombre)

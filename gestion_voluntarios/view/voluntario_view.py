from django.http import HttpResponse


def index(request):

    return HttpResponse("Hola, esta será la pantalla principal del perfil Voluntario!")

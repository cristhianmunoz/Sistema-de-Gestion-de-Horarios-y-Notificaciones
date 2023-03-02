from django.shortcuts import render

from gestion_voluntarios.model.voluntario_model import Voluntario


def index(request):
    voluntario_id = request.GET.get('voluntario_id')
    contexto = {}

    if voluntario_id:
        try:
            voluntario = Voluntario.objects.get(id=voluntario_id)
            contexto = {'voluntario': voluntario}
        except Voluntario.DoesNotExist:
            contexto = {}

    return render(request=request, template_name='voluntario_test_view.html', context=contexto)

from django.shortcuts import redirect, render

from gestion_voluntarios.model.voluntario_credencial_model import VoluntarioCredencial


def index(request):
    correo = request.POST.get('correo')
    clave = request.POST.get('clave')

    if correo and clave:
        id_voluntario = VoluntarioCredencial.obtener_id_voluntario_por_correo_y_clave(correo, clave)

        if id_voluntario is not None:
            return redirect('/gestion_voluntarios/voluntario?id_voluntario={}'.format(id_voluntario))

    return render(request=request, template_name='voluntario_login.html')

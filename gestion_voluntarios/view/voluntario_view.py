from django.shortcuts import  render

def index(request):
    return render(request, 'gestion_voluntarios/notif_voluntarios.html')

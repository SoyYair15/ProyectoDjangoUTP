from django.contrib.auth.models import User

def project_context(request):

    context = {
        'me': User.objects.first(),
    }

    return context

# APARTADO DÓNDE LA FUNCIÓN TOMA EL OBJETO DE SOLICITUD COMO ARGUMENTO y DEVUELVE UN DICCIONARIO PARA FUSIONARLO EN EL CONTEXTO, Y ES ACCESIBLE EN TODAS LAS PLANTILLAS
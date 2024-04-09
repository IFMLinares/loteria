from django.contrib.sessions.models import Session
from django.http import JsonResponse
from django.dispatch import receiver
from allauth.account.signals import user_logged_in
from django.contrib.auth.signals import user_logged_out

# @receiver(user_logged_in)
# def limit_concurrent_sessions(request, user, **kwargs):
#     if not user.is_superuser:
#         # Si el usuario ya tiene una sesión activa, no permitir el inicio de sesión
#         if user.logged_in_user.session_key and Session.objects.filter(session_key=user.logged_in_user.session_key).exists():
#             # Aquí puedes manejar cómo quieres que se trate esta situación.
#             # Por ejemplo, podrías enviar una respuesta JSON:
#         # Guardar la clave de la sesión cuando el usuario inicie sesión
#         user.logged_in_user.session_key = request.session.session_key
#         user.logged_in_user.save()

@receiver(user_logged_out)
def clear_session_key(request, user, **kwargs):
    if not user.is_superuser:
        user.logged_in_user.session_key = None
        user.logged_in_user.save()

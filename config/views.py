from allauth.account.views import LoginView
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    def form_valid(self, form):
        self.user = form.user

        # # Si el usuario ya tiene una sesión activa, no permitir el inicio de sesión
        # if self.user.logged_in_user.session_key and Session.objects.filter(session_key=self.user.logged_in_user.session_key).exists():
        #     messages.error(self.request, 'Ya existe una sesión activa.')
        #     print('EXISTA UNA SESION ACTIVA')
        #     return redirect('account_login')
        # else:
        #     # Guardar la clave de la sesión cuando el usuario inicie sesión
        #     self.user.logged_in_user.session_key = self.request.session.session_key
        #     self.user.logged_in_user.save()
        #     return super().form_valid(form)

        return super().form_valid(form)

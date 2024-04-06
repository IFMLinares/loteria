from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse, reverse_lazy

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        if request.user.is_staff:
            # Si el usuario es un administrador, redirígelo a la URL del administrador
            return reverse_lazy('core:index')
        else:
            # Si el usuario no es un administrador, redirígelo a la URL normal
            return reverse_lazy('core:lottery')

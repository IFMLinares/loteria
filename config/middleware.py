from django.shortcuts import redirect

class AdminLoginRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/admin/login/' and request.user.is_authenticated:
            if request.user.is_staff:
                # Si el usuario es un administrador, redirígelo a 'core:index'
                return redirect('core:index')
            else:
                # Si el usuario no es un administrador, redirígelo a 'core:lottery'
                return redirect('core:lottery')

        response = self.get_response(request)
        return response

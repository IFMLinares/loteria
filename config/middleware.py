from django.shortcuts import redirect

class AdminLoginRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path == '/admin/login/' and request.user.is_authenticated:
            return redirect('core:index')
        return response
from django.http import HttpResponsePermanentRedirect

class CaseInsensitiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path != request.path.lower():
            return HttpResponsePermanentRedirect(request.path.lower())
        return self.get_response(request)
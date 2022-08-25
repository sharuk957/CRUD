from django.core import exceptions


class FilterIPMiddleware(object):
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def process_request(self,request):
        allowed_ips = ['127.0.0.1']
        ip = request.META.get('REMOTE_ADDR')
        if ip not in allowed_ips:
            raise exceptions.DisallowedHost("IP is not allowed")
        return None

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        return response
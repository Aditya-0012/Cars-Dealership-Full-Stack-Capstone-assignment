from django.http import HttpResponse
class LocalFrontendCorsMiddleware:
    def __init__(self,get_response): self.get_response=get_response
    def __call__(self,request):
        origin=request.headers.get('Origin','')
        allowed={'http://localhost:5173','http://127.0.0.1:5173'}
        if request.method=='OPTIONS' and origin in allowed:
            response=HttpResponse(status=204)
        else: response=self.get_response(request)
        if origin in allowed:
            response['Access-Control-Allow-Origin']=origin
            response['Access-Control-Allow-Credentials']='true'
            response['Access-Control-Allow-Headers']='Content-Type, X-CSRFToken'
            response['Access-Control-Allow-Methods']='GET, POST, OPTIONS'
            response['Vary']='Origin'
        return response

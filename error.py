from django.http import HttpResponse

class HttpError500(HttpResponse):
    status_code = 500
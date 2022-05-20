from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class CoreMiddleware(MiddlewareMixin):
    def process_reqeust(self, request):
        if request.method == "OPTIONS":
            return HttpResponse()

    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = '*'
        response["Access-Control-Allow-Headers"] = '*'
        response["Access-Control-Request-Method"] = '*'
        return response

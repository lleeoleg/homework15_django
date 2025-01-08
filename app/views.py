from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

def json_response_view(request):
    data = {"message": "Hello, this is a JSON response"}
    return JsonResponse(data)

def redirect_view(request):
    return redirect('https://example.com')

@require_http_methods(["GET"])
def get_only_view(request):
    return HttpResponse("Только GET-запросы разрешены")

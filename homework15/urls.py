from django.urls import path
from . import views

urlpatterns = [
    path('json-response/', views.json_response_view, name='json_response'),
    path('redirect/', views.redirect_view, name='redirect_view'),
    path('get-only/', views.get_only_view, name='get_only_view'),
]

from django.urls import path

from . import api

urlpatterns= [
    path('',api.procedures_list, name='api_procedures_list'),
    path('create/', api.create_procedure, name='api_create_procedures©')
]
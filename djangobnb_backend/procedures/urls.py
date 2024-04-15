from django.urls import path

from . import api

urlpatterns= [
    path('',api.procedures_list, name='api_procedures_list'),
    path('create/', api.create_procedure, name='api_create_procedure'),
    path('<uuid:pk>/', api.procedure_detail, name='api_procedures_detail'),
    path('<uuid:pk>/book/', api.book_procedure, name='api_book_procedure'),
    path('<uuid:pk>/reservations/', api.procedure_reservation, name='api_procedure_reservation'),
]
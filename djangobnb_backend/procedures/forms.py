from django.forms import ModelForm
from rest_framework import serializers

from .models import Procedures

class ProcedureForm(ModelForm):
    class Meta:
        model = Procedures
        fields = (
            'title',
            'description',
            'price_per_procedure',
            'payment',
            'country',
            'guests',
            'image',
        )


